import subprocess

def display_ascii_art():
    art = '''
    __  ____  __    __________  ____  __    __ __ __________
   /  |/  / |/ /   /_  __/ __ \/ __ \/ /   / //_//  _/_  __/
  / /|_/ /|   /     / / / / / / / / / /   / ,<   / /  / /   
 / /  / //   |     / / / /_/ / /_/ / /___/ /| |_/ /  / /    
/_/  /_//_/|_|    /_/  \____/\____/_____/_/ |_/___/ /_/     
                                                            
    '''

    print(art)

# Call the function to display the ASCII art
display_ascii_art()


def check_blacklists():
    subprocess.call(['python', 'blacklist/blacklist.py'])

def dns_lookup():
    subprocess.call(['python', 'dns_lookup/dns_lookup.py'])

def check_smtp():
    subprocess.call(['python', 'smtp/smtp.py'])

def check_ssl():
    subprocess.call(['python', 'ssl/ssl_check.py'])

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Check Domains in Blacklists")
        print("2. DNS Lookup")
        print("3. Check for SMTP Open Relay")
        print("4. Check SSL Cert")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_blacklists()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            check_smtp()
        elif choice == "4":
            check_ssl()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
