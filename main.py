import socket

print("=" * 45)
print("        PORT SCANNER v0.2")
print("=" * 45)

target = input("\nEnter Target (IP or Domain): ").strip()
target_port = int(input("Enter Target Port         : "))

target_ip = socket.gethostbyname(target)

scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
scanner.settimeout(1)

result = scanner.connect_ex((target_ip, target_port))

print("\nScan Result")
print("-" * 30)

if result == 0:
    print(f"[OPEN]   Port {target_port}")
else:
    print(f"[CLOSED] Port {target_port}")

scanner.close()