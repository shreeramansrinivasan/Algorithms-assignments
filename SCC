#implement function for computing SCC

import numpy as np


#DFS loop main function
def DFS_loop(input_graph):
    global t
    global s
    global leader
    global finish_time
    global explore
    for i in range(len(explore),0,-1):
        if explore[i-1]==0:# which means that node has not been explored
            s=i
            DFS(input_graph,i)#call DFS

#subfunction of DFS loop that does DFS
def DFS(func_input_graph,vertex):
    #mark the vertex as explored
    explore[vertex-1]=1#vertex marked as explored
    leader[vertex-1]=s#leader of a particular node
    #find which rows of first column correspond to input vertex
    indices_in_vertex=np.where(np.array([func_input_graph[i][0] for i in range(len(func_input_graph))])==vertex)[0];
    for i in indices_in_vertex:
        if explore[func_input_graph[i][1]-1]==0:
            DFS(func_input_graph,func_input_graph[i][1]);#pass the current vertex into DFS

    t=t+1
    finish_time[vertex-1]=t;


graph=[np.array(map(int,line.split())) for line in open('DFS_loop_test.txt') ];

graph_rev_col1=[graph[i][0] for i in range(0,len(graph))];
graph_rev_col2=[graph[i][1] for i in range(0,len(graph))];
graph_rev=np.column_stack([graph_rev_col2,graph_rev_col1])


leader=np.zeros(max(graph_rev_col1))
finish_time=np.zeros(max(graph_rev_col1));
explore=np.zeros(max(graph_rev_col1))
s=0;
t=0;
DFS_loop(graph_rev);
explore=np.zeros(len(graph))

graph_modified=None
#create a new graph using finishing times
for i in range(2):
    for j in range(len(graph_rev_col1)):
        graph_modified[i][j]=finish_time[graph[i][j]]

finish_time=None
del graph

DFS_loop(graph_modified)




