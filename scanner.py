import networkx as nx
import matplotlib.pyplot as plt
from pythonping import ping
from scapy.all import srp, Ether, ARP
import socket
import os

def resolve_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return ip

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

    # Scan IP range and add devices to the graph
    for i in range(1, 256):
        ip = ip_range + '.' + str(i)

        # Check if device responds to ping
        response = ping(ip, count=1)
        if response.success():
            G.add_node(ip)

            # Resolve DNS for the IP address
            G.nodes[ip]['label'] = resolve_dns(ip)

            # Update the network diagram
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8)
            nx.draw_networkx_labels(G, pos, labels=nx.get_node_attributes(G, 'label'), font_size=8)
            plt.show()
            plt.pause(0.001)

        else:
            # Send ARP request to get MAC address
            try:
                ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=1, verbose=False)
                for _, rcv in ans:
                    mac = rcv[Ether].src
                    G.add_node(mac)

                    # Update the network diagram
                    pos = nx.spring_layout(G)
                    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8)
                    plt.show()
                    plt.pause(0.001)
            except Exception as e:
                print(f"Error while sending ARP request to {ip}: {e}")

    # Drop root permission
    os.seteuid(os.getuid())

    # Final network diagram
    plt.ioff()  # Disable interactive mode
    plt.show()

if __name__ == '__main__':
    ip_range = '192.168.0'  # Change this to your desired IP range

    # Request root permission if not already running as root
    if os.geteuid() != 0:
        args = [sys.executable] + sys.argv
        os.execlp('sudo', 'sudo', *args)

    scan_network_topology(ip_range)
