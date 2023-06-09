from scapy.all import *
load_layer('tls')

import time
import matplotlib.pyplot as plt
import plotly.tools as tls

import cryptography

# Set network interface to capture packets (e.g., "eth0" or "wlan0")
interface = "wlan1"

# Set the BPF filter to capture specific traffic (e.g., "port 80" or "port 443" or "port 5060")
bpf_filter = "port 80 or port 443 or port 5060"

# Initialize packet counts dictionary
packet_counts = {}

# Start packet capture
start_time = time.time()
while True:
    # Capture packets for 0.1 seconds
    packets = sniff(iface=interface, filter=bpf_filter, timeout=0.1)

    # Process each captured packet
    for packet in packets:
        if packet.haslayer(TCP):
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport

            # Check if packet contains video stream traffic
            if dst_port == 80 or dst_port == 443:
                if packet.haslayer(Raw):
                    payload = packet[Raw].load
                    if payload == "RTSP":
                        packet_counts.setdefault((src_ip, dst_ip), {'http_video': 0, 'rtsp_video': 0, 'encrypted_traffic': 0, 'sip_traffic': 0})['rtsp_video'] += 1
                    elif payload == "HTTP":
                        packet_counts.setdefault((src_ip, dst_ip), {'http_video': 0, 'rtsp_video': 0, 'encrypted_traffic': 0, 'sip_traffic': 0})['http_video'] += 1

            # Check if packet contains encrypted traffic
            if packet.haslayer(TLS):
                packet_counts.setdefault((src_ip, dst_ip), {'http_video': 0, 'rtsp_video': 0, 'encrypted_traffic': 0, 'sip_traffic': 0})['encrypted_traffic'] += 1

            # Check if packet contains SIP traffic
            if dst_port == 5060 or src_port == 5060:
                if packet.haslayer(Raw):
                    payload = packet[Raw].load
                    if "SIP" in payload:
                        packet_counts.setdefault((src_ip, dst_ip), {'http_video': 0, 'rtsp_video': 0, 'encrypted_traffic': 0, 'sip_traffic': 0})['sip_traffic'] += 1

    # Plot packet counts in real-time for each IP address pair
    plt.clf()
    for (src_ip, dst_ip), counts in packet_counts.items():
        timestamps = list(counts.keys())
        values = list(counts.values())
        for i in range(len(timestamps)):
            plt.plot([timestamps[i]], [values[i]], 'o-', label=f"{src_ip} -> {dst_ip} - {timestamps[i]}")
    plt.xlabel('Category')
    plt.ylabel('Packet Count')
    plt.title('Packet Counts by IP Address Pair')
    plt.legend()
    plt.grid(True)
    plt.pause(0.01)
