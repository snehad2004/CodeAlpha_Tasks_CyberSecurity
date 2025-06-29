from scapy.all import sniff


def show_packet(packet):
    print("\n New Packet:")
    print(f" Source IP: {packet[0][1].src}")
    print(f" Destination IP: {packet[0][1].dst}")
    print(f" Protocol: {packet[0][1].proto}")
    print(f" Raw Payload: {bytes(packet[0][1].payload)}")

# Start sniffing
print(" Starting Packet Sniffer... Press Ctrl+C to stop.")
sniff(prn=show_packet, count=10)
