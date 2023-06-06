import networkx as nx
import matplotlib.pyplot as plt
from pythonping import ping
from scapy.all import srp, Ether, ARP
import socket
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def resolve_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return ip

def check_device(ip, G):
    response = ping(ip, count=1)
    if response.success():
        G.add_node(ip)
        G.nodes[ip]['label'] = resolve_dns(ip)
        print(f"Device at {ip} is up.")
        return ip

    try:
        ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=1, verbose=False)
        for _, rcv in ans:
            mac = rcv[Ether].src
            G.add_node(mac)
            print(f"Device with MAC address {mac} discovered.")
            return mac
    except Exception as e:
        print(f"Error while sending ARP request to {ip}: {e}")

def scan_network_topology(ip_range):
    G = nx.Graph()
    plt.ion()  # Enable interactive mode

    # Draw initial empty network diagram
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8)
    plt.show()
    plt.pause(0.001)

    # Request root permission for network checks
    os.seteuid(0)
    print("Root permission obtained.")

    # Scan IP range and add devices to the graph
    print("Scanning network...")
    with ThreadPoolExecutor() as executor:
        check_partial = partial(check_device, G=G)
        futures = [executor.submit(check_partial, ip_range + '.' + str(i)) for i in range(1, 256)]

        # Update the network diagram as devices are confirmed
        for future in futures:
            device = future.result()
            if device is not None:
                pos = nx.spring_layout(G)
                nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8)
                nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=8)
                plt.show()
                plt.pause(0.001)

    # Drop root permission
    os.seteuid(os.getuid())
    print("Root permission dropped.")

    # Final network diagram
    plt.ioff()  # Disable interactive mode
    plt.show()

if __name__ == '__main__':
    ip_range = input("Enter the IP range to scan (e.g., 192.168.0): ")

    # Request root permission if not already running as root
    if os.geteuid() != 0:
        args = [sys.executable] + sys.argv
        os.execlp('sudo', 'sudo', *args)

    scan_network_topology(ip_range)
