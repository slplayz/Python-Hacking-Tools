# network_scanner.py

import argparse
import socket
import threading

# Define the command-line arguments
parser = argparse.ArgumentParser(description='Network Scanner')
parser.add_argument('-t', '--target', help='Target IP address or range (e.g. 192.168.1.1 or 192.168.1.1-100)')
parser.add_argument('-p', '--ports', help='Port range to scan (e.g. 1-1000)')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

args = parser.parse_args()

# Define the target IP address or range
target_ip = args.target

# Define the port range to scan
port_range = args.ports

# Define the verbose mode
verbose = args.verbose

# Function to scan a single port
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        sock.close()
    except socket.error:
        print(f"Error scanning port {port} on {ip}")

# Function to scan a range of ports
def scan_ports(ip, port_range):
    start_port, end_port = port_range.split('-')
    start_port = int(start_port)
    end_port = int(end_port)
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)

# Main function
def main():
    if '-' in target_ip:
        start_ip, end_ip = target_ip.split('-')
        start_ip_parts = start_ip.split('.')
        end_ip_parts = end_ip.split('.')
        for i in range(int(start_ip_parts[3]), int(end_ip_parts[3]) + 1):
            ip = f"{start_ip_parts[0]}.{start_ip_parts[1]}.{start_ip_parts[2]}.{i}"
            scan_ports(ip, port_range)
    else:
        scan_ports(target_ip, port_range)

if __name__ == "__main__":
    main()