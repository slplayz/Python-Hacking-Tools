# packet_sniffer.py

import scapy.all as scapy
import netifaces as ni
import argparse
import time

# Define a function to get the list of available network interfaces
def get_interfaces():
    interfaces = ni.interfaces()
    return interfaces

# Define a function to capture packets
def capture_packets(interface, count):
    print(f"Capturing {count} packets on interface {interface}...")
    packets = scapy.sniff(iface=interface, count=count)
    return packets

# Define a function to display packet information
def display_packets(packets):
    for packet in packets:
        print(packet.show())

# Define the main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Packet Sniffer")
    parser.add_argument("-i", "--interface", help="Network interface to capture packets on")
    parser.add_argument("-c", "--count", type=int, help="Number of packets to capture")
    args = parser.parse_args()

    # Get the list of available network interfaces
    interfaces = get_interfaces()
    print("Available interfaces:")
    for interface in interfaces:
        print(interface)

    # Capture packets
    packets = capture_packets(args.interface, args.count)

    # Display packet information
    display_packets(packets)

if __name__ == "__main__":
    main()