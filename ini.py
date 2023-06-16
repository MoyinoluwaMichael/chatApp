# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 6999))
# s.listen(5)
#
# while True:

#     clientSocket, address = s.accept()
#     print(f"Established a connection with {address}")
#     # print(clientSocket.recv(2000))
#     clientSocket.send(bytes("Hello World", "utf-8"))
#     clientSocket.close()