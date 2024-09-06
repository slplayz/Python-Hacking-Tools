import dns.resolver

def dns_lookup(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for answer in answers:
            print(f"IP address: {answer}")
    except dns.resolver.NoAnswer:
        print(f"No IP address found for {domain}")

domain = input("Enter the domain: ")
dns_lookup(domain)