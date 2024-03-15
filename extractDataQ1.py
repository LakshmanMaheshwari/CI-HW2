import numpy as np
import matplotlib.pyplot as plt
import random
import time
edgeList = []
nodes = 0
with open('le450.txt','r') as file:
    i = 0
    for line in file:
        if (i >= 0 and i<33):
            pass
        elif i == 33:
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


iterations = 30
ant_size = 30
deg_node_pairs = [(k,len(v)) for k, v in G.items()]
# deg_dsc = list(reversed(sorted(deg_node_pairs, key=lambda x: x[1])))
# print(deg_dsc)
ants = list()
# for _ in range(ant_size):
#     coloring = [i for i in range(nodes)]
#     np.random.shuffle(coloring)
#     ants.append(coloring)
#     print(colors_used(coloring))

def check_feasibility(cmin):
    for v in G:
        current_color = cmin[v]
        for u in G[v]:
            if cmin[u] == current_color and cmin[u] != 0:
                print(u, v, cmin[u], u in G[v])
                return False
    return True

def update_cmin_N(v, cmin):
    # print(G[v])
    for neb in G[v]:
        max_cmin = 0
        neb_colors = set()
        for nebb in G[neb]:
            neb_colors.add(cmin[nebb])
        while max_cmin in neb_colors:
            max_cmin += 1
        cmin[neb] = max_cmin
        # print(neb, cmin[neb], neb_colors)

def update_dsat_N(v, dsat, A, cmin):
    
    
    for neb in G[v]:
        max_cmin = 0
        colors = []
        val = 0
        neb_colors = set()
        for nebb in G[neb]:
            neb_colors.add(cmin[nebb])
            if not(nebb in A) and not(cmin[nebb] in colors):
                colors.append(cmin[neb])
                val += 1
        while max_cmin in neb_colors:
            max_cmin += 1
        cmin[neb] = max_cmin
        dsat[neb] = val

def select_prob(k, solution, cmin, dsat, A):
    probs = []
    for v in A:
        des = dsat[v]
        trail = 0
        if len(solution[cmin[v]]) == 0:
            trail = 1
        else:
            for x in solution[cmin[v]]:
                if not(x in G[v]):
                    trail += M[x][v]
            trail = trail / len(solution[cmin[v]])
        denom_sum = 0
        for u in A:
            # print(u)
            tr = 0
            if len(solution[cmin[u]]) == 0:
                tr = 1
            else:
                tr = 0
                for x in solution[cmin[u]]:
                    if not(x in G[u]):
                        tr += M[x][u]
                tr = tr / len(solution[cmin[u]])
            denom_sum += (dsat[u] ** beta)*(tr**alpha)
        if denom_sum in [0, 0.0]:
            denom_sum = 1
        # if ((des ** beta) * (trail ** alpha))/denom_sum != 0.0:
        #     print(((des ** beta) * (trail ** alpha))/denom_sum)
        probs.append(((des ** beta) * (trail ** alpha))/denom_sum)
    # print(sum(probs))
    if sum(probs) == 0:
        # print("Random")
        return A[random.randint(0,len(A)-1)]
    # print("Not Random")
    probs = [i/sum(probs) for i in probs]
    # print(sum(probs))
    p = random.uniform(0,1)
    cdf = 0
    idx = 0
    for i in probs:
        if cdf <= p <= cdf + i:
            return A[idx]
            break
        cdf = cdf + i
        idx += 1

def construct_coloring():
    cmin = [0 for _ in range(nodes)] # Min color assignment to each node (Initially set to 0)
    dsat = [0 for _ in range(nodes)] # No of different colors assigned to neighbors (Initially 0 since all vertices are initally uncolored)
    solution = [set() for _ in range(nodes)] # Solution is the partition of nodes into subsets such that all the nodes in a subset have the same color
    A = [i for i in range(nodes)] # Uncolored Nodes. Initially all of them are uncolored
    # choosing the node with the maximum degree
    max_val = 0
    v = None
    for u in A:
        if len(G[u]) > max_val:
            max_val = len(G[u])
            v = u
    # Assigning lowest possible color i.e. 0 to v
    solution[0].add(v)
    q = 0
    # print(solution)
    for k in range(1,nodes):
        # print("Before")
        # print("dsat", dsat)
        # print("cmin", cmin)
        
        # update_cmin_N(v, cmin)
        update_dsat_N(v, dsat, A, cmin) # Update dsat and cmin values of neighbors of v
        # print(check_feasibility(cmin))
        # print(k)
        # print("After")
        # print("cmin", cmin)
        # print("dsat", dsat)
        
        A.remove(v) # Now that v is colored, we remove it
        # break
        v = select_prob(k, solution, cmin, dsat, A) # Selecting v based on probability formula
        # print(v)
        c = cmin[v] # Assigning color to v
        solution[c].add(v)
        if c == q+1:
            q += 1
        # print(solution)
    return solution

best_val = float("inf")
best_sol = []
rho = 0.5
alpha = 2
beta = 2
best_so_far = []
avg_so_far = []
# a = time.perf_counter()
for _ in range(iterations):
    # print(max(M))
    current_fitness = []
    print(f"Iternation No. {_}")
    dM = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for a in range(ant_size):
        # print(time.perf_counter() - a)
        # a = time.perf_counter()
        # print(M)
        # print("h")
        s = construct_coloring()
        # print("i")
        q = 0
        for i in s:
            if len(i) != 0:
                q += 1
        print(a, q)
        current_fitness.append(q)
        if q < best_val:
            best_val = q
            best_sol = s
        for i in s:
            for j in i:
                for k in i:
                    if not(j in G[k]) and j != k:
                        dM[j][k] += 1/q
                        # dM[k][j] += 1/q
    for r in range(len(M)):
        for s in range(len(M[r])):
            if not(r in G[s]):
                # print("update")
                M[r][s] = M[r][s] * (1-rho) + dM[r][s]
                # M[s][r] = M[s][r] * (1-rho) + dM[s][r]
    avg_so_far.append(sum(current_fitness)/len(current_fitness))
    best_so_far.append(best_val)
    # print(M)
# print(best_sol)
# print(best_val)

n = [i for i in range(1,iterations+1)]
plt.plot(n, best_so_far)
plt.plot(n, avg_so_far)
plt.legend(["Best So Far", "Average So Far"])
plt.title("ACO on Graph Coloring")
plt.show()