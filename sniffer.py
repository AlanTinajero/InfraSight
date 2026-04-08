from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        return {
            "src": packet["IP"].src,
            "dst": packet["IP"].dst,
            "proto": packet["IP"].proto
        }

def sniff_traffic(limit=50):
    packets = sniff(count=limit, iface="en1")

    data = []

    for p in packets:
        info = packet_callback(p)
        if info:
            data.append(info)

    return data
