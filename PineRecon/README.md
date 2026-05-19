# PineRecon

<p align="center">
  <img src="/readme_assets/pinerecon-logo.png" alt="PineRecon logo" width="320">
</p>

<p align="center">
  <img alt="WiFi Pineapple MK7" src="https://img.shields.io/badge/WiFi%20Pineapple-MK7-62f7d4?style=for-the-badge">
  <img alt="Angular" src="https://img.shields.io/badge/Angular-Module-dd0031?style=for-the-badge&logo=angular">
  <img alt="Python" src="https://img.shields.io/badge/Python-Backend-3776ab?style=for-the-badge&logo=python&logoColor=white">
  <img alt="Package" src="https://img.shields.io/badge/Package-tar.gz-444444?style=for-the-badge">
  <img alt="Theme" src="https://img.shields.io/badge/Themes-Dark%20%7C%20Red%20%7C%20Cobalt%20%7C%20Light-111111?style=for-the-badge">
</p>

PineRecon is a WiFi Pineapple Mark VII module that wraps the built-in Pineapple recon workflow in a radar-style UI with AP/client analysis, OUI enrichment, channel/security stats, MFP/PMF visibility, and WPA handshake capture validation. It keeps the Pineapple recon workflow familiar while adding focused capture status for PMKID and EAPOL material.

<table>
  <tr>
    <td align="center" width="50%">
      <img src="/readme_assets/pr-theme-red.png" alt="PineRecon radar dashboard" width="100%">
      <br><strong>Radar Dashboard</strong>
    </td>
    <td align="center" width="50%">
      <img src="/readme_assets/clients-tab.png" alt="PineRecon client intelligence tab" width="100%">
      <br><strong>Client Intelligence</strong>
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="/readme_assets/handshake-tab.png" alt="PineRecon handshake status" width="100%">
      <br><strong>Handshake Status</strong>
    </td>
    <td align="center" width="50%">
      <img src="/readme_assets/handshake.png" alt="PineRecon Handshake Capture" width="100%">
      <br><strong>Handshake Proof</strong></br>
      </td>
  </tr>
</table>

*Capturing handshakes on any devices other than your own is illegal the author of this module will not be held responsible for any misuse of this tool.*
*Any testing of this tool was done in a controlled environment on my own devices[!]*

## Features

- Futuristic radar view for nearby access points.
- Built-in WiFi Pineapple recon API integration for scan start, stop, scan status, and latest scan parsing.
- Top 15 AP pagination for cleaner results.
- Dedicated clients tab with associated AP, BSSID, channel, security, PMF/MFP state, frame counts, and targeted handshake action.
- Channel distribution and security distribution analysis.
- OUI lookup using the Pineapple OUI database at `/etc/pineapple/ouis`.
- MFP/PMF detection from Pineapple recon fields when available.
- Handshake capture support through `hcxdumptool`, with `airodump-ng` fallback when available.
- Active deauthentication support through `aireplay-ng` during PineRecon handshake capture when a target BSSID is selected.
- Original PineAP handshake capture support through the Pineapple `pineap handshake_capture_start` command.
- Capture preflight checks for interface state, active capture jobs, monitor mode, selected AP channel, and deauth capability.
- Automatic capture-interface channel retuning before handshake capture starts.
- EAPOL key message inspection for M1, M2, M3, and M4 capture status.
- PMKID and EAPOL hash validation through `hcxpcapngtool` when installed.
- Usable WPA material indicators for PMKID, EAPOL hashes, and fallback EAPOL message pairs.
- Raw capture file download from the UI for successful, partial, and unsuccessful capture attempts.
- Capture log download from the UI.
- Pineapple UI notifications for scan start, scan stop, dependency install completion, and handshake results.
- Theme selector with Pine Night, Red Zone, Cobalt Grid, and Light Ops.

## Project Layout

```text
PineRecon/
  build.sh
  package.json
  projects/PineRecon/src/
    module.py
    module.json
    module.svg
    assets/
      pinerecon-logo.png
    lib/
      components/
        PineRecon.component.ts
        PineRecon.component.html
        PineRecon.component.css
```

## Runtime Dependencies

PineRecon can check and install capture dependencies from the module UI.

Required for handshake capture and active deauthentication:

```text
hcxdumptool
aircrack-ng
```

The `aircrack-ng` package provides the fallback capture and deauthentication tooling PineRecon checks for:

```text
airodump-ng
aireplay-ng
```

Optional but recommended for capture validation:

```text
hcxpcapngtool
```

When `hcxpcapngtool` is present, PineRecon validates stored captures by generating and inspecting Hashcat mode 22000 material:

```text
WPA*01 = PMKID
WPA*02 = EAPOL
```

If `hcxpcapngtool` is not installed, PineRecon falls back to internal EAPOL frame inspection and reports usable message-pair indicators when possible.

