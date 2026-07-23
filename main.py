import socket
services = {
    20: "FTP (Data)",21: "FTP",22: "SSH",23: "Telnet",25: "SMTP",53: "DNS",80: "HTTP",110: "POP3",143: "IMAP",443: "HTTPS",445: "SMB",
    3306: "MySQL",3389: "RDP",5432: "PostgreSQL",8080: "HTTP-Alt"
}

print("=" * 45)
print("        GateKeeper")
print("     TCP Port Scanner v0.5")
print("=" * 45)

target = input("\nEnter Target (IP or Domain): ").strip()
start_port=int(input("Give start port number : "))
end_port=int(input("Give end port number   : "))
target_ip = socket.gethostbyname(target)
print(f"Target IP: {target_ip}")
print("\nScan Result")
print("-" * 30)
open_ports=[]
banner_List=[]
for port in range(start_port, end_port+1) :
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)
    result = scanner.connect_ex((target_ip, port))

    if result == 0:
        open_ports.append(port)
        try:
            banner=scanner.recv(1024).decode()
            banner_List.append(banner)
        except Exception:
            banner_List.append('Unknown')
        
    scanner.close()
if len(open_ports) == 0:
    print("No open ports found.")
else:
    print(f"\n{'Port':<8}{'Status':<10}{'Service':<15}{'Banner'}")
    print("-" * 70)

    for i in range (len(open_ports)):
        port=open_ports[i]
        banner_print=banner_List[i]
        service_name = services.get(port, "Unknown")
        print(f"{port:<8}{'OPEN':<10}{service_name:<15}{banner_print}")

print("-" * 70)
print("Scan Completed")
print(f"Open Ports Found : {len(open_ports)}")