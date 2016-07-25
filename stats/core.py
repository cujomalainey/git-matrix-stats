import theading

class stats():
	"""
	"""
	def __init__(self, github):
		self.github = github
		self.process()
		self.kick_off = 1
		self.last_limit = 5000

	def process(self):
		self.calculate_kickoff()
		threading.Timer(self.kick_off, self.process).start()

	def calculate_kickoff(self):
		pass