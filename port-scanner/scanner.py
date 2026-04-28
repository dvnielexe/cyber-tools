import socket
import threading

target = "scanme.nmap.org"

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"[OPEN] Port {port}")
    sock.close()

threads = []
for port in range(1, 1025):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()