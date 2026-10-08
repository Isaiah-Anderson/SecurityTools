import subprocess

# List of commands to run
commands = ['ipconfig /all', 'whoami']

while True:
    # Menu
    print("\n===== MENU =====")
    print("1. Enumerate")
    print("2. Close")
    choice = input("Select an option: ")

    if choice == '1':
        # Run each command
        for command in commands:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print("========== " + command.upper() + " ==========")
            print(result.stdout)

        # Ask to run again
        again = input("Would you like to run it again? (y/n): ")
        if again.lower() != 'y':
            print("Closing...")
            break

    elif choice == '2':
        print("Closing...")
        break

    else:
        print("Invalid option, try again.")
