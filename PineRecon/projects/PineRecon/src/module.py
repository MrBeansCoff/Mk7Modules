#!/usr/bin/env python3
#======================================================================#
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣄⡀⢰⣿⡀⢀⡠⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠈⢷⣜⣿⢆⣿⣷⣿⣵⡞⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣾⣿⣿⣿⣿⣿⣿⣿⣶⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠴⣤⣼⡟⢉⣡⣤⣤⣤⣌⡙⢻⣥⣤⠤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣻⣿⣏⣤⠶⠶⢦⣌⣿⣾⣋⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣦⡀⠈⠉⠉⣹⣿⡿⣷⡞⠛⣶⣿⣿⣿⡋⠁⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠿⡟⣷⣆⣼⡿⣻⡖⠉⣹⢿⡋⠷⣿⣟⣿⣧⠀⠠⠶⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⣤⣿⣿⣿⣿⣿⣿⣾⣁⡼⡻⢤⣤⡽⢻⣥⣾⠿⣿⣷⣿⣿⣷⣶⣄⣀⣠⣤⣶⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⣤⣶⣒⡛⠛⠉⠉⠉⠉⠙⠛⠿⣿⣿⡗⣷⣞⣓⣿⣟⣿⣿⣻⣾⣿⣿⣛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠒⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠤⠼⠿⢿⡶⢂⠀⣶⣶⣶⠀⠀⣠⢿⣿⣿⢿⣿⡿⢿⣿⣿⣿⣿⣿⡏⠁⣀⣀⠀⠈⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣷⣶⣶⣶⣦⣤⣀⣀⣀⣀⣀⣀⠀
#⠀⠀⠀⠈⣻⠇⠉⢸⡿⠏⠉⠀⣸⠇⠀⣾⠉⠀⢸⠁⣸⡏⢠⣤⣤⣿⠃⢠⣿⠟⠃⢀⡾⠁⢀⣀⣀⡿⠋⢀⣀⠀⡹⠉⠀⣀⠀⣹⠆⠀⢻⡿⠉⣹⠷⠂
#⠀⢠⣤⣭⣿⠀⠀⣀⣀⣠⣶⣿⣿⠀⢰⡇⠀⡄⠀⢠⣿⠀⣨⣭⣯⣭⠀⣄⠀⠠⢶⣿⡓⠀⢈⣩⣽⡇⠀⣿⣿⣿⡇⠀⣿⡏⠀⣿⠀⡀⠐⡇⠀⣿⠿⠀
#⠀⠀⠀⢶⣟⣁⣺⣿⣿⣿⣿⣿⣇⣴⣿⣡⣼⣧⣤⣼⡏⠀⠛⢻⣿⡇⢠⣿⣷⡄⠀⠿⠁⠀⠉⠉⣽⡀⠈⠉⠁⣹⡄⠈⠛⠁⣸⠏⠀⣿⡄⠀⢸⣿⡄⠀
#⠀⠀⠀⣾⣿⣿⣿⠟⢛⣛⣛⣛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣦⣦⡙⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⠿⠿⠿⣿⠟⠛⠛⢷⣾⠇⠀⠀
#⠀⠀⠰⢻⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠒⠚⠻⠿⣿⣿⣿⣷⣶⣦⣤⣤⣤⣴⣿⣿⣮⣻⣿⣿⣿⠟⠛⠛⠙⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀
#⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠻⠿⠿⠿⠟⠛⠙⠛⠉⠳
# [VERSION]: 1.0 [AUTHOR]: MrBeansCoff⠀[MODULE_BUILD]: MK7 
# [CONTRIBUTERS]: 1⠀⠀⠀[LICENSE]: Apache License (2.0)
# 
# [SPILLED BEANS]: 
#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#             -  A new generation of MARK VII recon.
#======================================================================#

import base64
import json
import logging
import os
import pathlib
import re
import shutil
import signal
import struct
import subprocess
from datetime import datetime
from logging import Logger
from typing import Dict, List, Optional

import pineapple.helpers.notification_helpers as notifier
import pineapple.helpers.opkg_helpers as opkg
from pineapple.helpers.opkg_helpers import OpkgJob
from pineapple.helpers.network_helpers import check_for_internet, get_interfaces
from pineapple.modules import Module, Request
from pineapple.jobs import Job, JobManager


module = Module('PineRecon', logging.DEBUG)
job_manager = JobManager(name='PineRecon', module=module, log_level=logging.DEBUG)

