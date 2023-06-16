import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Connecting...")
s.connect(("192.168.1.179", 7070))
print("Connected")
s.send(bytes("Yesssssssssssssssssssssssssssssssssssssssssssssssssssssss, E enter?", "utf-8"))
msg = s.recv(2048)

print(msg)

s.close()
