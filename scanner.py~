import networkx as nx
import matplotlib.pyplot as plt
from pythonping import ping

def scan_network_topology(ip_range):
    G = nx.Graph()

    # Scan IP range and add devices to the graph
    for i in range(1, 256):
        ip = ip_range + '.' + str(i)
        response = ping(ip, count=1)
        if response.success():
            G.add_node(ip)

    # Draw the network diagram
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8)
    plt.show()

if __name__ == '__main__':
    ip_range = '192.168.0'  # Change this to your desired IP range
    scan_network_topology(ip_range)