OUI_CANDIDATES = [
    '/etc/pineapple/ouis',
]
OUIS: Dict[str, str] = {}
OUI_PATH = ''
OUI_ERROR = ''
DEPENDENCIES = ['hcxdumptool', 'aircrack-ng']
DEPENDENCY_BINARIES = {
    'hcxdumptool': ['hcxdumptool', '/usr/bin/hcxdumptool', '/usr/sbin/hcxdumptool', '/bin/hcxdumptool', '/sbin/hcxdumptool'],
    'hcxpcapngtool': ['hcxpcapngtool', '/usr/bin/hcxpcapngtool', '/usr/sbin/hcxpcapngtool', '/bin/hcxpcapngtool', '/sbin/hcxpcapngtool'],
    'aircrack-ng': ['aircrack-ng', 'aircrack', '/usr/bin/aircrack-ng', '/usr/sbin/aircrack-ng', '/bin/aircrack-ng', '/sbin/aircrack-ng'],
    'airodump-ng': ['airodump-ng', '/usr/bin/airodump-ng', '/usr/sbin/airodump-ng', '/bin/airodump-ng', '/sbin/airodump-ng'],
}
CAPTURE_DIRECTORY_PATH = '/root/.PineRecon/captures'
CAPTURE_DIRECTORY = pathlib.Path(CAPTURE_DIRECTORY_PATH)
HCX_DIRECTORY = pathlib.Path('/root/.hcxdumptool')
EAPOL_MARKER = b'\xaa\xaa\x03\x00\x00\x00\x88\x8e'


class HandshakeCaptureJob(Job[dict]):
    def __init__(self, interface: str, channel: str, bssid: str, duration: int, engine: str):
        super().__init__()
        self.interface = interface
        self.channel = channel
        self.bssid = _normalise_mac(bssid)
        requested_duration = int(duration if duration is not None else 60)
        self.duration = None if requested_duration == 0 else max(10, min(requested_duration, 900))
        self.engine = engine
        self.stem = f"{datetime.now().strftime('%Y-%m-%dT%H-%M-%S')}-handshake"
        if self.engine == 'airodump-ng':
            self.file_name = f'{self.stem}-01.cap'
            self.output_prefix = f'{CAPTURE_DIRECTORY_PATH}/{self.stem}'
            self.output_path = f'{self.output_prefix}-01.cap'
        else:
            self.file_name = f'{self.stem}.pcapng'
            self.output_prefix = ''
            self.output_path = f'{CAPTURE_DIRECTORY_PATH}/{self.file_name}'
        self.log_path = '/tmp/PineRecon-handshake.log'
        self.proc = None

    def do_work(self, logger: Logger) -> dict:
        command = self._command()

        logger.debug(f'Starting handshake capture: {command}')
        with open(self.log_path, 'w') as stdout_file:
            stdout_file.write(f'PineRecon target BSSID: {self.bssid or "any"}\n')
            stdout_file.write(f'PineRecon capture engine: {self.engine}\n')
            stdout_file.write(f'PineRecon duration: {self.duration if self.duration is not None else "indefinite"}\n')
            stdout_file.write(f'PineRecon command: {" ".join(command)}\n\n')
            stdout_file.flush()
            self.proc = subprocess.Popen(command, stdout=stdout_file, stderr=stdout_file, start_new_session=True)
            try:
                if self.duration is None:
                    self.proc.wait()
                else:
                    self.proc.wait(timeout=self.duration)
            except subprocess.TimeoutExpired:
                self.stop()

        result = _analyze_capture_file(pathlib.Path(self.output_path))
        result['file'] = self.file_name
        result['target_bssid'] = _format_mac(self.bssid) if self.bssid else ''
        result['capture_engine'] = self.engine
        result['return_code'] = self.proc.returncode if self.proc else None
        result['log_tail'] = _read_tail(self.log_path)

        if result['return_code'] not in [0, None] and result.get('size', 0) == 0:
            self.error = f'{self.engine} exited with code {result["return_code"]}. Download logs for command output.'

        return result

    def _command(self) -> List[str]:
        if self.engine == 'airodump-ng':
            command = ['airodump-ng', '--write', self.output_prefix, '--output-format', 'pcap']
            if self.bssid:
                command.extend(['--bssid', _format_mac(self.bssid)])
            if self.channel:
                command.extend(['--channel', str(self.channel)])
            command.append(self.interface)
            return command

        command = ['hcxdumptool', '-i', self.interface, '-o', self.output_path]
        if self.channel:
            command.extend(['-c', str(self.channel)])
        return command

    def stop(self):
        if self.proc and self.proc.poll() is None:
            try:
                os.killpg(os.getpgid(self.proc.pid), signal.SIGTERM)
            except Exception:
                self.proc.terminate()
            try:
                self.proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(os.getpgid(self.proc.pid), signal.SIGKILL)
                except Exception:
                    self.proc.kill()


def _normalise_mac(mac: str) -> str:
    return re.sub(r'[^A-Fa-f0-9]', '', mac or '').upper()


