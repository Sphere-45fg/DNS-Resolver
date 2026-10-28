import socket


def resolve_dns(hostname: str):
    try:
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except socket.gaierror:
        raise ValueError(f"Could not resolve hostname: {hostname}")


def main():
    print("DNS Resolver")
    domain = input("Enter a domain name (for example, example.com): ").strip()

    if not domain:
        print("Domain name cannot be empty.")
        return

    try:
        ip_address = resolve_dns(domain)
        print(f"{domain} resolves to {ip_address}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
