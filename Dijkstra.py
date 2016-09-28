import numpy as np
import re
def Dijkstra(graph,source_vertex):
	#distance vector of each vertex from source
	#initialize with zeros
	dist=np.zeros([1,len(graph)])
	#sets for keeping track of visited and un-visited verticesy
	setX=source_vertex;
	setV=[graph[i][0] for i in range(len(graph))]
	array=list();#array of all distances from each vertex
	min_array=list();#min dist array from all the vertices
	while setX!=setV:
		#step 1: Try to find the list of edges radiating from setX  to setV-setX
		for vertices in setX:
			#Parse through all edges and compute the minimum distance 
			for i in range(1,len(graph[vertices]),2):#need to parse only the odd indices
				if !setX.__contains__(graph[vertices][i]):#the vertex has not been visited
							
				
						











graph=[re.split(',|\t|\s',line.strip()) for line in open('test_dijkstra.txt')];

graph=[map(int,graph[i]) for i in range(len(graph)-1)];
#print graph
s_vertex=1;
Dijkstra(graph,s_vertex)	






















