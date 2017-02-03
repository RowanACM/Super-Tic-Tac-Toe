import sys

class Node():
	def __init__(self):
		pass


def minimax(node, depth, maximizingPlayer):
	if depth == 0 or node.children is None:
		return h(node)
	
	if maximizingPlayer:
		bestValue = -1 - sys.maxint
		for child in node.children:
			v = minimax(child, depth-1, FALSE)
			bestValue = v if (v > bestValue) else bestValue
		return bestValue
	else:
		bestValue = sys.maxint
		for child in node.children:
			v = minimax(child, depth - 1, TRUE)
			bestValue = v if (v < bestValue) else bestValue
		return bestValue

def h(node):
	pass

if __name__=="__main__":
	args = sys.argv
	# Make args useful here
	minimax()
