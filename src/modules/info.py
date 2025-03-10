import platform
import psutil
import socket
import os
import sys

# System info using platform module
print("System:", platform.system())
print("Machine:", platform.machine())
print("Processor:", platform.processor())
print("OS Version:", platform.version())
print("Python version:", platform.python_version())

# CPU info using psutil
print("CPU cores:", psutil.cpu_count(logical=False))
print("Logical CPUs:", psutil.cpu_count(logical=True))
print("CPU usage (%):", psutil.cpu_percent(interval=1))

# Memory info using psutil
memory = psutil.virtual_memory()
print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
print(f"Free Memory: {memory.free / (1024 ** 3):.2f} GB")

# Disk info using psutil
disk = psutil.disk_usage('/')
print(f"Total Disk Space: {disk.total / (1024 ** 3):.2f} GB")
print(f"Used Disk Space: {disk.used / (1024 ** 3):.2f} GB")
print(f"Free Disk Space: {disk.free / (1024 ** 3):.2f} GB")

# Network info using socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print("Hostname:", hostname)
print("IP Address:", ip_address)

# Python runtime info using sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)
print("Platform:", sys.platform)
