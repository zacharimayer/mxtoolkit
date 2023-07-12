import dns.resolver

# read the list of domains from a text file
with open('domains.txt') as f:
    domains = [line.strip() for line in f]

blacklists = [
    'access.redhawk.org',
]

results = {}

with open("blacklists_results.txt", "w") as f:
    for domain in domains:
        print(f"\nChecking blacklists for domain: {domain}")
        f.write(f"\nChecking blacklists for domain: {domain}\n")
        f.write("=" * 40 + "\n")

        found_in_blacklists = []
        for bl in blacklists:
            query = '.'.join(reversed(str(domain).split("."))) + "." + bl
            try:
                answers = dns.resolver.resolve(query, 'A')
                print(f"{domain} is listed on {bl}.")
                f.write(f"{domain} is listed on {bl}.\n")
                found_in_blacklists.append(bl)
                for rdata in answers:
                    print(f"\t{bl} returned: {rdata.address}")
                    f.write(f"\t{bl} returned: {rdata.address}\n")
            except dns.resolver.NXDOMAIN:
                print(f"{domain} is not listed on {bl}.")
            except dns.resolver.NoAnswer:
                print(f"{bl} gave no answer.")
            except dns.resolver.Timeout:
                print(f"{bl} timed out.")
            except dns.resolver.NoNameservers:
                print(f"{bl} has no name servers.")

        if found_in_blacklists:
            results[domain] = found_in_blacklists
        else:
            results[domain] = ['Not listed in any blacklists']

    print("\nBlacklist Summary")
    f.write("\nBlacklist Summary\n")
    for domain, blacklists in results.items():
        if blacklists == ['Not listed in any blacklists']:
            print(f"{domain} was not found in any blacklists.")
            f.write(f"{domain} was not found in any blacklists.\n")
        else:
            print(f"{domain} was found in {len(blacklists)} blacklists.")
            f.write(f"{domain} was found in {len(blacklists)} blacklists.\n")
            print(f"\tBlacklists: {', '.join(blacklists)}")
            f.write(f"\tBlacklists: {', '.join(blacklists)}\n")
