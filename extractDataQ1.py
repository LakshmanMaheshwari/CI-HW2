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
Graph = {}
for node1, node2 in edgeList:
    if node1 in Graph:
        Graph[node1].append(node2)
    else:
        Graph[node1] = [node2]

print(Graph)
