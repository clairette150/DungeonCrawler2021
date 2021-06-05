import socket, sys
from _thread import *

from talkingmode import TalkingModeEncoder, speak_mode, shout_mode, whisper_mode, inform_mode

host = "127.0.0.1"
port = 8000


# https://docs.python.org/3/library/socket.html?highlight=sockets#socket.socket

class ClientConnection():
	def __init__(self, port, host):
		self.socket = None
		self.port =  port
		self.host =  host

	def make_connection_socket():
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		my_socket.bind((self.host, self.port))
		my_socket.listen(True)

	def give_connection_info():
		pass


class Server():
	def __init__(self):
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.my_socket.bind((host, port)) #socket.bind(0)
		self.my_socket.listen(True)
		self.clientsList=[]
		self.dictionary_of_client_names = {}
		print("Socket is listening")

    def parse_data(self, data):
       data_dict = json.loads(data.decode())
       # isinstance(object, classinfo)
       assert(isinstance(data_dict, dict)) 
       return data_dict

    def create_message(self, msg):
        assert(isinstance(msg, dict))
        return json.dumps(msg)

	def perpare_answer(self, message):
		# {"who": client_name, "talking_mode":say/whisper/shout/inform, "what":data}
		
		
		# handle commands:
		
		#TODO: Parse json
		
		
		
		
		
		# This won't work with json
		if data.decode("utf-8").startswith("nick:"):
			self.dictionary_of_client_names[str(sc)] = data.decode("utf-8")[5:]
			print("added new client named: ", data.decode("utf-8")[5:])
			return False
		else
			return answer
			
			# shout
			message = bytes("{} shout {}".format(self.dictionary_of_client_names[str(sc)], output.decode("utf-8")), "utf-8")
			
			# whisper
			message = bytes("{} whispers {}".format(self.dictionary_of_client_names[str(sc)], output.decode("utf-8")), "utf-8")
			
			# say
			message = bytes("{} sais {}".format(self.dictionary_of_client_names[str(sc)], output.decode("utf-8")), "utf-8")
		

	def clientHandler(self, sc, sock_name):
		print("Connection with", sc, sock_name)
		peer_name = sc.getpeername()
		print("peer_name: ", peer_name)
		n = 0
		while True:
			data = sc.recv(1024)
			if not data:
				break
			output = data.decode('ascii').encode('ascii')
			if self.prepare_answer(data) == False:
				continue # no sending of data here 
			else:
				answer = self.prepare_answer(data)
				for client in self.clientsList:
					print(self.clientsList)
					print("sending")
					try:
						if client != sc:
							client.sendall(message)
					except:
						print("removing client:  ", client)
						print("Bye {}", self.dictionary_of_client_names.get([str(client)], "unknown"))
						self.dictionary_of_client_names.pop([str(client)])
						self.clientList.remove(client)
			n += len(data)
			print('\r %d bytes processed so far' % (n,), end=' ')
			sys.stdout.flush()

	def run(self):
		while True:
			sc, sock_name = self.my_socket.accept()
			self.clientsList.append(sc)
			start_new_thread(self.clientHandler, (sc, sock_name))
			#sc.close()
			#print("-- socket closed -- ")


		print()
if __name__ == "__main__":
	server = Server()
	server.run()
