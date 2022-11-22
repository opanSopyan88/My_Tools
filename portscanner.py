import socket

def scan(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		serviceversion = sock.recv(1024)
		serviceversion = serviceversion.decode('utf-8')
		serviceversion = serviceversion.strip('\n')
		print(f'port {str(port)} is open', end='     ')
		print(serviceversion)
	except ConnectionRefusedError:
		print(f'Port {str(port)} is closed')
	except UnicodeDecodeError:
		print(f'port {str(port)} is closed')

target = input('Target: ')
ports = input('Port: ')

if ',' in ports:
	portlist = ports.split(',')
	for port in portlist:
		scan(target, int(port))
elif '-' in ports:
	portrange = ports.split('-')
	start = int(portrange[0])
	end = int(portrange[1])
	for port in range(start, end):
		scan(target, port)
else:
	scan(target, int(ports))