def _format_mac(mac: str) -> str:
    normalised = _normalise_mac(mac)
    if len(normalised) != 12:
        return mac
    return ':'.join(normalised[index:index + 2] for index in range(0, 12, 2))


def _lookup_vendor(mac: str) -> str:
    prefix = _normalise_mac(mac)[:6]
    if not prefix:
        return 'Unknown'
    return OUIS.get(prefix, 'Unknown')


def _normalise_oui_key(value: str) -> str:
    return _normalise_mac(value)[:6]


def _parse_oui_text(content: str) -> Dict[str, str]:
    records = {}
    for line in content.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        ieee_match = re.match(r'^([0-9A-Fa-f]{2})[-:]?([0-9A-Fa-f]{2})[-:]?([0-9A-Fa-f]{2})\s+\(hex\)\s+(.+)$', line)
        if ieee_match:
            records[''.join(ieee_match.group(index) for index in [1, 2, 3]).upper()] = ieee_match.group(4).strip()
            continue

        generic_match = re.match(r'^([0-9A-Fa-f]{2}[:-]?[0-9A-Fa-f]{2}[:-]?[0-9A-Fa-f]{2}|[0-9A-Fa-f]{6})[\s,;:=|-]+(.+)$', line)
        if generic_match:
            key = _normalise_oui_key(generic_match.group(1))
            vendor = generic_match.group(2).strip().strip('"')
            if len(key) == 6 and vendor:
                records[key] = vendor
    return records


def _load_ouis() -> None:
    global OUIS, OUI_PATH, OUI_ERROR
    OUIS = {}
    OUI_PATH = ''
    OUI_ERROR = ''

    candidates = list(OUI_CANDIDATES)
    for directory in ['/etc/pineapple', '/usr/share/pineapple', '/usr/share/ieee-data']:
        path = pathlib.Path(directory)
        if path.exists():
            candidates.extend(str(item) for item in path.iterdir() if item.is_file() and 'oui' in item.name.lower())

    seen = set()
    for candidate in candidates:
        if candidate in seen:
            continue
        seen.add(candidate)

        path = pathlib.Path(candidate)
        if not path.exists() or not path.is_file():
            continue

        try:
            content = path.read_text(errors='replace')
            if path.suffix.lower() == '.json' or content.lstrip().startswith('{'):
                raw = json.loads(content)
                if isinstance(raw, dict):
                    OUIS = {
                        _normalise_oui_key(str(key)): str(value)
                        for key, value in raw.items()
                        if len(_normalise_oui_key(str(key))) == 6
                    }
                elif isinstance(raw, list):
                    for item in raw:
                        if isinstance(item, dict):
                            key = _normalise_oui_key(str(item.get('oui') or item.get('prefix') or item.get('mac') or ''))
                            vendor = str(item.get('vendor') or item.get('name') or item.get('organization') or '')
                            if len(key) == 6 and vendor:
                                OUIS[key] = vendor
            else:
                OUIS = _parse_oui_text(content)

            if OUIS:
                OUI_PATH = str(path)
                module.logger.info(f'Loaded {len(OUIS)} OUI records from {OUI_PATH}')
                return
        except Exception as exc:
            OUI_ERROR = f'{path}: {exc}'
            module.logger.warning(f'Could not load OUI database from {path}: {exc}')

    if not OUI_ERROR:
        OUI_ERROR = 'No OUI database found in Pineapple paths.'
    module.logger.warning(OUI_ERROR)


def _has_binary(binary: str) -> bool:
    return os.path.isabs(binary) and os.path.exists(binary) or shutil.which(binary) is not None


def _has_named_tool(name: str) -> bool:
    return any(_has_binary(binary) for binary in DEPENDENCY_BINARIES.get(name, [name]))


def _select_capture_engine() -> str:
    if _has_named_tool('hcxdumptool'):
        return 'hcxdumptool'
    if _has_named_tool('airodump-ng'):
        return 'airodump-ng'
    return ''


def _dependency_state() -> dict:
    opkg_job_id: Optional[str] = None
    for job_id, runner in job_manager.jobs.items():
        if isinstance(runner.job, OpkgJob) and not runner.job.is_complete:
            opkg_job_id = job_id
            break

    package_state = {}
    for package in DEPENDENCIES:
        installed = opkg.check_if_installed(package, module.logger)
        if not installed:
            installed = any(_has_binary(binary) for binary in DEPENDENCY_BINARIES.get(package, [package]))
        package_state[package] = installed

    package_state['airodump-ng'] = _has_named_tool('airodump-ng')
    package_state['hcxpcapngtool'] = _has_named_tool('hcxpcapngtool')
    capture_engine = _select_capture_engine()
    installed = bool(capture_engine)
    return {
        'installed': installed,
        'installing': opkg_job_id is not None,
        'job_id': opkg_job_id,
        'packages': DEPENDENCIES,
        'package_state': package_state,
        'capture_engine': capture_engine,
        'capture_ready': installed,
    }


