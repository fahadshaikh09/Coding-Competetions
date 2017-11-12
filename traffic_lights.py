"""
	PROBLEM STATMENT : 
	you are given a roadmap of a country consisting of N cities and M roads. Each city has a traffic light, The traffic light has only 2 colors, Green and Red. All the traffic lights will swtich their color from Green to Red and vice cersa after every T seconds. You can cross a city only when the traffic light in the city is Green. Intially, all the lights are Green.At a city if the traffic light is Red, you have to wait for it to switch its color to Green. The time taken to travel through any road is C seconds.

	Input :
	The First Line contains 4 space separated integers, N, M, T and C
	Next M lines contains two integers each U and V denotting that there is a bidirectional road between U and V

	Output:
	Find Out:
	i) Minimum Time
	ii) Shortest Route
	iii) Second Minimum Time

"""

from pprint import pprint
import copy

def get_signal_status(curr_time, T):
	return "G" if curr_time % (2*T) < T else "R"

def get_wait_time(curr_time, T):
	return 2*T - (curr_time % (2*T))

def get_all_paths(graph, root, curr_time, T, C, N, traversed=[1], all_paths = []):

	# print "current : root = {root} | curr_time = {time} | traversed = {traversed}".format(root=root, time=curr_time, traversed=traversed)

	if root == N: # is it a N'th node ?
		all_paths.append([curr_time, traversed])
		return

	if not graph[root]: #is it a leaf node ?
		return

	signal_status = get_signal_status(curr_time, T)

	wait_time = 0
	if signal_status=="R":
		wait_time = get_wait_time(curr_time, T)

	start_time_for_next_node = wait_time + curr_time

	for child_node in graph[root]:
		if child_node not in traversed:
			get_all_paths(graph, child_node, start_time_for_next_node + C, T, C, N, traversed + [child_node])

	return all_paths
			
if __name__ == '__main__':
	input_ = """7 7 3 5
				1 2
				1 3
				2 4
				2 7
				3 7
				3 5
				5 6
				6 7"""

	lines = input_.split("\n")
	N, M, T, C = map(int, lines[0].split(" "))

	#create empty graph
	graph = {i :[] for i in range(1, N+1)}

	#collect all the edges
	for line in lines[1:]:
		i, j = map(int, line.split(" "))
		graph[i].append(j)

	print "Graph : ", 
	pprint(graph)


	curr_time = 0
	root = 1
	all_paths = get_all_paths(graph, root, curr_time, T, C, N)

	print "All Possible Paths with costs: ", 
	pprint(all_paths)
	
	print "Minium Time Path: ", min(all_paths, key=lambda x: x[0])[0]
	print "Shortest Route : ", min(all_paths, key=lambda x: len(x[1]))[1]
	print "Longest Route : ", max(all_paths, key=lambda x: len(x[1]))[1]
	print "Second Minimum Time: ", sorted(set([x[0] for x in all_paths]))[1]
