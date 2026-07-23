# GateKeeper v0.4 - TCP Port Scanner

GateKeeper is a Python-based TCP port scanner developed as part of my cybersecurity learning journey. It scans a specified range of TCP ports on a target host, identifies open ports, and displays the commonly associated network service for each open port using a built-in service mapping dictionary.

This project focuses on understanding core networking concepts such as IP addressing, TCP connections, ports, sockets, and service identification while applying them through hands-on development.

---

## Features

- Scan a user-defined range of TCP ports
- Accept both domain names and IP addresses as targets
- Automatically resolve domain names to IPv4 addresses
- Detect open TCP ports using Python sockets
- Identify common network services using a built-in port-to-service dictionary
- Display results in a clean, tabular format
- Count and display the total number of open ports found
- Simple command-line interface

---

## Technologies Used

- Python 3
- socket module
- TCP Networking
- Dictionary-based Service Identification

---

## Project Structure

```
GateKeeper/
│
├── main.py
├── README.md
└── .gitignore
```

---

## How It Works

1. The user enters a target domain or IP address.
2. The program resolves the target to an IPv4 address.
3. A start and end port are provided.
4. GateKeeper attempts to establish a TCP connection to every port in the specified range.
5. If a connection succeeds, the port is marked as **OPEN**.
6. The scanner looks up the port number in its internal service dictionary.
7. The results are displayed in a formatted table.

---

## Example Output

```text
=============================================
        GateKeeper
     TCP Port Scanner v0.4
=============================================

Enter Target (IP or Domain): scanme.nmap.org
Give start port number : 20
Give end port number   : 100

Target IP: 45.33.xxx.xxx

Scan Result
-----------------------------------

Port    Status    Service
-----------------------------------
22      OPEN      SSH
80      OPEN      HTTP
-----------------------------------
Scan Completed
Open Ports Found : 2
```

---

## Concepts Practiced

- TCP/IP Networking
- IPv4 Address Resolution
- DNS Lookup
- Socket Programming
- Port Scanning
- TCP Three-Way Handshake (Connection Attempt)
- Python Dictionaries
- Loops
- Conditional Statements
- Formatted Console Output

---

## Current Version

**Version:** v0.4

### Implemented

- TCP Port Scanning
- User-defined Port Range
- Domain Name Resolution
- Open Port Detection
- Service Identification
- Formatted Output

---

## Planned Improvements

- Banner Grabbing
- Multi-threaded Scanning
- Exception Handling Improvements
- Scan Time Measurement
- Export Scan Results
- Command-line Arguments
- IPv6 Support

---

## Learning Purpose

This project was built for educational purposes to strengthen my understanding of computer networking, Python programming, and cybersecurity fundamentals. It is part of my hands-on learning roadmap toward becoming a cybersecurity professional.

---

## Author

**Abhish Pulavarthi**

B.Tech Computer Science and Engineering (Cyber Security)  
SRM Institute of Science and Technology