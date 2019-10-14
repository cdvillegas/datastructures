class HashTable:
	def __init__(self, size):
		self.table = [[] for _ in range(size)]
		self.size = size

	def __str__(self):
		s = ''
		for bucket in self.table:
			for key, val in bucket:
				s += '(' + str(key) + ' => ' + str(val) + ')'
		return s

	def put(self, key, val):
		index = hash(key) % self.size
		chain = self.table[index]
		for i in range(len(chain)):
			if chain[i][0] == key:
				chain[i] = (key, val)
				return
		self.table[index].append((key, val))

	def get(self, key):
		index = hash(key) % self.size
		for k, v in self.table[index]:
			if k == key:
				return v
		raise KeyError

	@staticmethod
	def evaluate(actions):
		table = None
		res = []
		for action in actions:
			action = action.split(' ')
			if action[0] == 'init':
				table = HashTable(int(action[1]))
				res.append(None)
			elif action[0] == 'put':
				res.append(table.put(action[1], action[2]))
			elif action[0] == 'get':
				res.append(table.get(action[1]))
		return res