edgeList = []
with open('queen11.txt','r') as file:
    i = 0
    for line in file:
        if (i >= 0 and i<=3):
            pass
        else:
            x = line.strip().split()
            edgeList.append((int(x[1]),int(x[2])))
            #print(x)
        i += 1
#print(edgeList)
print(len(edgeList))
DirectedGraph = {}
for node1, node2 in edgeList:
    if node1 in DirectedGraph:
        DirectedGraph[node1].append(node2)
    else:
        DirectedGraph[node1] = [node2]

Graph = {}
for node1, neighbours in DirectedGraph.items():
    Graph[node1] = neighbours.copy()

    for j in neighbours:
        if j in Graph:
            Graph[j].append(node1)
        else:
            Graph[j] = [node1]

print(Graph)
