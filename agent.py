import random as r 
import numpy as np 


results = list()
iters = 3

def world():
	#creating an agent space/environment
	environment = np.zeros(shape = (3,3))
	#assigning random dirty and clean spots where 1 = clean and 0 = dirty
	for row in environment:
		rand_cols = np.random.randint(0,2,3)
		row[rand_cols] = 1

	#randomly assigning vacuum cleaner spot in the environment
	environment[r.randint(0,1)][r.randint(0,1)] = 2
	return environment

def performance(square, moves):
	# gets the cell value of the np matrix
	score = 0
	if square == 1: #does nothing if clean
		moves = moves + 1
		return score, moves
	elif square == 0: #cleans
		moves = moves + 1
		square = 1
		score = score + 1
		return score, moves
	else:
		moves = moves + 1
		score = score + 0
		return score, moves #starting point of vacuum cleaner


def runReflexAgent(world):
	#iterate through the matrix and pass each cell value to performance

	#environment = world()
	score = 0
	moves = 0
	for row in world:
		print str(row)
		moves = moves+1
		for element in row:
			score, moves = performance(element, moves)
			score = score + moves
	return score


for iteration in range(0,iters):

	environment = world()
	score = runReflexAgent(environment)
	print score
	results.append(score)
	# print score

print "average number of cleaning moves = {}".format(sum(results)/iters)



