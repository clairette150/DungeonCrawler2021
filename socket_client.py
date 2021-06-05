import socket, sys, threading


class Client:
	def __init__(self):
		self.host = '127.0.0.1'
		self.port = 8000
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def make_socket(self):
		print("Sending...", self.connection.connect((self.host, self.port)))
		
	def send(self, message="TEST"):
		byte_message = bytes(message, "utf-8")
		self.connection.sendall(byte_message)
		sys.stdout.flush()
		#my_sock.shutdown(socket.SHUT_WR)

	def listen(self):			
		data = self.connection.recv(1024)
		if not data:
			pass
		return data
	
	def wait_for_input(self):
		while True:
			user_input = input("You: ")
			self.send(user_input)

if __name__ == "__main__":
	client = Client()
	print(client.connection)
	#print(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	client.make_socket()
	print("Your name?")
	name = input()
	client.send("nick:" + name)
	input_thread = threading.Thread(target=client.wait_for_input)
	input_thread.start()
	while True:
		data = client.listen()
		if len(data) > 0:
			print(" said: ", data.decode("utf-8")) #add clear-line char!

