import datastructures as ds
import json

def parse_cases(structure, type):
	with open('cases/' + structure +'.json', 'r') as file:
		test = json.loads(file.read())
		if structure == 'binarytree':
			return [ds.BinaryTree(case) for case in test[type]]
		elif structure == 'graph':
			return [ds.Graph(case["nodes"], [(edge[0], edge[1]) for edge in case["graph"]]) for case in test[type]]
		elif structure == 'hashtable':
			return [ds.HashTable.evaluate(actions) for actions in test[type]]
		elif structure == 'heap':
			return [ds.Heap.evaluate(actions) for actions in test[type]]
		elif structure == 'linkedlist':
			return [ds.LinkedList.evaluate(actions) for actions in test[type]]
		elif structure == 'disjointsets':
			return [ds.DisjointSets(val, pairs) for val, pairs in test[type]]

def parse_solutions(test, structure, type):
	with open('solutions/' + structure + '.json') as file:
		results = json.loads(file.read())
		return results[test][type]

def error_str(result, solution, case_structure, case):
	return 'Got ' + str(result) + ', Expected ' + str(solution) + ' when testing ' + case_structure + ' ' + str(case)