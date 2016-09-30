import numpy as np
import re
def Dijkstra(graph,source_vertex):
	#distance vector of each vertex from source
	#initialize with zeros
	dist=np.zeros([len(graph)])
	#sets for keeping track of visited and un-visited verticesy
	setX=set([source_vertex]);
	setV=set([graph[i][0] for i in range(len(graph))])
	#array=list();#array of all distances from each vertex
	min_array=list();#min dist array from all the vertices
	vertex_list=list()#maintain the list of vertices with min distance
	min_dist_vertex_list=list()
	while setX!=setV:
		#step 1: Try to find the list of edges radiating from setX  to setV-setX
		
		for vertices in list(setX):
			array=list([np.Inf])#array for finding the minimum in each vertex's case
			vertex_list=list([np.Inf])
			#Parse through all edges and compute the minimum distance 
			for i in range(1,len(graph[vertices-1]),2):#need to parse only the odd indices
				if not(setX.__contains__(graph[vertices-1][i])):#the vertex has not been visited
					array.append(dist[vertices-1]+graph[vertices-1][i+1])#add the distance 
					vertex_list.append(graph[vertices-1][i])#append the vertex
			#print array
			min_array.append(min(array))#find minimum distance for edges radiating from each vertex
			min_dist_vertex_list.append(vertex_list[array.index(min(array))])#Keep track of the vertex who has a minimum length edge with another vertex in setX
		#figure out which out of all of them is the minimum
		temp=min(min_array)
		#print min_dist_vertex_list[min_array.index(temp)]
		dist[min_dist_vertex_list[min_array.index(temp)]-1]=temp#update the distance vector 
		#update the set X 
		setX.add(min_dist_vertex_list[min_array.index(temp)])
		#reinitialise the values 
		min_dist_vertex_list=list()
		min_array=list()
	
	
	return dist			
									
									
				
						











graph=[re.split(',|\t|\s',line.strip()) for line in open('Dijkstradata.txt')];

graph=[map(int,graph[i]) for i in range(len(graph)-1)];
#print graph
s_vertex=1;
distance=Dijkstra(graph,s_vertex)	
print distance[7-1]
print distance[37-1]
print distance[59-1]
print distance[82-1]
print distance[99-1]
print distance[115-1]
print distance[133-1]
print distance[165-1]
print distance[188-1]
print distance[197-1]




















