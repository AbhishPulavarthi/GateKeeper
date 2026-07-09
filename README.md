# GateKeeper

GateKeeper is a Python-based TCP port scanner built as part of my cybersecurity learning journey. It is designed to help understand how network communication, sockets, TCP connections, and port scanning work through practical implementation.

---

## Overview

GateKeeper scans a target host to determine whether a specific TCP port is open or closed. It supports both IPv4 addresses and domain names by resolving domain names into IP addresses before attempting a TCP connection.

---

## Current Features (v0.2)

- Scan a single TCP port
- Supports IPv4 addresses
- Supports domain names (DNS resolution)
- Detects whether a port is OPEN or CLOSED
- Configurable connection timeout
- Clean command-line interface
- Uses Python's built-in `socket` module

---

## Technologies Used

- Python 3
- socket

---

## Example

```text
=============================================
             GATEKEEPER v0.2
=============================================

Enter Target (IP or Domain): google.com
Enter Target Port          : 443

Scan Result
------------------------------
[OPEN] Port 443
```

---

## Current Version

**GateKeeper v0.2**

---

## Planned Features

- Scan a range of TCP ports
- Display common service names (HTTP, HTTPS, SSH, FTP, etc.)
- Better input validation and exception handling
- Banner grabbing
- Scan summaries
- Multithreaded scanning
- Export scan reports
- IPv6 support

---

## Purpose

This project is part of my Resume Sprint and cybersecurity learning roadmap. Each version introduces new networking concepts while following good software engineering practices such as version control, documentation, and incremental development.