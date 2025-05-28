#!/usr/bin/env python3
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

def scan_port(target, port, verbose=False):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                print(f"[+] Port {port} is OPEN | Service: {service}")
                return (port, service)
            elif verbose:
                print(f"[-] Port {port} is closed")
    except Exception as e:
        if verbose:
            print(f"[!] Error on port {port}: {e}")
    return None

def scan_ports(target, ports, max_threads, verbose):
    open_ports = []
    print(f"\n[*] Scanning {target} with {max_threads} threads...\n")

    with ThreadPoolExecutor(max_threads) as executor:
        futures = [executor.submit(scan_port, target, port, verbose) for port in ports]
        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)

    return sorted(open_ports)

def parse_ports(port_range):
    if '-' in port_range:
        start, end = map(int, port_range.split('-'))
        return range(start, end + 1)
    else:
        return [int(port_range)]

def main():
    parser = argparse.ArgumentParser(description="Simple Python Port Scanner")
    parser.add_argument("target", help="Target IP address or domain")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g. 1-65535)")
    parser.add_argument("-t", "--threads", type=int, default=100, help="Number of threads")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()
    ports = parse_ports(args.ports)

    print(f"\n[!] Starting scan on {args.target}...\n")
    start_time = datetime.now()

    open_ports = scan_ports(args.target, ports, args.threads, args.verbose)

    end_time = datetime.now()
    print(f"\n[✓] Scan completed in {end_time - start_time}")
    print(f"[+] Open Ports ({len(open_ports)}):")
    for port, service in open_ports:
        print(f"    - Port {port}: {service}")

if __name__ == "__main__":
    main()
