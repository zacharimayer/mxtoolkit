import ssl
import socket

def display_ascii_art():
    art = '''
  ____  ____   _        ____  _____  ____  _____ 
 / ___|/ ___| | |      / ___|| ____||  _ \|_   _|
 \___ \\___ \ | |     | |    |  _|  | |_) | | |  
  ___) |___) || |___  | |___ | |___ |  _ <  | |  
 |____/|____/ |_____|  \____||_____||_| \_\ |_|  
                                                                       
                                                                              
    '''

    print(art)

# Call the function to display the ASCII art
display_ascii_art()

# Set the port number
port = 443

# Set the SSL context options
context = ssl.create_default_context()
context.check_hostname = True
context.verify_mode = ssl.CERT_REQUIRED

# Read in the list of domains from a file
with open('domains.txt', 'r') as f:
    domains = f.read().splitlines()

print("*** SSL CHECK TOOL ***")

# Open a file to write the output to
with open('ssl_results.txt', 'w') as f:
    # Loop through each domain and check if it has a valid SSL certificate
    for domain in domains:
        try:
            # Create a socket object and connect to the domain
            sock = socket.create_connection((domain, port))

            # Wrap the socket with the SSL context
            with context.wrap_socket(sock, server_hostname=domain) as ssl_sock:
                # Get the SSL certificate information
                cert = ssl_sock.getpeercert()

                # Check if the certificate is valid
                if cert and 'subjectAltName' in cert:
                    print(f"Valid SSL certificate found for {domain}")
                    f.write(f"Valid SSL certificate found for {domain}\n")
                    if cert['OCSP'] and cert['issuer']:
                        print(f"Encryption enabled for {domain}")
                        f.write(f"Encryption enabled for {domain}\n")
                        print(f"Encryption protocol: {ssl_sock.version()}")
                        f.write(f"Encryption protocol: {ssl_sock.version()}\n")
                        print(f"SSL certificate subject: {cert['subject']}")
                        f.write(f"SSL certificate subject: {cert['subject']}\n")
                        print(f"SSL certificate issuer: {cert['issuer']}")
                        f.write(f"SSL certificate issuer: {cert['issuer']}\n")
                        print(f"SSL certificate expiry: {cert['notAfter']}")
                        f.write(f"SSL certificate expiry: {cert['notAfter']}\n")
                    else:
                        print(f"Encryption not enabled for {domain}")
                        f.write(f"Encryption not enabled for {domain}\n")
                else:
                    print(f"No valid SSL certificate found for {domain}")
                    f.write(f"No valid SSL certificate found for {domain}\n")
        except Exception as e:
            print(f"Error checking {domain}: {e}")
            f.write(f"Error checking {domain}: {e}\n")
