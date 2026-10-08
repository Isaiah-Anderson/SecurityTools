## Windows Log Parser
A Python script that pulls recent security events from the Windows
Security log and prints them in labeled sections. Useful for quickly
reviewing login activity and spotting suspicious events on a Windows host.

### Events Checked
| Event ID | Event             | Why It Matters                              |
|----------|-------------------|---------------------------------------------|
| 4625     | Failed login      | Many in a row can indicate a brute-force attempt |
| 4624     | Successful login  | Shows who signed in and when                |

Shows the 10 most recent events for each, newest first.

### Requirements
- Windows
- Python 3
- **Must be run as Administrator** (the Security log is protected)

### Usage
1. Open Command Prompt or PowerShell **as Administrator**
2. Go to the script's folder and run:

   python log_parser.py

Menu options:
1. **Parse Logs** – pulls each event type and prints the results
2. **Close** – exits the program

After parsing, you'll be asked whether to run it again.

### Adding More Events
Add a line to the `events` dictionary in the script:

    events = {
        'FAILED LOGINS': 4625,
        'SUCCESSFUL LOGINS': 4624,
        'LOG CLEARED': 1102,
    }

### Troubleshooting
- **"Access is denied"** – the terminal isn't running as Administrator.
- **No results** – there may be no matching events, or login auditing
  may be disabled on the machine.

### Planned Features
- Add more Event IDs (4672, 4720, 4732, 1102)
- Count failed logins per username to flag brute-force attempts
- Filter successful logins by type (local vs. Remote Desktop)
- Save results to a timestamped report file

