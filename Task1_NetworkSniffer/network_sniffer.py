from scapy.all import *
from datetime import datetime

print("="*55)
print("     NETWORK SNIFFER — M. Behlool Abbas")
print("     CodeAlpha Cyber Security Internship")
print("="*55)
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("Listening for packets... Press CTRL+C to stop\n")

packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    print(f"{'='*50}")
    print(f"Packet #{packet_count}")
    print(f"Time: {datetime.now().strftime('%H:%M:%S')}")

    if packet.haslayer(IP):
        print(f"Source IP:      {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol:       {packet[IP].proto}")
        print(f"TTL:            {packet[IP].ttl}")

    if packet.haslayer(TCP):
        print(f"Layer:          TCP")
        print(f"Source Port:    {packet[TCP].sport}")
        print(f"Dest Port:      {packet[TCP].dport}")
        print(f"Flags:          {packet[TCP].flags}")

    elif packet.haslayer(UDP):
        print(f"Layer:          UDP")
        print(f"Source Port:    {packet[UDP].sport}")
        print(f"Dest Port:      {packet[UDP].dport}")

    if packet.haslayer(Raw):
        payload = packet[Raw].load
        try:
            decoded = payload.decode('utf-8', errors='ignore')
            if 'HTTP' in decoded or 'GET' in decoded or 'POST' in decoded:
                print(f"HTTP Data:      {decoded[:100]}")
        except:
            pass

    print()

try:
    sniff(prn=analyze_packet, store=0, count=20)
    print(f"\nTotal Packets Captured: {packet_count}")
except KeyboardInterrupt:
    print(f"\nStopped! Total Packets: {packet_count}")
except Exception as e:
    print(f"Error: {e}")
