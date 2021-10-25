# hostname // 내부ip주소 // 외부ip주소 // mac주소 // 현재시간


import socket

print("Host Name ", socket.gethostname())

print("IP Address(Internal) : ", socket.gethostbyname(socket.gethostname()))


# import socket

print("Host Name ", socket.gethostname())

print("IP Address(Internal) : ", socket.gethostbyname(socket.gethostname()))

print("IP Address(External) : ", socket.gethostbyname(socket.getfqdn()))

# print("IP Address(External) : ", socket.getaddrinfo('localhost', 8080))