The backend checks both `opkg` package state and available binaries, so tools installed outside normal package metadata can still be detected.

OUI lookup source checked by the backend:

```text
/etc/pineapple/ouis
```

## Building

*The one command build will produce your side load module file*
*in the / directory of PineRecon for uploading to your pineapple*

```bash
./build.sh
```
Or

Install frontend dependencies once:

```bash
npm install
```

Build and package the module:

```bash
npm run build
```

The packaged module is written to:

```text
PineRecon-1.0.tar.gz
```

## Installing On WiFi Pineapple MK7

Upload the generated tarball through the WiFi Pineapple side load module manager, or 
build it and upload the dist folder to 
srp -r dist root@172.16.42.1:/pineapple/modules/

Package contents:

```text
PineRecon/PineRecon.umd.js
PineRecon/module.py
PineRecon/module.json
PineRecon/module.svg
PineRecon/assets/pinerecon-logo.png
```

## Backend Actions

The backend exposes Pineapple module actions from `module.py`:

| Action | Purpose |
| --- | --- |
| `status` | Returns internet state, interfaces, OUI status, dependency state, and socket path. |
| `check_dependencies` | Checks capture dependencies and active install jobs. |
| `manage_dependencies` | Starts the Pineapple `OpkgJob` installer when dependencies are missing. |
| `scan_notification` | Sends Pineapple UI notifications for recon scan start/stop events. |
| `lookup_oui` | Looks up a single MAC prefix. |
| `enrich_aps` | Enriches AP rows with OUI vendor names. |
| `handshake_preflight` | Checks capture engine, interface availability, monitor state, active jobs, target channel warnings, and whether active deauth support is available. |
| `start_handshake_capture` | Tunes the selected interface to the target channel, starts a timed handshake capture job, and launches `aireplay-ng` deauth when possible. |
| `stop_handshake_capture` | Stops the active capture job and its companion deauth process. |
| `start_pineap_handshake` | Starts Pine DAP using the original PineAP `handshake_capture_start` command. |
| `stop_pineap_handshake` | Stops Pine DAP native PineAP handshake capture. |
| `handshake_status` | Returns live capture output. |
| `list_captures` | Lists and analyzes stored capture files. |
| `analyze_capture` | Re-analyzes one capture file. |
| `download_capture` | Returns a stored `.pcapng`, `.pcap`, or `.cap` file for download. |
| `get_logs` | Returns downloadable module logs. |

## Handshake Capture Notes

Capture files are stored under:

```text
/root/.PineRecon/captures
```

PineRecon handshake capture uses `hcxdumptool` first and falls back to `airodump-ng` when available. When a target BSSID is selected and `aireplay-ng` is available, PineRecon also starts continuous deauthentication to trigger client reconnects:

```text
aireplay-ng --deauth 0 -a <target-bssid> <interface>
```

The companion deauth process is stopped when the capture job stops.

The analyzer scans capture bytes for EAPOL frames and reports counts for:

```text
M1, M2, M3, M4
```

When `hcxpcapngtool` is available, PineRecon also checks for validated Hashcat 22000 output:

```text
PMKID hashes
EAPOL hashes
total WPA hash lines
message pair metadata
```

Capture status is shown as:

```text
PMKID usable
EAPOL usable
complete
usable pair
partial
no EAPOL
```

PineRecon keeps the raw capture file available for download whether the validation result is successful, partial, or empty. The validation status is only a confidence indicator; the downloaded `.pcapng`, `.pcap`, or `.cap` can still be processed with external tooling such as `hcxpcapngtool`, Hashcat, or Aircrack-ng.

Before starting a PineRecon handshake capture, the backend attempts to tune the selected capture interface to the selected AP channel with `iw`. If tuning fails or the interface remains on the wrong channel, the capture is stopped before launch and the UI reports the error.

Pine DAP is available inside the Handshakes tab as an original PineAP handshake option. It calls the Pineapple `pineap` binary directly:

```text
pineap handshake_capture_start <bssid> <channel>
pineap handshake_capture_stop
```

## Development Notes

- Frontend framework: Angular.
- Backend language: Python 3.
- UI library: WiFi Pineapple Angular/Material module stack.
- Target hardware: Hak5 WiFi Pineapple Mark VII.
- Default module socket: `/tmp/modules/PineRecon.sock`.
- Default package name: `PineRecon-1.0.tar.gz`.

## Legal Use

Use PineRecon only on wireless networks and clients you own or are explicitly authorized to test. Handshake capture and client targeting features are intended for legitimate auditing, troubleshooting, and lab use.


## Credits
![hak5credits](https://hak5.org/cdn/shop/files/logo1_hak5_410x.png?v=1613786565)

<p align="left">
  Credits to <a href="https://github.com/hak5">@HAK5</a> & their team for publishing an amazing tool to work with.
</p>
