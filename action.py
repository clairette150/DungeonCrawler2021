from json import JSONEncoder
import json

from talking_mode import TalkingMode, TalkingModeEncoder, speak_mode, shout_mode, whisper_mode, inform_mode

class Action:
	def __init__(self, who, action, data):
		self.who = who
		self.action = action
		self.data = data
		
	def do(self):
		raise NotImplementedError
		
class ActionEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Action) or isinstance(object, TalkingMode):
            return object.__dict__
        else:
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)



# Examples:
# {"who":"client", "action":"request", "data":"map"}
# {"who":"client", "action":"request", "data":"player"}
# {"who":"client", "action":"register name", "data":"clientname"}
# {"who":"client", "action":"move player", "data":"location"}


class Talk(Action):
	def __init__(self, who, action, data, talking_mode):
		super().__init__(who, action, data)
		self.talking_mode = talking_mode
		
	def do(self):
		print("{} {} {}".format(self.who, self.talking_mode.verb, self.data))
	
class Request(Action):
	pass
	
	
class RegisterName(Action):
	pass
	

class SendData(Action):
	pass
	

class Move(Action):
	def __init__(self, who, action='move', data=(0,0)):
		super().__init__(who, action, data)
		self.talking_mode = talking_mode	
	
	def do(self, postion_data):
		if is_walkable(postion_data):
			# Todo: set actor's x, y 
			return new_postion
		else:
			return old_position 

	
if __name__ == "__main__":
	talk = Talk("Client", "talk", "Hello World", speak_mode)
	talk.do()
	talk_json = ActionEncoder().encode(talk)
	print(talk_json)
