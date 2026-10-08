# SecurityTools
Toolkit for basic security tasks.

## Windows Enumeration Tool
A Python script that runs common Windows commands and prints the results
in labeled sections. Useful for quickly gathering basic information about
a Windows host.

### Commands Run
| Command        | What It Shows                                   |
|----------------|-------------------------------------------------|
| `ipconfig /all`| Network adapters, IP addresses, DNS, MAC address |
| `whoami`       | The current logged-in user                      |
| `dir`          | Files in the current directory                  |
| `ver`          | Windows version                                 |
| `chkdsk`       | Disk status (read-only check)                   |

### Requirements
- Windows
- Python 3

### Usage
python "Windows Enumeration Tool.py"

Menu options:
1. **Enumerate** – runs all commands and prints the output
2. **Close** – exits the program

After enumerating, you'll be asked whether to run it again.

### Planned Features
- Save output to a timestamped report file
- Add more commands (`netstat -ano`, `systeminfo`, `tasklist`)
- Show errors when a command fails

### Disclaimer
For educational use and authorized testing only. Only run this on
systems you own or have permission to assess.
