class HashTable:
	"""
	A HashTable is a data structure that provides a mapping 
	between keys and values using a hashing function. It 
	allows efficient retrieval, insertion, and deletion of 
	elements. The keys are hashed into indices of an array, 
	and values are stored at those indices. In case of hash 
	collisions, chaining is used to store multiple key-value 
	pairs at the same index.
	"""
	def __init__(self, size):
	    self.table = [[] for _ in range(size)]
	    self.size = size

	def put(self, key, val):
	    # Compute the index using the hash function
	    index = hash(key) % self.size
	    chain = self.table[index]
	    
	    # Search the chain to see if the key already exists
	    # If it does, overwrite it
	    for i in range(len(chain)):
	        if chain[i][0] == key:
	            chain[i] = (key, val)
	            return
	    
	    # If the key does not exist, append a new key-value 
	    # tuple to the chain
	    self.table[index].append((key, val))

	def get(self, key):
	    # Compute the index using the hash function
	    index = hash(key) % self.size

	    # Search the chain for the key and return 
	    # the corresponding value
	    for k, v in self.table[index]:
	        if k == key:
	            return v
	    
	    # If the key does not exist, raise a KeyError
	    raise KeyError
