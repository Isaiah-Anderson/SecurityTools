import subprocess

# Events to look for: "Header name": Event ID
events = {
    'Failed Logins': 4625,
    'Successful Logins': 4624,
    'Admin Logins': 4672,
    'Accounts Created': 4720,
}

#Menu Items to automate logs parsing
while True:
    print("\n==== MENU ====")
    print("1. Parse Logs")
    print("2. Close")
    choice = input("Select an option: ")

#commands Windows will run in background
    if choice == '1':
        for name, event_id in events.items():
            command = f'wevtutil qe Security /q:"*[System[(EventID={event_id})]]" /c:10 /rd:true /f:text'
            result = subprocess.run(command, shell=True, capture_output=True, text=True)

            print("========== " + name + " ==========")
            print(result.stdout)
            print(result.stderr)

        again = input("Would you like to parse the logs again? (y/n): ")
        if again.lower() != 'y':
            print("Closing...")
            break

    elif choice == '2':
        print("Closing...")
        break

    else:
        print("Invalid option, try again.")
