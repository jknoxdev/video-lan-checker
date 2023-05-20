from scapy.all import *
import time
import matplotlib.pyplot as plt

# Set network interface to capture packets (e.g., "eth0" or "wlan0")
interface = "eth0"

# Set the BPF filter to capture specific traffic (e.g., "port 80" or "port 443" or "port 5060")
bpf_filter = "port 80 or port 443 or port 5060"

# Initialize packet counts
http_video_count = 0
rtsp_video_count = 0
encrypted_traffic_count = 0
sip_traffic_count = 0

# Initialize time and counts lists
timestamps = []
http_video_counts = []
rtsp_video_counts = []
encrypted_traffic_counts = []
sip_traffic_counts = []

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
                    switch = {
                        "RTSP": lambda: rtsp_video_count += 1,
                        "HTTP": lambda: http_video_count += 1
                    }
                    switch.get(payload, lambda: None)()

            # Check if packet contains encrypted traffic
            if packet.haslayer(TLS):
                encrypted_traffic_count += 1

            # Check if packet contains SIP traffic
            if dst_port == 5060 or src_port == 5060:
                if packet.haslayer(Raw):
                    payload = packet[Raw].load
                    if "SIP" in payload:
                        sip_traffic_count += 1

    # Append current counts and timestamp to lists
    elapsed_time = time.time() - start_time
    timestamps.append(elapsed_time)
    http_video_counts.append(http_video_count)
    rtsp_video_counts.append(rtsp_video_count)
    encrypted_traffic_counts.append(encrypted_traffic_count)
    sip_traffic_counts.append(sip_traffic_count)

    # Plot packet counts in real-time
    plt.clf()
    plt.plot(timestamps, http_video_counts, label='HTTP Video')
    plt.plot(timestamps, rtsp_video_counts, label='RTSP Video')
    plt.plot(timestamps, encrypted_traffic_counts, label='Encrypted Traffic')
    plt.plot(timestamps, sip_traffic_counts, label='SIP Traffic')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Packet Count')
    plt.title('Packet Counts')
    plt.legend()
    plt.grid(True)
    plt.pause(0.01)

