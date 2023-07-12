import dns.resolver

def display_ascii_art():
    art = '''
  _      _               _     _  _       _           _                  _    
 | |__  | |  __ _   ___ | | __| |(_) ___ | |_    ___ | |__    ___   ___ | | __
 | '_ \ | | / _` | / __|| |/ /| || |/ __|| __|  / __|| '_ \  / _ \ / __|| |/ /
 | |_) || || (_| || (__ |   < | || |\__ \| |_  | (__ | | | ||  __/| (__ |   < 
 |_.__/ |_| \__,_| \___||_|\_\|_||_||___/ \__|  \___||_| |_| \___| \___||_|\_\
                                                                              
    '''

    print(art)

# Call the function to display the ASCII art
display_ascii_art()


# read the list of domains from a text file
with open('domains.txt') as f:
    domains = [line.strip() for line in f]

blacklists = [
    'access.redhawk.org',
    'all.s5h.net',
    'b.barracudacentral.org',
    'bl.blocklist.de',
    'bl.drmx.org',
    'bl.konstant.no',
    'bl.nosolicitado.org',
    'bl.spamcannibal.org',
    'bl.spamcop.net',
    'bl.spameatingmonkey.net',
    'bl.spamstinks.com',
    'blackholes.five-ten-sg.com',
    'blacklist.sci.kun.nl',
    'blacklist.woody.ch',
    'bogons.cymru.com',
    'bsb.empty.us',
    'cbl.abuseat.org',
    'cdl.anti-spam.org.cn',
    'combined.abuse.ch',
    'db.wpbl.info',
    'dnsbl-1.uceprotect.net',
    'dnsbl-2.uceprotect.net',
    'dnsbl-3.uceprotect.net',
    'dnsbl-4.uceprotect.net',
    'dnsbl.anticaptcha.net',
    'dnsbl.inps.de',
    'dnsbl.justspam.org',
    'dnsbl.kempt.net',
    'dnsbl.sorbs.net',
    'dnsbl.spfbl.net',
    'dnsbl.zapbl.net',
    'dnsrbl.org',
    'dnswl.inps.de',
    'drone.abuse.ch',
    'dronebl.org',
    'duinv.aupads.org',
    'dul.dnsbl.sorbs.net',
    'dul.ru',
    'dyna.spamrats.com',
    'dynip.rothen.com',
    'exitnodes.tor.dnsbl.sectoor.de',
    'http.dnsbl.sorbs.net',
    'ips.backscatterer.org',
    'ix.dnsbl.manitu.net',
    'korea.services.net',
    'l2.apews.org',
    'mail-abuse.blacklist.jippg.org',
    'misc.dnsbl.sorbs.net',
    'multi.surbl.org',
    'netblock.pedantic.org',
    'new.spam.dnsbl.sorbs.net',
    'no-more-funn.moensted.dk',
    'noptr.spamrats.com',
    'ohps.dnsbl.net.au',
    'omrs.dnsbl.net.au',
    'orvedb.aupads.org',
    'osrs.dnsbl.net.au',
    'owfs.dnsbl.net.au',
    'pbl.spamhaus.org',
    'phishing.rbl.msrbl.net',
    'probes.dnsbl.net.au',
    'proxy.bl.gweep.ca',
    'proxy.block.transip.nl',
    'psbl.surriel.com',
    'rbl.interserver.net',
    'rbl.megarbl.net',
    'rbl.rbldns.ru',
    'rbl.schulte.org',
    'rbl.snark.net',
    'rdts.dnsbl.net.au',
    'relays.bl.gweep.ca',
    'relays.bl.kundenserver.de',
    'relays.nether.net',
    'residential.block.transip.nl',
    'ricn.dnsbl.net.au',
    'rmst.dnsbl.net.au',
    'sbl.spamhaus.org',
    'smtp.dnsbl.sorbs.net',
    'zen.spamhaus.org',
    'zrd.zen.spamhaus.org',
    'spamrbl.imp.ch',
    'bl.swissantispam.ch',
    'inbound-smtp.threatstop.com',
    'dnsbl-1.uceprotect.net',
    'dnsbl-2.uceprotect.net',
    'dnsbl-3.uceprotect.net',
    'dnsbl-4.uceprotect.net',
    'dnsbl-5.uceprotect.net'
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
