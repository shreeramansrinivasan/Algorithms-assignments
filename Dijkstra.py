import numpy as np
import re
def Dijkstra(graph,source_vertex):
	#distance vector of each vertex from source
	#initialize with zeros
	dist=np.zeros([1,len(graph)])
	#sets for keeping track of visited and un-visited verticesy
	setX=source_vertex;
	setV=[graph[i][0] for i in range(len(graph))]
	while setX!=setV:
		#step 1: Try to find the list of edges radiating from setX  to setV-setX
			











graph=[re.split(',|\t|\s',line.strip()) for line in open('test_dijkstra.txt')];

graph=[map(int,graph[i]) for i in range(len(graph)-1)];
#print graph
s_vertex=1;
Dijkstra(graph,s_vertex)	






















