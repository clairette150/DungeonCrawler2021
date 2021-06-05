from json import JSONEncoder
import json


class TalkingMode:
	def __init__(self, name, verb, color=(255, 0, 0, 1)):
		self.name = name
		self.verb = verb  #english
		self.color = color  
		#self.range =       # how many tiles in each direction
		

speak_mode = TalkingMode("speak", "sais", color=(255, 223, 0, 1))
shout_mode = TalkingMode("shout", "shouts", color=(255, 0, 53, 1))
whisper_mode = TalkingMode("whisper", "whispers", color=(170, 227, 229, 1))
inform_mode = TalkingMode("inform", "see")		


class TalkingModeEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, TalkingMode):
            return object.__dict__
        else:
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)


# jsonString = TalkingModeEncoder().encode(speak_mode)
