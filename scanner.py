import networkx as nx
import matplotlib.pyplot as plt
from pythonping import ping
from scapy.all import srp, Ether, ARP
import socket

def resolve_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return ip

def scan_network_topology(ip_range):
    G = nx.Graph()

    # Scan IP range and add devices to the graph
    for i in range(1, 256):
        ip = ip_range + '.' + str(i)

        # Check if device responds to ping
        response = ping(ip, count=1)
        if response.success():
            G.add_node(ip)
        else:
            # Send ARP request to get MAC address
            try:
                ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=1, verbose=False)
                for _, rcv in ans:
                    mac = rcv[Ether].src
                    G.add_node(mac)
            except Exception as e:
                print(f"Error while sending ARP request to {ip}: {e}")

    # Resolve DNS for each IP address
    for node in G.nodes():
        G.nodes[node]['label'] = resolve_dns(node)

    # Draw the network diagram
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8)
    nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=8)
    plt.show()

if __name__ == '__main__':
    ip_range = '192.168.0'  # Change this to your desired IP range
    scan_network_topology(ip_range)
