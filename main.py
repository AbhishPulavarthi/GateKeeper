import socket

print("=" * 45)
print("        GateKeeper")
print("     TCP Port Scanner v0.3")
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
print("Open Ports")
if len(open_ports) == 0:
    print("No open ports found.")
else:
    for port in open_ports:
        print(f"[OPEN] {port}")
print("-" * 30)
print("Scan Completed")
print(f"Open Ports Found : {len(open_ports)}")