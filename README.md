# GateKeeper v0.6

GateKeeper is a Python-based TCP port scanner developed as a personal learning project to understand networking, socket programming, and service enumeration. The project is built from scratch with a focus on learning how network scanners work rather than relying on external libraries.

> **Note:** This project is intended for educational purposes and should only be used on systems you own or have permission to test.

---

## Features

- Scan a custom range of TCP ports
- Detect open and closed TCP ports
- Resolve domain names to IPv4 addresses
- Identify common services using well-known port numbers
- Perform basic TCP banner grabbing
- Send HTTP requests to web servers
- Parse HTTP responses and extract the `Server` header
- Display scan results in a clean terminal table

---

## Example Output

```text
=============================================
        GateKeeper
     TCP Port Scanner v0.6
=============================================

Enter Target (IP or Domain): google.com
Give start port number : 79
Give end port number   : 80

Target IP: 142.xxx.xxx.xxx

Scan Result
----------------------------------------------------------------------

Port    Status    Service        Banner
----------------------------------------------------------------------
80      OPEN      HTTP           gws
----------------------------------------------------------------------

Scan Completed
Open Ports Found : 1
```

---

## Built With

- Python 3
- Socket Programming
- TCP Networking
- DNS Resolution (`socket.gethostbyname`)
- Basic HTTP Protocol

---

## Current Capabilities

- TCP Connect Scan
- Domain Name Resolution
- Common Service Identification
- TCP Banner Grabbing
- HTTP GET Request
- HTTP `Server` Header Extraction

---

## Project Structure

```text
GateKeeper/
├── main.py          # Main scanner logic
├── services.py      # Common service definitions
└── README.md
```

---

## Version History

### v0.6 – HTTP-Aware Banner Parsing

- Added HTTP GET request support
- Implemented HTTP-aware banner grabbing
- Extracted the HTTP `Server` header
- Improved banner parsing for cleaner output

### v0.5 – TCP Banner Grabbing

- Implemented TCP connect scanning
- Added banner grabbing
- Added common service identification
- Added domain name resolution

---

## Roadmap

### Networking

- UDP port scanning
- IPv6 support
- Configurable timeout

### Performance

- Multi-threaded scanning

### Protocol Support

- HTTPS support
- SSH banner parser
- FTP banner parser
- SMTP banner parser

### Output

- Export results to JSON
- Export results to CSV
- Command-line arguments

---

## Requirements

- Python 3.10 or later
- No external dependencies

---

## Learning Objectives

This project is helping me gain practical experience with:

- Computer Networking
- TCP/IP
- Socket Programming
- Service Enumeration
- Banner Grabbing
- Protocol Analysis
- Cybersecurity Fundamentals

---

## Author

**Abhish Pulavarthi**

Cybersecurity Undergraduate  
SRM Institute of Science and Technology (SRMIST)