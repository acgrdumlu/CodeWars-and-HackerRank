class Person:
	def __init__(self, name):
		self.name = name

	def greet(self, other_name):
		return "Hi %s, my name is %s" % (other_name, self.name)