def _read_tail(path: str, max_chars: int = 4000) -> str:
    if not os.path.exists(path):
        return ''
    with open(path, 'r', errors='replace') as f:
        content = f.read()
    return content[-max_chars:]


def _run_command(command: List[str], timeout: int = 5) -> dict:
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=timeout)
        return {
            'ok': result.returncode == 0,
            'return_code': result.returncode,
            'stdout': result.stdout or '',
            'stderr': result.stderr or '',
        }
    except Exception as exc:
        return {'ok': False, 'return_code': None, 'stdout': '', 'stderr': str(exc)}


def _interface_iw_info(interface: str) -> dict:
    result = _run_command(['iw', 'dev', interface, 'info'])
    info = {
        'available': result['ok'],
        'type': '',
        'channel': '',
        'frequency': '',
        'raw': result['stdout'] or result['stderr'],
    }
    if not result['ok']:
        return info

    for line in result['stdout'].splitlines():
        line = line.strip()
        if line.startswith('type '):
            info['type'] = line.split(None, 1)[1]
        elif line.startswith('channel '):
            parts = line.split()
            if len(parts) > 1:
                info['channel'] = parts[1]
            if '(' in line and 'MHz' in line:
                info['frequency'] = line[line.find('(') + 1:line.find('MHz')].strip()
    return info


def _set_interface_channel(interface: str, channel: str) -> dict:
    channel = str(channel or '').strip()
    if not interface or not channel:
        return {'ok': False, 'message': 'Capture interface and target channel are required.'}

    result = _run_command(['iw', 'dev', interface, 'set', 'channel', channel], timeout=8)
    if not result['ok']:
        return {
            'ok': False,
            'message': f'Could not tune {interface} to channel {channel}.',
            'stdout': result['stdout'],
            'stderr': result['stderr'],
            'return_code': result['return_code'],
        }

    iw_info = _interface_iw_info(interface)
    if iw_info.get('channel') and str(iw_info['channel']) != channel:
        return {
            'ok': False,
            'message': f'{interface} stayed on channel {iw_info["channel"]}; target AP is channel {channel}.',
            'interface_info': iw_info,
        }

    return {'ok': True, 'interface_info': iw_info}


def _process_lines() -> List[str]:
    result = _run_command(['ps', 'w'])
    if not result['ok'] and not result['stdout']:
        result = _run_command(['ps'])
    return result['stdout'].splitlines()


def _busy_capture_processes(interface: str = '') -> List[dict]:
    process_names = ['hcxdumptool', 'airodump-ng', 'tcpdump', 'dumpcap', 'kismet']
    busy = []
    for line in _process_lines():
        if not any(name in line for name in process_names):
            continue
        if 'PineRecon' in line and 'grep' in line:
            continue
        if interface and interface not in line:
            continue
        parts = line.split(None, 4)
        busy.append({
            'pid': parts[0] if parts else '',
            'command': line.strip(),
        })
    return busy


def _active_handshake_jobs() -> List[str]:
    active = []
    for job_id, runner in job_manager.jobs.items():
        if isinstance(runner.job, HandshakeCaptureJob) and runner.job.proc and runner.job.proc.poll() is None:
            active.append(job_id)
    return active


def _handshake_preflight(interface: str, channel: str = '') -> dict:
    blockers = []
    warnings = []
    suggestions = []
    interfaces = get_interfaces()
    capture_engine = _select_capture_engine()

    if not capture_engine:
        blockers.append('No capture engine is available. Install hcxdumptool or aircrack-ng.')
    if not interface:
        blockers.append('No capture interface selected.')
    elif interface not in interfaces:
        blockers.append(f'Interface {interface} was not found.')

    iw_info = _interface_iw_info(interface) if interface else {'available': False, 'type': '', 'channel': '', 'frequency': '', 'raw': ''}
    if interface and not iw_info.get('available'):
        warnings.append(f'Could not read wireless mode for {interface} with iw.')
    elif iw_info.get('type') and iw_info.get('type') != 'monitor':
        warnings.append(f'{interface} is currently {iw_info["type"]}, not monitor mode.')

    if interface and re.match(r'^wlan0($|-)', interface):
        warnings.append(f'{interface} is commonly used for Pineapple management/AP duties.')

    active_jobs = _active_handshake_jobs()
    if active_jobs:
        blockers.append('A PineRecon handshake capture is already running.')

    busy_processes = _busy_capture_processes(interface)
    if busy_processes:
        blockers.append(f'{interface} already appears to be used by a capture process.')

    if channel and iw_info.get('channel') and str(channel) != str(iw_info['channel']):
        warnings.append(f'{interface} is currently on channel {iw_info["channel"]}; target AP is channel {channel}.')

    if not blockers and warnings:
        suggestions.append('Capture can start, but monitor-mode interfaces such as wlan1mon are usually most reliable.')
    elif not blockers:
        suggestions.append('Preflight looks ready.')

    return {
        'ready': not blockers,
        'blockers': blockers,
        'warnings': warnings,
        'suggestions': suggestions,
        'interface': interface,
        'interfaces': interfaces,
        'interface_info': iw_info,
        'capture_engine': capture_engine,
        'busy_processes': busy_processes,
    }


