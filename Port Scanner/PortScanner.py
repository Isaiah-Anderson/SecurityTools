#This Script takes an IP input and checks for common ports being Open. For the sake of security only use your local loopback address
import socket

# Common ports to check:
ports = {
    'FTP': 21,
    'SSH': 22,
    'TELNET': 23,
    'SMTP': 25,
    'DNS': 53,
    'HTTP': 80,
    'HTTPS': 443,
    'SMB': 445,
    'RDP': 3389,
}

#Select an Option from Menu
while True:
    print("\n==== MENU ====")
    print("1. Scan Ports")
    print("2. Close")
    choice = input("Select an option: ")

  #Enter IP Address
    if choice == '1':
        target = input("Enter target IP: ")

        print("========== SCANNING " + target + " ==========")

      #cycles through ports and checks if they're open
        for name, port in ports.items():
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target, port))

            if result == 0:
                print(f"Port {port} ({name}): OPEN")
            else:
                print(f"Port {port} ({name}): closed")

            sock.close()

        again = input("Would you like to scan again? (y/n): ")
        if again.lower() != 'y':
            print("Closing...")
            break

    elif choice == '2':
        print("Closing...")
        break

    else:
        print("Invalid option, try again.")
