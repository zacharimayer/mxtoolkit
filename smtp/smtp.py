import smtplib
import socket

def display_ascii_art():
    art = '''
  ____   __  __  _____  ____    _____  ___    ___   _     
 / ___| |  \/  ||_   _||  _ \  |_   _|/ _ \  / _ \ | |    
 \___ \ | |\/| |  | |  | |_) |   | | | | | || | | || |    
  ___) || |  | |  | |  |  __/    | | | |_| || |_| || |___ 
 |____/ |_|  |_|  |_|  |_|       |_|  \___/  \___/ |_____|
                                                          
                                                               
                                                                              
    '''

    print(art)

# Call the function to display the ASCII art
display_ascii_art()


socket.setdefaulttimeout(15)

with open('domains.txt') as file:
    targets = file.read().splitlines()

with open('smtp_results.txt', 'w') as output_file:
    output_file.write(f"Checking SMTP relay for {len(targets)} targets...\n\n")

    for i, target in enumerate(targets, start=1):
        print("*** SMTP TEST TOOL ***")
        print(f"Checking {target} ({i}/{len(targets)})...")
        try:
            server = smtplib.SMTP(target)
            response = server.docmd('EHLO example.com')
            if '250-' in response[1] and '250-STARTTLS' in response[1]:
                output_file.write(f"{target} does not allow open relay\n")
                print(f"{target} does not allow open relay")
            else:
                output_file.write(f"{target} allows open relay\n")
                print(f"{target} allows open relay")
            server.quit()
        except (socket.timeout, ConnectionRefusedError):
            output_file.write(f"{target} is not reachable\n")
            print(f"{target} is not reachable")
        except:
            output_file.write(f"An error occurred while checking {target}\n")
            print(f"An error occurred while checking {target}")

print("Done! Check smtp_results.txt for the results.")
