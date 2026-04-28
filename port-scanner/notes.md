# Port Scanning Notes

## 🔹 What is Port Scanning?

Port scanning is the process of checking which ports on a system are open, closed, or filtered.

Each port corresponds to a service:

* 22 → SSH
* 80 → HTTP
* 443 → HTTPS

---

## 🔹 TCP 3-Way Handshake

A TCP connection is established using:

1. **SYN** → Client sends request
2. **SYN-ACK** → Server responds
3. **ACK** → Client confirms connection

If this process completes, the port is considered **open**.

---

## 🔹 TCP Connect Scan

This is the type used in this project.

### How it works:

* Attempts full TCP connection using system calls
* If connection succeeds → port is open
* If connection fails → port is closed

### Pros:

* Simple to implement
* Reliable

### Cons:

* Slower than other methods
* Easily detected (completes full handshake)

---

## 🔹 Other Scan Types (Overview)

### SYN Scan (Half-Open)

* Sends SYN, receives SYN-ACK, then resets connection
* Faster and stealthier
* Requires raw socket access (admin/root)

### UDP Scan

* Sends UDP packets
* No response usually means open or filtered
* Slower and less reliable

---

## 🔹 Key Takeaways

* Open ports = potential attack surface
* Port scanning is a fundamental recon technique
* Tools like Nmap automate and optimize this process

---

## 🔹 Real-World Context

Security professionals use port scanning to:

* Identify exposed services
* Detect misconfigurations
* Perform penetration testing

Attackers use it for reconnaissance before exploitation.

---

## 🔹 Next Steps

* Learn service/version detection
* Understand firewalls and filtering
* Explore advanced scanning techniques
