from json import JSONEncoder

class Action:
	def __init__(self, who, what, data):
		self.who = who
		self.data = data
		
	def do(self):
		raise NotImplementedError
		
class ActionEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Action):
            return object.__dict__
        else:
            # raising exceptions for unsupported types
            return json.JSONEncoder.default(self, object)



# Examples:
# {"who":"client", "action":"request", "data":"map"}
# {"who":"client", "action":"request", "data":"player"}
# {"who":"client", "action":"register name", "data":"clientname"}
# {"who":"client", "action":"move player", "data":"location"}
