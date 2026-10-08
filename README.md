# SecurityTools
Toolkit for Basic Security Tasks

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

### Disclaimer
For educational use and authorized testing only. Only run this on
systems you own or have permission to assess.
