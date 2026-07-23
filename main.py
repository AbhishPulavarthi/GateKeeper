import socket
services = {
    20: "FTP (Data)",21: "FTP",22: "SSH",23: "Telnet",25: "SMTP",53: "DNS",80: "HTTP",110: "POP3",143: "IMAP",443: "HTTPS",445: "SMB",
    3306: "MySQL",3389: "RDP",5432: "PostgreSQL",8080: "HTTP-Alt"
}

print("=" * 45)
print("        GateKeeper")
print("     TCP Port Scanner v0.4")
print("=" * 45)

target = input("\nEnter Target (IP or Domain): ").strip()
start_port=int(input("Give start port number : "))
end_port=int(input("Give end port number   : "))
target_ip = socket.gethostbyname(target)
print(f"Target IP: {target_ip}")
print("\nScan Result")
print("-" * 30)
open_ports=[]
for port in range(start_port, end_port+1) :
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)
    result = scanner.connect_ex((target_ip, port))

    if result == 0:
        open_ports.append(port)
    scanner.close()
if len(open_ports) == 0:
    print("No open ports found.")
else:
    print(f"\n{'Port':<8}{'Status':<10}{'Service'}")
    print("-" * 35)

    for port in open_ports:
        service_name = services.get(port, "Unknown")
        print(f"{port:<8}{'OPEN':<10}{service_name}")

print("-" * 35)
print("Scan Completed")
print(f"Open Ports Found : {len(open_ports)}")