from scapy.all import sniff
from scapy.layers.inet import IP, TCP
from datetime import datetime

print("======================================")
print(" SIMPLE NETWORK INTRUSION DETECTION ")
print("======================================")

# Suspicious ports commonly targeted by attackers
suspicious_ports = [21, 22, 23, 445, 3389]

# Log file
log_file = "intrusion_log.txt"


def detect_intrusion(packet):

    # Check if packet has TCP and IP layers
    if packet.haslayer(TCP) and packet.haslayer(IP):

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        dst_port = packet[TCP].dport

        # Check suspicious ports
        if dst_port in suspicious_ports:

            alert = f"[ALERT] {datetime.now()} - Suspicious access detected!"

            print(alert)
            print(f"Source IP: {src_ip}")
            print(f"Destination IP: {dst_ip}")
            print(f"Target Port: {dst_port}")
            print("----------------------------------")

            with open(log_file, "a") as f:
                f.write(alert + "\n")
                f.write(f"Source IP: {src_ip}\n")
                f.write(f"Destination IP: {dst_ip}\n")
                f.write(f"Target Port: {dst_port}\n\n")


print("Monitoring Network Traffic...\n")

# Start packet sniffing
sniff(prn=detect_intrusion, store=False)