def _notify_capture_finished(job: HandshakeCaptureJob):
    if not job.was_successful:
        module.send_notification(job.error, notifier.ERROR)
    elif job.result and job.result.get('accepted'):
        module.send_notification('PineRecon captured usable WPA handshake material.', notifier.SUCCESS)
    else:
        module.send_notification('PineRecon capture finished. No usable WPA handshake material was confirmed.', notifier.WARN)


def _notify_dependencies_finished(job: OpkgJob):
    if not job.was_successful:
        module.send_notification(job.error, notifier.ERROR)
    elif job.install:
        module.send_notification('PineRecon dependencies finished installing.', notifier.SUCCESS)


def _extract_eapol_from_packet(packet: bytes, linktype: int) -> List[dict]:
    frames = []
    search_start = 0
    while True:
        marker_index = packet.find(EAPOL_MARKER, search_start)
        if marker_index == -1:
            break

        eapol_offset = marker_index + len(EAPOL_MARKER)
        eapol = packet[eapol_offset:eapol_offset + 128]
        if len(eapol) >= 8:
            key_info = struct.unpack('>H', eapol[5:7])[0] if eapol[1] == 3 else 0
            frames.append({
                'eapol_type': int(eapol[1]),
                'key_info': key_info,
                'message': _classify_eapol_message(key_info),
                'linktype': linktype,
            })
        search_start = eapol_offset
    return frames


def _classify_eapol_message(key_info: int) -> str:
    has_mic = bool(key_info & 0x0100)
    has_ack = bool(key_info & 0x0080)
    has_install = bool(key_info & 0x0040)
    has_secure = bool(key_info & 0x0200)

    if has_ack and not has_mic:
        return 'M1'
    if has_mic and not has_ack and not has_secure:
        return 'M2'
    if has_ack and has_mic and has_install:
        return 'M3'
    if has_mic and has_secure and not has_ack:
        return 'M4'
    return 'EAPOL'


def _empty_capture_report(path: pathlib.Path, error: str = '') -> dict:
    report = {
        'file': path.name,
        'size': 0,
        'eapol_frames': 0,
        'pmkid_hashes': 0,
        'eapol_hashes': 0,
        'hash_lines': 0,
        'messages': [],
        'message_counts': {'M1': 0, 'M2': 0, 'M3': 0, 'M4': 0},
        'complete': False,
        'partial': False,
        'accepted': False,
        'confidence': 'none',
        'validation_tool': 'fallback',
    }
    if error:
        report['error'] = error
    return report


def _usable_eapol_pairs(message_counts: dict) -> List[str]:
    pairs = []
    if message_counts.get('M1', 0) and message_counts.get('M2', 0):
        pairs.append('M1+M2')
    if message_counts.get('M2', 0) and message_counts.get('M3', 0):
        pairs.append('M2+M3')
    if message_counts.get('M3', 0) and message_counts.get('M4', 0):
        pairs.append('M3+M4')
    if message_counts.get('M1', 0) and message_counts.get('M4', 0):
        pairs.append('M1+M4')
    return pairs


def _validate_capture_hashes(path: pathlib.Path) -> dict:
    if not _has_named_tool('hcxpcapngtool'):
        return {'available': False, 'pmkid_hashes': 0, 'eapol_hashes': 0, 'hash_lines': 0, 'message_pairs': []}

    hash_path = pathlib.Path(f'{path}.hc22000')
    if hash_path.exists():
        try:
            hash_path.unlink()
        except Exception:
            pass

    result = _run_command(['hcxpcapngtool', '-o', str(hash_path), str(path)], timeout=45)
    hash_lines = []
    if hash_path.exists():
        try:
            hash_lines = [line.strip() for line in hash_path.read_text(errors='replace').splitlines() if line.strip().startswith('WPA*')]
        except Exception:
            hash_lines = []

    pmkid_lines = [line for line in hash_lines if line.startswith('WPA*01*')]
    eapol_lines = [line for line in hash_lines if line.startswith('WPA*02*')]
    message_pairs = []
    for line in eapol_lines:
        parts = line.split('*')
        if parts:
            message_pairs.append(parts[-1])

    return {
        'available': True,
        'ok': result['ok'] or bool(hash_lines),
        'pmkid_hashes': len(pmkid_lines),
        'eapol_hashes': len(eapol_lines),
        'hash_lines': len(hash_lines),
        'message_pairs': sorted(set(message_pairs)),
        'hash_file': hash_path.name if hash_lines else '',
        'stdout': result['stdout'][-1200:],
        'stderr': result['stderr'][-1200:],
        'return_code': result['return_code'],
    }


