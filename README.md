# GateKeeper

GateKeeper is a Python-based TCP port scanner built as part of my cybersecurity learning journey. It is designed to help understand how network communication, sockets, TCP connections, and port scanning work through practical implementation.

---

## Overview

GateKeeper scans a target host to identify open TCP ports. It supports both IPv4 addresses and domain names by resolving domain names into IP addresses before performing TCP connection attempts across a user-defined range of ports.

This version expands the scanner from checking a single port to scanning multiple ports, making it a more practical network reconnaissance tool while continuing to focus on learning the fundamentals of networking and socket programming.

---

## Current Features (v0.3)

- Scan a user-defined range of TCP ports
- Supports IPv4 addresses
- Supports domain names (DNS resolution)
- Detects open TCP ports
- Displays all discovered open ports
- Displays the total number of open ports found
- Configurable connection timeout
- Clean command-line interface
- Uses Python's built-in `socket` module

---

## Technologies Used

- Python 3
- Python Socket Library
- TCP Networking

---

## Example

```text
=============================================
        GateKeeper
     TCP Port Scanner v0.3
=============================================

Enter Target (IP or Domain): openai.in
Give start port number : 443
Give end port number   : 445

Target IP : 172.67.161.68

Scan Result
------------------------------
Open Ports
[OPEN] 443
------------------------------
Scan Completed
Open Ports Found : 1
```

---

## Current Version

**GateKeeper v0.3**

---

## What's New in v0.3

- Added TCP port range scanning
- Improved output formatting
- Added scan completion summary
- Displays total number of open ports found
- Improved variable naming and overall code readability
- Reduced scan timeout for faster execution

---

## Planned Features

- Better input validation
- Exception handling
- Service detection
- Banner grabbing
- Multithreaded scanning
- Export scan reports
- IPv6 support
- Command-line arguments
- Performance optimizations

---

## Purpose

This project is part of my cybersecurity learning roadmap and portfolio development. Each version introduces new networking concepts while following software engineering practices such as incremental development, documentation, and version control.

The long-term goal of GateKeeper is to evolve from a basic TCP port scanner into a more capable network reconnaissance tool by implementing progressively advanced networking concepts.

---

## Disclaimer

This project is intended for educational purposes only.

Only scan systems that you own or have explicit permission to test.