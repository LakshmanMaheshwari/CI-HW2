import numpy as np
edgeList = []
nodes = 0
with open('queen11.txt','r') as file:
    i = 0
    for line in file:
        if (i >= 0 and i<3):
            pass
        elif i == 3:
            temp = line.strip().split()
            nodes = int(temp[2])
        else:
            x = line.strip().split()
            edgeList.append((int(x[1])-1,int(x[2])-1))
            #print(x)
        i += 1
# print(edgeList)
# print(len(edgeList))
G = {n:[] for n in range(nodes)}
for node1, node2 in edgeList:
        G[node1].append(node2)

# print(G)

M = [[1 for _ in range(nodes)] for _ in range(nodes)]
for i in range(len(M)):
    for j in range(len(M[i])):
        if j in G[i]:
            M[i][j] = 0
            M[j][i] = 0

def colors_used(ant):
    return len(set(ant))

alpha = 1
beta = 1
iterations = 30
best_val = float("inf")
ant_size = 30
# deg_node_pairs = [(k,len(v)) for k, v in G.items()]
# deg_dsc = list(reversed(sorted(deg_node_pairs, key=lambda x: x[1])))
# print(deg_dsc)
ants = list()
# for _ in range(ant_size):
#     coloring = [i for i in range(nodes)]
#     np.random.shuffle(coloring)
#     ants.append(coloring)
#     print(colors_used(coloring))


def update_cmin_N(v, cmin):
    # print(G[v])
    for neb in G[v]:
        max_cmin = 0
        for nebb in G[neb]:
            if cmin[nebb] > max_cmin:
                max_cmin = cmin[nebb]
        cmin[neb] = max_cmin + 1
        # print(neb, cmin[neb])

def update_dsat_N(v, dsat, A):
    for neb in G[v]:
        uncolored_neighbours = 0
        for nebb in G[neb]:
            if nebb in A:
                uncolored_neighbours += 1
        dsat[neb] = uncolored_neighbours

def select_prob(k, v, solution, cmin, dsat):
    des = dsat(v)
    trail = 0
    if len(solution[cmin[v]]) == 0:
        trail = 1
    else:
        for x in solution[cmin[v]]:
            trail += M[x][v]
        trail = trail / len(solution[cmin[v]])
    
    return des ** beta + trail ** alpha

def construct_coloring():
    cmin = [0 for _ in range(nodes)]
    dsat = [0 for _ in range(nodes)]
    solution = [set() for _ in range(nodes)]
    A = [i for i in range(nodes)]
    max_val = 0
    v = None
    for u in A:
        if len(G[u]) > max_val:
            max_val = len(G[u])
            v = u
    solution[0].add(v)
    q = 1
    print(solution)
    for k in range(1,nodes):
        print("Before")
        print(dsat)
        update_cmin_N(v, cmin)
        update_dsat_N(v, dsat, A)
        print("After")
        print(dsat)
        A.remove(v)
        v = select_prob(k, v, solution)
        break


for _ in range(1):
    dM = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for a in range(ant_size):
        ant = construct_coloring()
        break
# print(M)