import subprocess

#Command List ['']
commands = ['ipconfig /all', 'whoami', 'dir', 'ver', 'chkdsk']

while True:
    print("\n==== MENU ====")
    print("1. Enumerate")
    print("2. Close")
    choice = input("Select an option: ")

    if choice == '1':
        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print("========== " + command.upper() + " ==========")
            print(result.stdout)

        again = input("Would you like to enumerate the Windows OS again? (y/n): ")
        if again.lower() != 'y':
            print("Closing...")
            break

        elif choice == '2':
            print("Closing...")
            break

        else:
            print("Invalid option, try again.")