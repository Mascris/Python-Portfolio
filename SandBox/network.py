import socket
from datetime import datetime

# The Logic: We aren't managing strings; we are managing connections.
target = "192.168.1.1"  # Could be a local IP like 192.168.1.1
print(f"Scanning target: {target}")

try:
    # 1. Resolve the URL to an IP address (Talks to DNS)
    ip = socket.gethostbyname(target)
    print(f"IP Address: {ip}")

    # 2. Check common ports (80=HTTP, 443=HTTPS, 21=FTP)
    ports = [21, 80, 443, 8080]
    
    for port in ports:
        # Create a socket object (This is the 'phone' that calls the server)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # Don't wait forever
        
        # Try to connect
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
        
        s.close()
        
except Exception as e:
    print(f"Error: {e}")

# USEFULNESS:
# You can run this to see if your own server is secure, 
# or if a website is actually down or if it's just your browser acting up.
