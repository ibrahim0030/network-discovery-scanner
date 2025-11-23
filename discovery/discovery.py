import argparse
import json
import os
from datetime import datetime

import nmap


def parse_args():
    parser = argparse.ArgumentParser(
        description="Enkel network discovery-skanner med JSON-logging."
    )
    parser.add_argument(
        "--network",
        "-n",
        default="192.168.4.0/22",
        help="Nettverk å skanne (CIDR-format), f.eks. 192.168.4.0/22 eller 192.168.7.0/24",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Filnavn for å lagre resultater som JSON. "
             "Hvis ikke satt, lages et navn automatisk i data/-mappen.",
    )
    return parser.parse_args()


def discover_hosts(network: str):
    """
    Bruker nmap til å finne aktive enheter på nettverket (ping scan).
    Returnerer en liste med dicts: {ip, mac, vendor}.
    """
    print(f"[+] Starter network discovery på {network}")
    nm = nmap.PortScanner()
    # -sn = ping scan (ingen portskanning, kun hvilke hoster som er oppe)
    nm.scan(hosts=network, arguments="-sn")

    hosts = []

    for host in nm.all_hosts():
        state = nm[host].state()
        if state != "up":
            continue

        mac = None
        vendor = None

        if "addresses" in nm[host]:
            mac = nm[host]["addresses"].get("mac")

        if "vendor" in nm[host]:
            # vendor-dict: {"MAC": "Navn"}
            vendor_values = list(nm[host]["vendor"].values())
            vendor = vendor_values[0] if vendor_values else None

        hosts.append(
            {
                "ip": host,
                "mac": mac,
                "vendor": vendor,
                "state": state,
            }
        )

    return hosts


def save_to_json(hosts, filename: str):
    """
    Lagre funnene til en JSON-fil.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    data = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "host_count": len(hosts),
        "hosts": hosts,
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[+] Resultater lagret til {filename}")


def main():
    args = parse_args()

    hosts = discover_hosts(args.network)

    if not hosts:
        print("[!] Ingen aktive enheter funnet.")
    else:
        print(f"[+] Fant {len(hosts)} aktive enheter:\n")
        for h in hosts:
            print(
                f"  IP: {h['ip']}\t"
                f"MAC: {h['mac'] or 'ukjent'}\t"
                f"Vendor: {h['vendor'] or 'ukjent'}"
            )

    # Bestem filnavn
    if args.output:
        output_file = args.output
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join("data", f"network_discovery_{timestamp}.json")

    save_to_json(hosts, output_file)


if __name__ == "__main__":
    main()
