# Basic Python Port Scanner

A simple multi-threaded TCP port scanner built with Python sockets.
This project is part of my cybersecurity learning journey.

## 🚀 Features

* Scans ports 1–1024 (common ports)
* Uses TCP connect scanning
* Multi-threaded for faster performance
* Command-line input for target

## 🛠️ Requirements

* Python 3.x

## ▶️ Usage

```bash
python scanner.py <target>
```

### Example:

```bash
python scanner.py scanme.nmap.org
```

## 🧠 How It Works

The scanner attempts to establish a TCP connection to each port:

* If the connection succeeds → port is **open**
* If it fails → port is **closed or filtered**

## ⚠️ Disclaimer

This tool is for **educational purposes only**.
Do NOT scan systems you don’t have permission to test.

## 📌 Future Improvements

* Add port range selection
* Banner grabbing (service detection)
* Save results to a file
* Improve threading efficiency
