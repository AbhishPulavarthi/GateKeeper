# GateKeeper

A lightweight TCP Port Scanner built in Python as part of my cybersecurity learning journey.

Current Version: **v0.5**

---

## Overview

GateKeeper is a command-line TCP port scanner that discovers open ports on a target host and attempts basic service identification and banner grabbing.

This project is under active development as part of my cybersecurity learning journey. New features will be added incrementally while focusing on understanding networking concepts and secure software development.
---

## Features

- TCP Port Scanning
- User-defined port range
- Domain name to IPv4 resolution
- Open port detection using TCP sockets
- Common service identification
- Basic banner grabbing
- Timeout handling
- Exception handling
- Formatted scan results

---

## Technologies Used

- Python 3
- socket
- TCP Networking

---

## Current Workflow

1. Enter a target IP address or domain.
2. Specify the starting and ending port.
3. Scan each TCP port.
4. Identify open ports.
5. Match common services.
6. Attempt banner grabbing.
7. Display results in a formatted table.

---

## Sample Output

```text
=============================================
        GateKeeper
     TCP Port Scanner v0.5
=============================================

Enter Target (IP or Domain): example.com

Port    Status    Service        Banner
---------------------------------------------------------------
22      OPEN      SSH            SSH-2.0-OpenSSH_9.9
80      OPEN      HTTP           Unknown
443     OPEN      HTTPS          Unknown

---------------------------------------------------------------
Scan Completed
Open Ports Found : 3
```

---

## Current Limitations

- HTTP servers generally require a request before sending data.
- HTTPS banner grabbing is not yet implemented.
- Only basic TCP scanning is supported.
- No multithreading yet.
- No UDP scanning.
- No OS detection.

---

## Learning Outcomes

This version focuses on understanding:

- TCP sockets
- Client-server communication
- Port scanning
- Socket timeouts
- Exception handling
- Banner grabbing concepts
- Service identification
- Python list indexing and iteration

## Author

**Abhish Pulavarthi**

Cybersecurity Student  
SRM Institute of Science and Technology