# 🔎 Subdomain Finder

A simple Python-based subdomain enumeration tool that combines **wordlist brute force** and **passive API-based discovery**.

Built as a learning project to understand how real reconnaissance tools work under the hood.

---

## 🚀 Features

* 🔤 Wordlist-based subdomain brute forcing
* 🌐 Passive enumeration using Certificate Transparency logs
* ⚡ Fast DNS resolution checks
* 🧩 Modular code structure (easy to extend)
* 📄 Clean output of discovered subdomains

---

## 🧠 How It Works

This tool uses two main techniques:

### 1. Brute Force Enumeration

* Reads from a wordlist (`wordlist.txt`)
* Appends each entry to the target domain
* Checks if the subdomain resolves via DNS

Example:
admin.example.com
dev.example.com
api.example.com

---

### 2. Passive Enumeration (API)

* Queries Certificate Transparency logs via crt.sh
* Extracts subdomains from SSL certificate records
* No direct interaction with the target (stealthy)

---

## 📦 Project Structure

```
subdomain-finder/
│── main.py          # Entry point
│── utils.py         # DNS resolution logic
│── api_enum.py      # API-based enumeration
│── wordlist.txt     # Subdomain wordlist
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/subdomain-finder.git
cd subdomain-finder
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the tool:

```bash
python main.py
```

Enter a target domain when prompted:

```
Enter target domain: example.com
```

---

## 🧪 Example Output

```
[BF] admin.example.com
[BF] dev.example.com

=== RESULTS ===
admin.example.com
dev.example.com
mail.example.com
```

---

## 📌 Requirements

* Python 3.x
* requests
* dnspython

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes only**.

Do not use it against targets without proper authorization.
You are responsible for how you use this tool.

---

## 🛠️ Future Improvements

* Multi-threading for faster brute forcing
* HTTP probing (check which subdomains are alive)
* CLI argument support
* Integration with additional APIs
* Output export (JSON, TXT)

---

## 📚 Learning Goals

This project helps you understand:

* DNS resolution and subdomain discovery
* Passive vs active reconnaissance
* API handling and JSON parsing
* Basic automation in Python

---

## 🤝 Contributing

Pull requests are welcome. Feel free to fork and improve the tool.

---

## ⭐ Acknowledgments

* Certificate Transparency logs via crt.sh
* Inspired by tools like Subfinder and Amass

---