def _parse_classic_pcap(data: bytes) -> List[dict]:
    if len(data) < 24:
        return []

    magic = data[:4]
    if magic == b'\xd4\xc3\xb2\xa1':
        endian = '<'
    elif magic == b'\xa1\xb2\xc3\xd4':
        endian = '>'
    else:
        return _scan_eapol_bytes(data)

    linktype = struct.unpack(f'{endian}I', data[20:24])[0]
    offset = 24
    frames = []

    while offset + 16 <= len(data):
        incl_len = struct.unpack(f'{endian}I', data[offset + 8:offset + 12])[0]
        offset += 16
        packet = data[offset:offset + incl_len]
        frames.extend(_extract_eapol_from_packet(packet, linktype))
        offset += incl_len

    return frames


def _scan_eapol_bytes(data: bytes) -> List[dict]:
    frames = []
    search_start = 0
    while True:
        marker_index = data.find(EAPOL_MARKER, search_start)
        if marker_index == -1:
            break
        eapol_offset = marker_index + len(EAPOL_MARKER)
        eapol = data[eapol_offset:eapol_offset + 128]
        if len(eapol) >= 8:
            key_info = struct.unpack('>H', eapol[5:7])[0] if eapol[1] == 3 else 0
            frames.append({'eapol_type': int(eapol[1]), 'key_info': key_info, 'message': _classify_eapol_message(key_info)})
        search_start = eapol_offset
    return frames


def _analyze_capture_file(path: pathlib.Path) -> dict:
    if not path.exists() or not path.is_file():
        return _empty_capture_report(path, 'Capture file not found')

    with open(str(path), 'rb') as f:
        data = f.read()

    frames = _parse_classic_pcap(data)
    messages = sorted(set(frame['message'] for frame in frames))
    message_counts = {
        'M1': len([frame for frame in frames if frame['message'] == 'M1']),
        'M2': len([frame for frame in frames if frame['message'] == 'M2']),
        'M3': len([frame for frame in frames if frame['message'] == 'M3']),
        'M4': len([frame for frame in frames if frame['message'] == 'M4']),
    }
    complete = all(message in messages for message in ['M1', 'M2', 'M3', 'M4'])
    usable_pairs = _usable_eapol_pairs(message_counts)
    hcx_validation = _validate_capture_hashes(path)
    pmkid_hashes = hcx_validation.get('pmkid_hashes', 0)
    eapol_hashes = hcx_validation.get('eapol_hashes', 0)
    hash_lines = hcx_validation.get('hash_lines', 0)
    accepted = bool(hash_lines or usable_pairs)
    partial = bool(frames) and not accepted
    if pmkid_hashes:
        confidence = 'pmkid'
    elif eapol_hashes:
        confidence = 'eapol'
    elif complete:
        confidence = 'complete'
    elif usable_pairs:
        confidence = 'pair'
    elif frames:
        confidence = 'partial'
    else:
        confidence = 'none'

    return {
        'file': path.name,
        'size': path.stat().st_size,
        'modified': datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
        'eapol_frames': len(frames),
        'pmkid_hashes': pmkid_hashes,
        'eapol_hashes': eapol_hashes,
        'hash_lines': hash_lines,
        'messages': messages,
        'message_counts': message_counts,
        'usable_pairs': usable_pairs,
        'complete': complete,
        'partial': partial,
        'accepted': accepted,
        'confidence': confidence,
        'validation_tool': 'hcxpcapngtool' if hcx_validation.get('available') else 'fallback',
        'hash_file': hcx_validation.get('hash_file', ''),
        'message_pairs': hcx_validation.get('message_pairs', []),
    }


def _capture_files() -> List[pathlib.Path]:
    paths = []
    for directory in [CAPTURE_DIRECTORY, HCX_DIRECTORY]:
        if directory.exists():
            paths.extend([item for item in directory.iterdir() if item.is_file() and item.suffix.lower() in ['.pcap', '.pcapng', '.cap']])
    return sorted(paths, key=lambda item: item.stat().st_mtime, reverse=True)


def _capture_file_by_name(filename: str) -> Optional[pathlib.Path]:
    safe_name = pathlib.Path(filename or '').name
    if not safe_name:
        return None
    for path in _capture_files():
        if path.name == safe_name:
            return path
    return None


