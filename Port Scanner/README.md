## Port Scanner
A Python script that checks a target IP for common open TCP ports.
Useful for quickly seeing which services a host is exposing.

### Ports Checked
| Port | Service | Security Note |
|------|---------|---------------|
| 21   | FTP     | File Transfer Protocol
| 22   | SSH     | Secure Shell
| 23   | Telnet  | Unencrypted remote access
| 25   | SMTP    | Simple Mail Transfer Protocol
| 53   | DNS     | Domain Name System
| 80   | HTTP    | Unencrypted web traffic 
| 443  | HTTPS   | Hypertest Transfer Protocol Secure
| 445  | SMB     | Server Message Block
| 3389 | RDP     | Remote Desktop Protocol

### Requirements
- Python 3 (no extra libraries; uses the built-in `socket` module)
- Works on Windows, Linux, and macOS


Menu options:
1. **Scan Ports** – asks for a target IP, then checks each port
2. **Close** – exits the program

After scanning, you'll be asked whether to scan again.


### How It Works
For each port, the script attempts a TCP connection with a 1-second
timeout. If the connection succeeds, the port is reported as OPEN.
Closed and filtered ports are both reported as closed.

### Adding More Ports
Add a line to the `ports` dictionary in the script:

    ports = {
        'MYSQL': 3306,
    }
