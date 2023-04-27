import dns.resolver

# read domain names from domains.txt
with open('domains.txt', 'r') as domain_file:
    domain_names = domain_file.readlines()

print("*** DNS LOOKUP TOOL***")

# open file for writing output
with open('dns_results.txt', 'w') as file:
    for domain in domain_names:
        domain = domain.strip() # remove newline character
        print(f"Performing DNS lookup for {domain}...")

        # A records
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            a_record = f"A record: {rdata.address}"
            print(a_record)
            file.write(a_record + "\n")

        # MX records
        answers = dns.resolver.resolve(domain, 'MX')
        for rdata in answers:
            mx_record = f"MX record: {rdata.exchange} preference {rdata.preference}"
            print(mx_record)
            file.write(mx_record + "\n")

        # CNAME records
        try:
            answers = dns.resolver.resolve(domain, 'CNAME')
            for rdata in answers:
                cname_record = f"CNAME record: {rdata.target}"
                print(cname_record)
                file.write(cname_record + "\n")
        except dns.resolver.NoAnswer:
            print("No CNAME record found")

        # NS records
        answers = dns.resolver.resolve(domain, 'NS')
        for rdata in answers:
            ns_record = f"NS record: {rdata.target}"
            print(ns_record)
            file.write(ns_record + "\n")

        file.write("\n") # add newline character between domains

print("DNS lookup complete. Output saved to dns_results.txt")