def _running_job(job_id: str) -> Optional[HandshakeCaptureJob]:
    runner = job_manager.jobs.get(job_id)
    if not runner or not isinstance(runner.job, HandshakeCaptureJob):
        return None
    return runner.job


@module.on_start()
def on_start():
    CAPTURE_DIRECTORY.mkdir(parents=True, exist_ok=True)
    _load_ouis()


@module.handles_action('status')
def status(request: Request):
    if not OUIS:
        _load_ouis()
    dependencies = _dependency_state()
    return {
        'internet': check_for_internet(logger=module.logger),
        'interfaces': get_interfaces(),
        'oui_count': len(OUIS),
        'oui_path': OUI_PATH,
        'oui_error': OUI_ERROR,
        'has_hcxdumptool': dependencies['package_state'].get('hcxdumptool', False),
        'has_hcxpcapngtool': dependencies['package_state'].get('hcxpcapngtool', False),
        'has_aircrack': dependencies['package_state'].get('aircrack-ng', False),
        'has_airodump': dependencies['package_state'].get('airodump-ng', False),
        'has_dependencies': dependencies['installed'],
        'capture_ready': dependencies['capture_ready'],
        'capture_engine': dependencies['capture_engine'],
        'dependencies_installing': dependencies['installing'],
        'dependency_job_id': dependencies['job_id'],
        'dependency_packages': dependencies['packages'],
        'socket': f'/tmp/modules/{module.name}.sock',
    }


@module.handles_action('check_dependencies')
def check_dependencies(request: Request):
    return _dependency_state()


@module.handles_action('reload_ouis')
def reload_ouis(request: Request):
    _load_ouis()
    return {
        'oui_count': len(OUIS),
        'oui_path': OUI_PATH,
        'oui_error': OUI_ERROR,
    }


@module.handles_action('lookup_oui')
def lookup_oui(request: Request):
    if not OUIS:
        _load_ouis()
    mac = getattr(request, 'mac', '')
    normalised = _normalise_mac(mac)

    if len(normalised) < 6:
        return {'mac': mac, 'vendor': 'Invalid MAC', 'valid': False}

    return {
        'mac': mac,
        'prefix': normalised[:6],
        'vendor': _lookup_vendor(mac),
        'valid': True,
    }


@module.handles_action('enrich_aps')
def enrich_aps(request: Request):
    if not OUIS:
        _load_ouis()
    aps: List[dict] = getattr(request, 'aps', [])
    vendors = {}

    for ap in aps:
        bssid = ap.get('bssid') or ap.get('BSSID') or ''
        normalised = _normalise_mac(bssid)
        if len(normalised) >= 6:
            vendor = _lookup_vendor(bssid)
            vendors[bssid] = vendor
            vendors[bssid.upper()] = vendor
            vendors[normalised] = vendor

    return {'vendors': vendors}


@module.handles_action('manage_dependencies')
def manage_dependencies(request: Request):
    state = _dependency_state()
    if state['installed']:
        return {'installed': True, 'job_id': None}
    if state['installing']:
        return {'job_id': state['job_id']}
    return {'job_id': job_manager.execute_job(OpkgJob(DEPENDENCIES, request.install), callbacks=[_notify_dependencies_finished])}


@module.handles_action('scan_notification')
def scan_notification(request: Request):
    event = getattr(request, 'event', '')
    if event == 'start':
        duration = getattr(request, 'duration', 0)
        band = getattr(request, 'band', 'both')
        if int(duration or 0) == 0:
            module.send_notification(f'PineRecon indefinite recon scan started on {band} band.', notifier.INFO)
        else:
            module.send_notification(f'PineRecon recon scan started for {duration}s on {band} band.', notifier.INFO)
        return True
    if event == 'stop':
        module.send_notification('PineRecon recon scan stopped.', notifier.WARN)
        return True
    return 'Unknown scan notification event.', False


@module.handles_action('handshake_preflight')
def handshake_preflight(request: Request):
    return _handshake_preflight(getattr(request, 'interface', ''), getattr(request, 'channel', ''))


@module.handles_action('start_handshake_capture')
def start_handshake_capture(request: Request):
    capture_engine = _select_capture_engine()
    if not capture_engine:
        return 'No capture engine is available. Install hcxdumptool or aircrack-ng.', False

    interface = getattr(request, 'interface', '')
    channel = getattr(request, 'channel', '')
    preflight = _handshake_preflight(interface, channel)
    if not preflight['ready']:
        return {'message': 'Handshake preflight failed.', 'preflight': preflight}, False

    if channel:
        tune_result = _set_interface_channel(interface, channel)
        if not tune_result['ok']:
            return {'message': tune_result['message'], 'preflight': preflight, 'tune': tune_result}, False
        preflight = _handshake_preflight(interface, channel)

    job = HandshakeCaptureJob(
        interface=interface,
        channel=channel,
        bssid=getattr(request, 'bssid', ''),
        duration=getattr(request, 'duration', 60),
        engine=capture_engine
    )
    job_id = job_manager.execute_job(job, callbacks=[_notify_capture_finished])
    module.send_notification('PineRecon handshake capture started.', notifier.INFO)
    return {'job_id': job_id, 'output_file': job.file_name, 'preflight': preflight}


