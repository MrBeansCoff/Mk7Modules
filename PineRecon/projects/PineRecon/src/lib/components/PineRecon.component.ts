import { Component, OnDestroy, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

interface AccessPoint {
    bssid: string;
    ssid: string;
    channel: string;
    signal: number;
    security: string;
    securityTags: string[];
    hidden: boolean;
    wps: boolean;
    lastSeen: string;
    dataFrames: number;
    probes: number;
    clients: number;
    clientList: string[];
    vendor: string;
    mfp: string;
    securityDetails: SecurityDetails;
    taggedParameters: TaggedParameter[];
    x: number;
    y: number;
    delay: number;
}

interface SecurityDetails {
    summary: string;
    authentication: string[];
    groupCiphers: string[];
    pairwiseCiphers: string[];
}

interface TaggedParameter {
    name: string;
    value: string;
}

interface ModuleStatus {
    internet: boolean;
    interfaces: string[];
    oui_count: number;
    oui_path?: string;
    oui_error?: string;
    has_hcxdumptool: boolean;
    has_hcxpcapngtool?: boolean;
    has_aircrack: boolean;
    has_airodump?: boolean;
    capture_ready?: boolean;
    capture_engine?: string;
    has_dependencies?: boolean;
    dependencies_installing?: boolean;
    dependency_job_id?: string;
    dependency_packages?: string[];
    socket: string;
}

interface CaptureReport {
    file: string;
    size: number;
    modified: string;
    eapol_frames: number;
    pmkid_hashes?: number;
    eapol_hashes?: number;
    hash_lines?: number;
    messages: string[];
    message_counts: {[key: string]: number};
    usable_pairs?: string[];
    complete: boolean;
    partial?: boolean;
    accepted?: boolean;
    confidence: string;
    validation_tool?: string;
    hash_file?: string;
    message_pairs?: string[];
    error?: string;
    log_tail?: string;
    return_code?: number;
}

interface StatBucket {
    label: string;
    count: number;
    percent: number;
}

interface ClientRecord {
    mac: string;
    apBssid: string;
    apSsid: string;
    apChannel: string;
    security: string;
    mfp: string;
    dataFrames: number;
    broadcastProbes: number;
    directProbes: number;
    lastSeen: string;
    associated: boolean;
}

interface VendorMap {
    [key: string]: string;
}

interface HandshakePreflight {
    ready: boolean;
    blockers: string[];
    warnings: string[];
    suggestions: string[];
    capture_engine?: string;
    interface_info?: {
        type?: string;
        channel?: string;
        frequency?: string;
    };
    busy_processes?: Array<{pid: string; command: string}>;
}

@Component({
    selector: 'lib-PineRecon',
    templateUrl: './PineRecon.component.html',
    styleUrls: ['./PineRecon.component.css']
})
export class PineReconComponent implements OnInit, OnDestroy {
    logoPaths = [
        `${ApiService.extractBaseHref()}/modules/PineRecon/assets/pinerecon-logo.png`,
        `${ApiService.extractBaseHref()}/modules/pinerecon/assets/pinerecon-logo.png`,
        '/pineapple/ui/modules/PineRecon/assets/pinerecon-logo.png',
        '/pineapple/ui/modules/pinerecon/assets/pinerecon-logo.png',
        'assets/pinerecon-logo.png'
    ];
    logoPath = this.logoPaths[0];
    logoFailed = false;
    status: ModuleStatus = {
        internet: false,
        interfaces: [],
        oui_count: 0,
        has_hcxdumptool: false,
        has_hcxpcapngtool: false,
        has_aircrack: false,
        socket: '/tmp/modules/PineRecon.sock'
    };

    accessPoints: AccessPoint[] = [];
    clients: ClientRecord[] = [];
    captures: CaptureReport[] = [];
    channelStats: StatBucket[] = [];
    securityStats: StatBucket[] = [];
    selectedAp: AccessPoint = null;
    selectedClient: ClientRecord = null;
    selectedCapture: CaptureReport = null;
    activeCapture: CaptureReport = null;
    selectedCaptureFile = '';
    selectedApDetail = 'security';
    handshakePreflight: HandshakePreflight = null;
    pineDapBusy = false;
    pineDapMessage = '';
    scanning = false;
    capturing = false;
    dependencyBusy = false;
    dependencyChecked = false;
    statusLoaded = false;
    ouiChecked = false;
    loading = false;
    error = '';
    theme = 'dark';
    themes = [
        {value: 'dark', label: 'Pine Night'},
        {value: 'red', label: 'Red Zone'},
        {value: 'cobalt', label: 'Cobalt Grid'},
        {value: 'light', label: 'Light Ops'}
    ];
    band = 'both';
    scanTime = 15;
    captureDuration = 90;
    captureInterface = '';
    captureStartedAt = 0;
    scanId = '';
    scanPercent = 0;
    continuousScan = false;
    captureJobId = '';
    handshakeLog = '';
    lastUpdated = '';
    displayedColumns: string[] = ['signal', 'ssid', 'bssid', 'vendor', 'channel', 'security', 'wps', 'mfp', 'clients'];
    clientColumns: string[] = ['mac', 'ap', 'security', 'channel', 'data', 'lastSeen'];
    pageSize = 15;
    pageIndex = 0;
    clientPageIndex = 0;

    private poller: any = null;
    private logoIndex = 0;
    private ouiRetryCount = 0;

    constructor(private API: ApiService) {}

    ngOnInit() {
        this.loadSavedTheme();
        this.loadStatus();
        this.checkDependencies();
        this.loadRecon();
        this.loadCaptures();
    }

    ngOnDestroy() {
        if (this.poller) {
            clearInterval(this.poller);
        }
    }

    loadStatus(): void {
        this.API.request({module: 'PineRecon', action: 'status'}, (response) => {
            if (response && !response.error) {
                this.status = response;
                this.statusLoaded = true;
                if (!this.captureInterface && response.interfaces && response.interfaces.length) {
                    this.captureInterface = this.preferredCaptureInterface(response.interfaces);
                }
                if (response.dependencies_installing && response.dependency_job_id) {
                    this.dependencyBusy = true;
                    this.pollDependencyJob(response.dependency_job_id);
                }
                if (!response.oui_count && this.ouiRetryCount < 3) {
                    this.retryOuiLoad();
                } else {
                    this.ouiChecked = true;
                }
            }
        });
    }

    checkDependencies(): void {
        this.API.request({module: 'PineRecon', action: 'check_dependencies'}, (response) => {
            if (!response || response.error) {
                return;
            }

            this.status.has_dependencies = response.installed;
            this.status.dependencies_installing = response.installing;
            this.status.dependency_job_id = response.job_id;
            this.status.dependency_packages = response.packages || this.status.dependency_packages;
            this.status.has_hcxdumptool = response.package_state ? response.package_state.hcxdumptool : this.status.has_hcxdumptool;
            this.status.has_hcxpcapngtool = response.package_state ? response.package_state.hcxpcapngtool : this.status.has_hcxpcapngtool;
            this.status.has_aircrack = response.package_state ? response.package_state['aircrack-ng'] : this.status.has_aircrack;
            this.status.has_airodump = response.package_state ? response.package_state['airodump-ng'] : this.status.has_airodump;
            this.status.capture_ready = response.capture_ready !== undefined ? response.capture_ready : response.installed;
            this.status.capture_engine = response.capture_engine || this.status.capture_engine;
            this.dependencyChecked = true;
            if (response.installing && response.job_id) {
                this.dependencyBusy = true;
                this.pollDependencyJob(response.job_id);
            }
        });
    }

    reloadOuis(): void {
        this.API.request({module: 'PineRecon', action: 'reload_ouis'}, (response) => {
            this.ouiChecked = true;
            if (response && !response.error) {
                this.status.oui_count = response.oui_count;
                this.status.oui_path = response.oui_path;
                this.status.oui_error = response.oui_error;
            }
        });
    }

    startScan(): void {
        this.startRecon(this.scanTime, false);
    }

    startIndefiniteScan(): void {
        this.startRecon(0, true);
    }

    startRecon(scanTime: number, continuous: boolean): void {
        this.error = '';
        this.scanning = true;
        this.loading = true;
        this.continuousScan = continuous;
        this.scanPercent = 0;

        this.API.APIPost('/api/recon/start', {
            live: true,
            scan_time: scanTime,
            band: this.band
        }, (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.scanning = false;
                this.loading = false;
                return;
            }

            this.scanId = response && (response.scanID || response.scan_id) ? (response.scanID || response.scan_id).toString() : '';
            this.scanPercent = 0;
            this.notifyScan('start', scanTime);
            this.beginPolling();
        });
    }

    stopScan(): void {
        this.API.APIPost('/api/recon/stop', {}, () => {
            this.scanning = false;
            this.loading = false;
            this.continuousScan = false;
            if (this.poller) {
                clearInterval(this.poller);
                this.poller = null;
            }
            this.notifyScan('stop', 0);
            this.loadRecon();
        });
    }

    refresh(): void {
        this.ouiRetryCount = 0;
        this.ouiChecked = false;
        this.loadStatus();
        this.checkDependencies();
        this.loadRecon();
        this.loadCaptures();
    }

    installDependencies(): void {
        this.dependencyBusy = true;
        this.API.request({module: 'PineRecon', action: 'manage_dependencies', install: true}, (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.dependencyBusy = false;
                return;
            }

            if (response && response.installed) {
                this.dependencyBusy = false;
                this.checkDependencies();
                this.loadStatus();
                return;
            }

            this.pollDependencyJob(response.job_id);
        });
    }

    startHandshakeCapture(): void {
        if (!this.selectedAp) {
            this.error = 'Select an access point before starting a handshake capture.';
            return;
        }

        this.error = '';
        if (!this.captureInterface && this.status.interfaces && this.status.interfaces.length) {
            this.captureInterface = this.preferredCaptureInterface(this.status.interfaces);
        }
        if (!this.captureInterface) {
            this.error = 'Select a capture interface before starting a handshake capture.';
            return;
        }
        this.runHandshakePreflight((ready) => {
            if (!ready) {
                return;
            }
            this.runHandshakeCapture();
        });
    }

    startPineDap(): void {
        if (!this.selectedAp) {
            this.error = 'Select an access point before starting Pine DAP.';
            return;
        }
        this.error = '';
        this.pineDapBusy = true;
        this.pineDapMessage = 'Starting native PineAP handshake capture...';
        this.API.request({
            module: 'PineRecon',
            action: 'start_pineap_handshake',
            bssid: this.selectedAp.bssid,
            channel: this.selectedAp.channel
        }, (response) => {
            this.pineDapBusy = false;
            if (response && response.error) {
                this.error = response.error.message || response.error || 'Pine DAP failed to start.';
                this.pineDapMessage = '';
                return;
            }
            this.pineDapMessage = `Pine DAP started for ${this.selectedAp.ssid} on CH ${this.selectedAp.channel}.`;
        });
    }

    stopPineDap(): void {
        this.pineDapBusy = true;
        this.API.request({module: 'PineRecon', action: 'stop_pineap_handshake'}, (response) => {
            this.pineDapBusy = false;
            if (response && response.error) {
                this.error = response.error.message || response.error || 'Pine DAP stop failed.';
                return;
            }
            this.pineDapMessage = 'Pine DAP stopped.';
        });
    }

    private runHandshakeCapture(): void {
        this.capturing = true;
        this.captureStartedAt = Date.now();
        this.API.request({
            module: 'PineRecon',
            action: 'start_handshake_capture',
            interface: this.captureInterface,
            bssid: this.selectedAp.bssid,
            channel: this.selectedAp.channel,
            duration: this.captureDuration
        }, (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.capturing = false;
                this.captureStartedAt = 0;
                return;
            }

            this.captureJobId = response.job_id;
            this.activeCapture = this.emptyCaptureReport(response.output_file || 'running-capture');
            this.handshakeLog = '';
            this.pollCaptureJob();
        });
    }

    runHandshakePreflight(callback?: (ready: boolean) => void): void {
        this.API.request({
            module: 'PineRecon',
            action: 'handshake_preflight',
            interface: this.captureInterface,
            channel: this.selectedAp ? this.selectedAp.channel : ''
        }, (response) => {
            if (response && response.error) {
                this.error = response.error.message || response.error || 'Handshake preflight failed.';
                if (callback) {
                    callback(false);
                }
                return;
            }
            this.handshakePreflight = response;
            if (!response.ready) {
                this.error = (response.blockers || ['Handshake preflight failed.']).join(' ');
            }
            if (callback) {
                callback(!!response.ready);
            }
        });
    }

    stopHandshakeCapture(): void {
        this.API.request({module: 'PineRecon', action: 'stop_handshake_capture', job_id: this.captureJobId}, () => {
            this.capturing = false;
            this.captureStartedAt = 0;
            this.captureJobId = '';
            this.loadCaptures();
        });
    }

    selectAp(ap: AccessPoint): void {
        this.selectedAp = ap;
        this.selectedApDetail = 'security';
    }

    selectClient(client: ClientRecord): void {
        this.selectedClient = client;
        const ap = this.accessPoints.find((candidate) => {
            return (candidate.bssid || '').toUpperCase() === (client.apBssid || '').toUpperCase();
        });
        if (ap) {
            this.selectedAp = ap;
        }
    }

    startClientHandshake(): void {
        if (!this.selectedClient) {
            this.error = 'Select a client first.';
            return;
        }

        const ap = this.accessPoints.find((candidate) => {
            return (candidate.bssid || '').toUpperCase() === (this.selectedClient.apBssid || '').toUpperCase();
        });
        if (!ap) {
            this.error = 'Selected client is not associated with a targetable AP.';
            return;
        }

        this.selectedAp = ap;
        this.startHandshakeCapture();
    }

    selectCapture(capture: CaptureReport): void {
        this.selectedCapture = capture;
        this.selectedCaptureFile = capture ? capture.file : '';
        this.handshakeLog = capture.log_tail || this.handshakeLog;
    }

    selectCaptureByFile(fileName: string): void {
        const capture = this.captures.find((candidate) => candidate.file === fileName);
        if (capture) {
            this.selectCapture(capture);
        }
    }

    downloadSelectedCapture(): void {
        if (!this.selectedCapture) {
            return;
        }
        this.downloadCapture(this.selectedCapture);
    }

    downloadCapture(capture: CaptureReport): void {
        if (!capture) {
            return;
        }

        this.API.request({module: 'PineRecon', action: 'download_capture', file: capture.file}, (response) => {
            if (response && response.error) {
                this.error = response.error;
                return;
            }

            const binary = atob(response.content_b64 || '');
            const bytes = new Uint8Array(binary.length);
            for (let index = 0; index < binary.length; index++) {
                bytes[index] = binary.charCodeAt(index);
            }
            const blob = new Blob([bytes], {type: response.mime || 'application/vnd.tcpdump.pcap'});
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = response.file || capture.file;
            link.click();
            window.URL.revokeObjectURL(url);
        });
    }

    deleteSelectedCapture(): void {
        if (!this.selectedCapture) {
            return;
        }

        const file = this.selectedCapture.file;
        this.API.request({module: 'PineRecon', action: 'delete_capture', file}, (response) => {
            if (response && response.error) {
                this.error = response.error;
                return;
            }

            this.captures = this.captures.filter((capture) => capture.file !== file);
            this.selectedCapture = this.captures.length ? this.captures[0] : null;
            this.selectedCaptureFile = this.selectedCapture ? this.selectedCapture.file : '';
            if (!this.selectedCapture) {
                this.handshakeLog = '';
            }
        });
    }

    eapolCount(capture: CaptureReport, message: string): number {
        return capture && capture.message_counts ? (capture.message_counts[message] || 0) : 0;
    }

    handshakeReport(): CaptureReport {
        return this.activeCapture || this.selectedCapture;
    }

    captureReady(): boolean {
        return !!(this.status.capture_ready || this.status.has_hcxdumptool || this.status.has_airodump);
    }

    captureEngineLabel(): string {
        if (this.status.capture_engine) {
            return this.status.capture_engine;
        }
        if (this.status.has_hcxdumptool) {
            return 'hcxdumptool';
        }
        if (this.status.has_airodump) {
            return 'airodump-ng';
        }
        return 'No capture engine';
    }

    captureStatusLabel(capture: CaptureReport): string {
        if (!capture) {
            return 'none';
        }
        if ((capture.pmkid_hashes || 0) > 0) {
            return 'PMKID usable';
        }
        if ((capture.eapol_hashes || 0) > 0) {
            return 'EAPOL usable';
        }
        if (capture.complete) {
            return 'complete';
        }
        if (capture.accepted) {
            return 'usable pair';
        }
        if (capture.partial || capture.accepted || capture.eapol_frames > 0) {
            return 'partial';
        }
        return 'no EAPOL';
    }

    captureDurationLabel(): string {
        return Number(this.captureDuration) === 0 ? 'indefinite' : `${this.captureDuration}s`;
    }

    captureElapsedLabel(): string {
        if (!this.captureStartedAt) {
            return '00:00';
        }
        const seconds = Math.max(0, Math.floor((Date.now() - this.captureStartedAt) / 1000));
        const minutes = Math.floor(seconds / 60).toString().padStart(2, '0');
        const remainder = (seconds % 60).toString().padStart(2, '0');
        return `${minutes}:${remainder}`;
    }

    hasSecurityDetails(ap: AccessPoint): boolean {
        return !!(ap && ap.securityDetails && (
            ap.securityDetails.authentication.length ||
            ap.securityDetails.groupCiphers.length ||
            ap.securityDetails.pairwiseCiphers.length ||
            ap.securityDetails.summary
        ));
    }

    hasTaggedParameters(ap: AccessPoint): boolean {
        return !!(ap && ap.taggedParameters && ap.taggedParameters.length);
    }

    onThemeChange(theme: string): void {
        this.theme = theme;
        try {
            localStorage.setItem('PineRecon.theme', theme);
        } catch (error) {}
    }

    onLogoError(): void {
        this.logoIndex++;
        if (this.logoIndex < this.logoPaths.length) {
            this.logoPath = this.logoPaths[this.logoIndex];
        } else {
            this.logoFailed = true;
        }
    }

    get pagedAccessPoints(): AccessPoint[] {
        const start = this.pageIndex * this.pageSize;
        return this.accessPoints.slice(start, start + this.pageSize);
    }

    get pagedClients(): ClientRecord[] {
        const start = this.clientPageIndex * this.pageSize;
        return this.clients.slice(start, start + this.pageSize);
    }

    get apPageCount(): number {
        return Math.max(1, Math.ceil(this.accessPoints.length / this.pageSize));
    }

    get clientPageCount(): number {
        return Math.max(1, Math.ceil(this.clients.length / this.pageSize));
    }

    nextApPage(): void {
        this.pageIndex = Math.min(this.pageIndex + 1, this.apPageCount - 1);
    }

    prevApPage(): void {
        this.pageIndex = Math.max(this.pageIndex - 1, 0);
    }

    nextClientPage(): void {
        this.clientPageIndex = Math.min(this.clientPageIndex + 1, this.clientPageCount - 1);
    }

    prevClientPage(): void {
        this.clientPageIndex = Math.max(this.clientPageIndex - 1, 0);
    }

    downloadLogs(): void {
        this.API.request({module: 'PineRecon', action: 'get_logs'}, (response) => {
            if (response && response.error) {
                this.error = response.error;
                return;
            }

            let content = '';
            Object.keys(response || {}).forEach((name) => {
                content += `===== ${name} =====\n${response[name]}\n\n`;
            });
            const blob = new Blob([content], {type: 'text/plain'});
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = `PineRecon-logs-${new Date().toISOString()}.txt`;
            link.click();
            window.URL.revokeObjectURL(url);
        });
    }

    signalBars(signal: number): number[] {
        const strength = this.signalPercent(signal);
        const filled = strength > 80 ? 4 : strength > 58 ? 3 : strength > 34 ? 2 : strength > 12 ? 1 : 0;
        const bars = [];
        for (let i = 0; i < 4; i++) {
            bars.push(i < filled ? 1 : 0);
        }
        return bars;
    }

    signalPercent(signal: number): number {
        const clamped = Math.max(-95, Math.min(-30, signal || -95));
        return Math.round(((clamped + 95) / 65) * 100);
    }

    trackByBssid(index: number, ap: AccessPoint): string {
        return ap.bssid || index.toString();
    }

    private beginPolling(): void {
        if (this.poller) {
            clearInterval(this.poller);
        }

        this.loadRecon();
        this.poller = setInterval(() => this.checkScanStatus(), 2500);
    }

    private retryOuiLoad(): void {
        this.ouiRetryCount++;
        setTimeout(() => {
            this.API.request({module: 'PineRecon', action: 'reload_ouis'}, (response) => {
                if (response && !response.error && response.oui_count) {
                    this.status.oui_count = response.oui_count;
                    this.status.oui_path = response.oui_path;
                    this.status.oui_error = response.oui_error;
                    this.ouiChecked = true;
                    return;
                }

                if (this.ouiRetryCount < 3) {
                    this.retryOuiLoad();
                } else {
                    this.ouiChecked = true;
                    if (response && !response.error) {
                        this.status.oui_error = response.oui_error || this.status.oui_error;
                    }
                }
            });
        }, 900);
    }

    private notifyScan(event: string, duration: number): void {
        this.API.request({
            module: 'PineRecon',
            action: 'scan_notification',
            event,
            duration,
            band: this.band
        }, () => {});
    }

    private loadSavedTheme(): void {
        try {
            const savedTheme = localStorage.getItem('PineRecon.theme');
            if (savedTheme && this.themes.some((option) => option.value === savedTheme)) {
                this.theme = savedTheme;
            }
        } catch (error) {}
    }

    private emptyCaptureReport(file: string): CaptureReport {
        return {
            file,
            size: 0,
            modified: '',
            eapol_frames: 0,
            pmkid_hashes: 0,
            eapol_hashes: 0,
            hash_lines: 0,
            messages: [],
            message_counts: {M1: 0, M2: 0, M3: 0, M4: 0},
            usable_pairs: [],
            complete: false,
            partial: false,
            accepted: false,
            confidence: 'none',
            validation_tool: 'fallback',
            hash_file: '',
            message_pairs: []
        };
    }

    private preferredCaptureInterface(interfaces: string[]): string {
        const monitor = interfaces.find((iface) => /mon$/i.test(iface));
        if (monitor) {
            return monitor;
        }

        const external = interfaces.find((iface) => /^wlan[1-9]/i.test(iface));
        return external || interfaces[0];
    }

    private checkScanStatus(): void {
        this.API.APIGet('/api/recon/status', (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.scanning = false;
                this.loading = false;
                clearInterval(this.poller);
                this.poller = null;
                return;
            }

            const running = response && (response.scanRunning || response.continuous || response.running || response.scanning);
            this.scanPercent = response && response.scanPercent !== undefined ? response.scanPercent : this.scanPercent;
            if (response && (response.scanID || response.scan_id)) {
                this.scanId = (response.scanID || response.scan_id).toString();
            }
            this.loadRecon(this.scanId);

            if (!running) {
                this.scanning = false;
                this.loading = false;
                this.notifyScan('stop', 0);
                clearInterval(this.poller);
                this.poller = null;
            }
        });
    }

    private pollDependencyJob(jobId: string): void {
        this.API.request({module: 'PineRecon', action: 'poll_job', job_id: jobId, remove_if_complete: false}, (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.dependencyBusy = false;
                return;
            }

            if (response.is_complete) {
                this.dependencyBusy = false;
                this.loadStatus();
                this.checkDependencies();
                return;
            }

            setTimeout(() => this.pollDependencyJob(jobId), 2500);
        });
    }

    private pollCaptureJob(): void {
        this.API.request({module: 'PineRecon', action: 'poll_job', job_id: this.captureJobId, remove_if_complete: false}, (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.capturing = false;
                this.loadCaptures();
                return;
            }

            if (response.log_tail) {
                this.handshakeLog = response.log_tail;
            }

            if (response.is_complete) {
                this.capturing = false;
                this.captureStartedAt = 0;
                this.captureJobId = '';
                if (response.job_error) {
                    this.error = response.job_error;
                }
                if (response.result) {
                    this.activeCapture = response.result;
                    this.selectedCapture = response.result;
                    this.selectedCaptureFile = response.result.file || this.selectedCaptureFile;
                }
                if (response.result && response.result.log_tail) {
                    this.handshakeLog = response.result.log_tail;
                }
                this.loadCaptures();
                return;
            }

            this.loadHandshakeStatus();
            setTimeout(() => this.pollCaptureJob(), 3000);
        });
    }

    private loadHandshakeStatus(): void {
        if (!this.captureJobId) {
            return;
        }

        this.API.request({module: 'PineRecon', action: 'handshake_status', job_id: this.captureJobId}, (response) => {
            if (response && !response.error) {
                this.activeCapture = Object.assign(this.activeCapture || this.emptyCaptureReport(response.output_file || response.file || 'running-capture'), response);
                if (response.log_tail) {
                    this.handshakeLog = response.log_tail;
                }
            }
        });
    }

    private loadRecon(scanId?: string): void {
        if (scanId) {
            this.loadReconScan(scanId);
            return;
        }

        this.API.APIGet('/api/recon/scans', (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.loading = false;
                return;
            }

            const scans = this.normaliseArray(response);
            if (!scans.length) {
                this.accessPoints = [];
                this.clients = [];
                this.updateStats([]);
                this.loading = false;
                return;
            }

            const latest = scans[0];
            const latestId = (latest.scan_id || latest.scanID || latest.id || '').toString();
            if (!latestId) {
                this.loading = false;
                return;
            }
            this.loadReconScan(latestId);
        });
    }

    private loadReconScan(scanId: string): void {
        this.API.APIGet(`/api/recon/scans/${scanId}`, (response) => {
            if (response && response.error) {
                this.error = response.error;
                this.loading = false;
                return;
            }

            const aps = this.extractAccessPoints(response);
            this.accessPoints = aps;
            this.clients = this.extractClientRecords(response, aps);
            this.updateStats(aps);
            this.pageIndex = Math.min(this.pageIndex, this.apPageCount - 1);
            this.clientPageIndex = Math.min(this.clientPageIndex, this.clientPageCount - 1);
            if (!this.selectedAp && aps.length) {
                this.selectedAp = aps[0];
            }
            this.scanId = scanId;
            this.lastUpdated = new Date().toLocaleTimeString();
            this.loading = false;
            this.enrichVendors(aps);
        });
    }

    private loadCaptures(): void {
        this.API.request({module: 'PineRecon', action: 'list_captures'}, (response) => {
            if (response && !response.error) {
                this.captures = response;
                if (this.selectedCapture) {
                    this.selectedCapture = this.captures.find((capture) => capture.file === this.selectedCapture.file) || null;
                }
                if (!this.selectedCapture && this.captures.length) {
                    this.selectedCapture = this.captures[0];
                }
                if (!this.capturing) {
                    this.activeCapture = null;
                }
                this.selectedCaptureFile = this.selectedCapture ? this.selectedCapture.file : '';
            }
        });
    }

    private enrichVendors(aps: AccessPoint[]): void {
        this.API.request({module: 'PineRecon', action: 'enrich_aps', aps}, (response) => {
            if (!response || response.error || !response.vendors) {
                return;
            }

            const vendors: VendorMap = response.vendors;
            this.accessPoints = this.accessPoints.map((ap) => {
                const normalized = (ap.bssid || '').replace(/[^A-Fa-f0-9]/g, '').toUpperCase();
                ap.vendor = vendors[ap.bssid] || vendors[(ap.bssid || '').toUpperCase()] || vendors[normalized] || ap.vendor || 'Unknown';
                return ap;
            });
        });
    }

    private updateStats(aps: AccessPoint[]): void {
        this.channelStats = this.makeBuckets(aps.map((ap) => ap.channel || 'N/A'));
        this.securityStats = this.makeBuckets(aps.map((ap) => ap.security || 'Open'));
    }

    private makeBuckets(values: string[]): StatBucket[] {
        const total = values.length || 1;
        const counts = values.reduce((acc: {[key: string]: number}, value) => {
            acc[value] = (acc[value] || 0) + 1;
            return acc;
        }, {});

        return Object.keys(counts).map((label) => ({
            label,
            count: counts[label],
            percent: Math.round((counts[label] / total) * 100)
        })).sort((a, b) => b.count - a.count);
    }

    private extractAccessPoints(response: any): AccessPoint[] {
        const scans = this.normaliseArray(response);
        const latest = scans.length ? scans[0] : response;
        const rawAps = this.normaliseArray(latest && (latest.APResults || latest.ap_results || latest.access_points || latest.aps));

        return rawAps.map((ap, index) => this.mapAccessPoint(ap, index))
            .sort((a, b) => b.signal - a.signal);
    }

    private extractClientRecords(response: any, aps: AccessPoint[]): ClientRecord[] {
        const byBssid = aps.reduce((acc: {[key: string]: AccessPoint}, ap) => {
            acc[(ap.bssid || '').toUpperCase()] = ap;
            return acc;
        }, {});
        const latest = Array.isArray(response) ? response[0] : response;
        const records = [];

        aps.forEach((ap) => {
            const rawAp = this.findRawAp(latest, ap.bssid);
            this.normaliseArray(rawAp && rawAp.clients).forEach((client) => {
                records.push(this.mapClient(client, ap, true));
            });
        });

        const outOfRange = this.normaliseArray(latest && (latest.OutOfRangeClientResults || latest.OutOfRangeResult || latest.out_of_range_clients));
        const unassociated = this.normaliseArray(latest && (latest.UnassociatedClientResults || latest.UnassociatedResult || latest.unassociated_clients));

        outOfRange.concat(unassociated).forEach((client) => {
            const ap = byBssid[(client.ap_mac || client.ap_bssid || '').toUpperCase()];
            records.push(this.mapClient(client, ap, !!ap));
        });

        return records.sort((a, b) => b.dataFrames - a.dataFrames);
    }

    private findRawAp(response: any, bssid: string): any {
        const rawAps = this.normaliseArray(response && (response.APResults || response.ap_results || response.access_points || response.aps));
        return rawAps.find((ap) => (ap.bssid || ap.BSSID || '').toUpperCase() === (bssid || '').toUpperCase());
    }

    private mapClient(client: any, ap: AccessPoint, associated: boolean): ClientRecord {
        return {
            mac: typeof client === 'string' ? client : (client.client_mac || client.mac || client.client || ''),
            apBssid: ap ? ap.bssid : (client.ap_mac || client.ap_bssid || 'Unassociated'),
            apSsid: ap ? ap.ssid : 'Unassociated',
            apChannel: ap ? ap.channel : (client.ap_channel || 'N/A').toString(),
            security: ap ? ap.security : 'N/A',
            mfp: ap ? ap.mfp : 'Unknown',
            dataFrames: parseInt(client.data || '0', 10) || 0,
            broadcastProbes: parseInt(client.broadcast_probes || '0', 10) || 0,
            directProbes: parseInt(client.direct_probes || '0', 10) || 0,
            lastSeen: client.last_seen || 'N/A',
            associated
        };
    }

    private normaliseArray(value: any): any[] {
        if (!value) {
            return [];
        }

        if (Array.isArray(value)) {
            return value;
        }

        if (value.scans && Array.isArray(value.scans)) {
            return value.scans;
        }

        if (value.data && Array.isArray(value.data)) {
            return value.data;
        }

        return [];
    }

    private mapAccessPoint(ap: any, index: number): AccessPoint {
        const signal = parseInt(ap.signal || ap.rssi || ap.power || '-95', 10);
        const channel = (ap.channel || ap.chan || '').toString();
        const securityTags = this.securityTags(ap.encryption !== undefined ? ap.encryption : ap.security || ap.privacy);
        const clientList = this.extractClients(ap);
        const radians = ((index * 47) % 360) * (Math.PI / 180);
        const radius = 18 + (100 - this.signalPercent(signal)) * 0.28;

        return {
            bssid: ap.bssid || ap.BSSID || '',
            ssid: ap.ssid || ap.SSID || '<hidden>',
            channel,
            signal,
            security: securityTags.join(' / ') || 'Open',
            securityTags,
            hidden: !!ap.hidden,
            wps: !!ap.wps,
            lastSeen: ap.last_seen || ap.lastSeen || 'N/A',
            dataFrames: parseInt(ap.data || '0', 10) || 0,
            probes: parseInt(ap.probes || '0', 10) || 0,
            clients: clientList.length || parseInt(ap.clients || ap.client_count || '0', 10) || 0,
            clientList,
            vendor: 'Lookup pending',
            mfp: this.mfpState(ap),
            securityDetails: this.securityDetails(ap, securityTags),
            taggedParameters: this.taggedParameters(ap),
            x: 50 + Math.cos(radians) * radius,
            y: 50 + Math.sin(radians) * radius,
            delay: (index % 8) * 0.18
        };
    }

    private securityDetails(ap: any, securityTags: string[]): SecurityDetails {
        const authentication = this.valueList(
            ap.akm_suites || ap.akms || ap.auth_key_suites || ap.authentication_key_suites ||
            ap.authentication || ap.auth || ap.key_management || ap.keyManagement
        );
        const groupCiphers = this.valueList(
            ap.group_cipher_suites || ap.group_ciphers || ap.group_cipher || ap.groupCipher ||
            ap.group || ap.cipher
        );
        const pairwiseCiphers = this.valueList(
            ap.pairwise_cipher_suites || ap.pairwise_ciphers || ap.pairwise_cipher ||
            ap.pairwiseCipher || ap.pairwise || ap.ciphers
        );
        const ssid = ap.ssid || ap.SSID || '<hidden>';
        const bssid = ap.bssid || ap.BSSID || '';
        const security = securityTags.join(' and ') || 'Open';
        const authText = authentication.length ? authentication.join(', ') : 'unknown';
        const pairwiseText = pairwiseCiphers.length ? pairwiseCiphers.join(', ') : 'unknown';
        const groupText = groupCiphers.length ? groupCiphers.join(', ') : 'unknown';

        return {
            summary: `${ssid} (${bssid}) is using ${security} security with ${authText} authentication key suites, ${pairwiseText} pairwise ciphers, and ${groupText} group ciphers.`,
            authentication,
            groupCiphers,
            pairwiseCiphers
        };
    }

    private taggedParameters(ap: any): TaggedParameter[] {
        const raw = ap.tagged_parameters || ap.taggedParameters || ap.information_elements ||
            ap.informationElements || ap.InformationElements || ap.ies || ap.IEs || ap.ie;
        const items = this.normaliseObjectList(raw);

        return items.map((item, index) => {
            if (typeof item === 'string' || typeof item === 'number') {
                return {name: `Tag ${index + 1}`, value: item.toString()};
            }

            const name = item.name || item.tag || item.id || item.type || item.element || `Tag ${index + 1}`;
            const value = item.value || item.data || item.info || item.description || item.raw || item.hex || JSON.stringify(item);
            return {name: name.toString(), value: value.toString()};
        }).filter((item) => item.name || item.value);
    }

    private normaliseObjectList(value: any): any[] {
        if (!value) {
            return [];
        }
        if (Array.isArray(value)) {
            return value;
        }
        if (typeof value === 'object') {
            return Object.keys(value).map((key) => {
                const item = value[key];
                if (typeof item === 'object') {
                    return Object.assign({name: key}, item);
                }
                return {name: key, value: item};
            });
        }
        return [value];
    }

    private valueList(value: any): string[] {
        if (!value) {
            return [];
        }
        if (Array.isArray(value)) {
            return value.map((item) => item.toString()).filter((item) => item);
        }
        if (typeof value === 'object') {
            return Object.keys(value).map((key) => value[key] === true ? key : value[key].toString()).filter((item) => item);
        }
        return value.toString().split(/[,+/|;]/).map((item) => item.trim()).filter((item) => item);
    }

    private extractClients(ap: any): string[] {
        const clients = ap.clients || ap.Clients || ap.client_macs || [];
        if (!Array.isArray(clients)) {
            return [];
        }

        return clients.map((client) => {
            if (typeof client === 'string') {
                return client;
            }
            return client.client_mac || client.mac || client.client || client.station || client.bssid || '';
        }).filter((client) => client);
    }

    private securityTags(encryption: any): string[] {
        if (typeof encryption === 'string') {
            return encryption.split(/[,+/ ]+/).filter((tag) => tag);
        }

        const value = parseInt(encryption || '0', 10);
        if (!value) {
            return ['Open'];
        }

        const tags = [];
        if (value & 1) {
            tags.push('WEP');
        }
        if (value & 2) {
            tags.push('WPA');
        }
        if (value & 4) {
            tags.push('WPA2');
        }
        if (value & 8) {
            tags.push('WPA3');
        }
        return tags.length ? tags : [`Enc ${value}`];
    }

    private mfpState(ap: any): string {
        const value = ap.mfp !== undefined ? ap.mfp :
            ap.MFP !== undefined ? ap.MFP :
            ap.pmf !== undefined ? ap.pmf :
            ap.PMF !== undefined ? ap.PMF :
            ap.management_frame_protection !== undefined ? ap.management_frame_protection :
            ap.managementFrameProtection !== undefined ? ap.managementFrameProtection :
            ap.ieee80211w !== undefined ? ap.ieee80211w :
            ap.pmf_required !== undefined ? ap.pmf_required :
            ap.mfp_required;

        if (value === undefined || value === null || value === '') {
            return 'Unknown';
        }

        if (typeof value === 'boolean') {
            return value ? 'Enabled' : 'Disabled';
        }

        const text = value.toString().trim().toLowerCase();
        if (text === '2' || text.indexOf('required') !== -1) {
            return 'Required';
        }
        if (text === '1' || text.indexOf('capable') !== -1 || text.indexOf('enabled') !== -1 || text === 'true') {
            return 'Enabled';
        }
        if (text === '0' || text.indexOf('disabled') !== -1 || text === 'false') {
            return 'Disabled';
        }
        return value.toString();
    }

    get themeClass(): string {
        return `${this.theme}-theme`;
    }
}
