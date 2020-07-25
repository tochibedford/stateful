__author__ = "tochi bedford"

class StatefulNone(str):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__()
		self.states = []
		self.state = None
class StatefulString(str):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__()
		self.states = []
		self.state = None
class StatefulInt(int):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__()
		self.states = []
		self.state = None
class StatefulFloat(float):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__()
		self.states = []
		self.state = None
class StatefulList(list):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__(s, *args, **kwargs)
		self.states = []
		self.state = None
class StatefulDict(dict):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__(s, *args, **kwargs)
		self.states = []
		self.state = None
class StatefulSet(set):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__(s, *args, **kwargs)
		self.states = []
		self.state = None
class StatefulTuple(tuple):
	def __new__(cls, *args, **kwargs):
		return super().__new__(cls, args[0])

	def __init__(self, s, *args, **kwargs):
		super().__init__()
		self.states = []
		self.state = None
	def switch(self, newState):
		self.state = newState(self)

stLib = {
	type(None): StatefulNone,
	str: StatefulString,
	int: StatefulInt,
	float: StatefulFloat,
	list: StatefulList,
	dict: StatefulDict,
	set: StatefulSet,
	tuple: StatefulTuple,
	StatefulNone: type(None),
	StatefulString: str,
	StatefulInt: int,
	StatefulFloat: float,
	StatefulList: list,
	StatefulDict: dict,
	StatefulSet: set,
	StatefulTuple: tuple,

}

def _(obj, prev=None, stateful=True):
	if hasattr(prev, "states") and stateful:
		obj = stLib[type(obj)](obj)
		obj.states = [st for st in prev.states]
		obj.states.append(obj)
		try:
			obj.state = stLib[type(obj)](obj)
		except TypeError:
			obj.state = None
	elif stateful and prev:
		obj = stLib[type(obj)](obj)
		obj.states = [prev, obj]
		try:
			obj.state = stLib[type(obj)](obj)
		except TypeError:
			obj.state = None
	elif stateful:
		obj = stLib[type(obj)](obj)
		obj.states = [obj]
		try:
			obj.state = stLib[type(obj)](obj)
		except TypeError:
			obj.state = None
	return obj