@module.handles_action('start_pineap_handshake')
def start_pineap_handshake(request: Request):
    if not _has_binary('pineap'):
        return 'PineAP command is not available on this Pineapple.', False

    bssid = _normalise_mac(getattr(request, 'bssid', ''))
    channel = str(getattr(request, 'channel', '') or '').strip()
    if len(bssid) != 12:
        return 'A valid target BSSID is required.', False
    if not channel:
        return 'A target channel is required.', False

    result = _run_command(['pineap', 'handshake_capture_start', _format_mac(bssid), channel], timeout=12)
    if not result['ok']:
        return {
            'message': 'PineAP handshake capture did not start cleanly.',
            'stdout': result['stdout'],
            'stderr': result['stderr'],
            'return_code': result['return_code'],
        }, False

    module.send_notification('Pine DAP native PineAP handshake capture started.', notifier.INFO)
    return {
        'started': True,
        'method': 'pineap',
        'bssid': _format_mac(bssid),
        'channel': channel,
        'stdout': result['stdout'],
        'stderr': result['stderr'],
    }


@module.handles_action('stop_pineap_handshake')
def stop_pineap_handshake(request: Request):
    if not _has_binary('pineap'):
        return 'PineAP command is not available on this Pineapple.', False
    result = _run_command(['pineap', 'handshake_capture_stop'], timeout=8)
    module.send_notification('Pine DAP native PineAP handshake capture stopped.', notifier.WARN)
    return {'stopped': result['ok'], 'stdout': result['stdout'], 'stderr': result['stderr']}


@module.handles_action('stop_handshake_capture')
def stop_handshake_capture(request: Request):
    job_id = getattr(request, 'job_id', '')
    if job_id:
        job_manager.stop_job(job_id=job_id)
    else:
        subprocess.call(['killall', '-9', 'hcxdumptool'])
        subprocess.call(['killall', '-9', 'airodump-ng'])
    module.send_notification('PineRecon handshake capture stopped.', notifier.WARN)
    return True


@module.handles_action('handshake_status')
def handshake_status(request: Request):
    job_id = getattr(request, 'job_id', '')
    job = _running_job(job_id)
    if not job:
        return {'running': False, 'log_tail': _read_tail('/tmp/PineRecon-handshake.log')}

    analysis = _analyze_capture_file(pathlib.Path(job.output_path))
    analysis.update({
        'running': job.proc is not None and job.proc.poll() is None,
        'output_file': job.file_name,
        'target_bssid': _format_mac(job.bssid) if job.bssid else '',
        'capture_engine': job.engine,
        'log_tail': _read_tail(job.log_path),
    })
    return analysis


@module.handles_action('list_captures')
def list_captures(request: Request):
    return [_analyze_capture_file(path) for path in _capture_files()]


@module.handles_action('analyze_capture')
def analyze_capture(request: Request):
    path = _capture_file_by_name(getattr(request, 'file', ''))
    if path:
        return _analyze_capture_file(path)
    return 'Capture file not found.', False


@module.handles_action('download_capture')
def download_capture(request: Request):
    path = _capture_file_by_name(getattr(request, 'file', ''))
    if not path:
        return 'Capture file not found.', False

    with open(str(path), 'rb') as capture_file:
        content = base64.b64encode(capture_file.read()).decode('ascii')

    return {
        'file': path.name,
        'content_b64': content,
        'mime': 'application/vnd.tcpdump.pcap',
        'size': path.stat().st_size,
    }


@module.handles_action('delete_capture')
def delete_capture(request: Request):
    path = _capture_file_by_name(getattr(request, 'file', ''))
    if not path:
        return 'Capture file not found.', False

    path.unlink()
    return {'deleted': path.name}


@module.handles_action('get_logs')
def get_logs(request: Request):
    logs = {}
    for log_path in ['/tmp/PineRecon-handshake.log', '/tmp/PineRecon-hcxdumptool.log', '/tmp/PineRecon.log']:
        if os.path.exists(log_path):
            with open(log_path, 'r', errors='replace') as f:
                logs[pathlib.Path(log_path).name] = f.read()
    if not logs:
        logs['PineRecon.log'] = 'No PineRecon runtime logs found yet.'
    return logs


if __name__ == '__main__':
    module.start()
