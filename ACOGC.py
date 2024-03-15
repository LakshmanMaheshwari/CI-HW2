import numpy as np
import matplotlib.pyplot as plt
import random


class ACOGC:
    def __init__(self, hyp):
        self.G = dict()
        self.best_val = float("inf")
        self.best_sol = []
        self.rho = hyp['Rho']
        self.alpha = hyp['Alpha']
        self.beta = hyp['Beta']
        self.iterations = hyp['Iterations']
        self.ant_size = hyp['Antsize']
        self.best_so_far = []
        self.avg_so_far = []
        self.populate_graph(hyp['filename'], hyp['ub'])
    def populate_graph(self, filename, ub):
        edgeList = []
        self.nodes = 0
        self.ants = list()
        with open(filename,'r') as file:
            i = 0
            for line in file:
                if (i >= 0 and i<ub):
                    pass
                elif i == ub:
                    temp = line.strip().split()
                    self.nodes = int(temp[2])
                else:
                    x = line.strip().split()
                    edgeList.append((int(x[1])-1,int(x[2])-1))
                i += 1
        self.G = {n:[] for n in range(self.nodes)}
        for node1, node2 in edgeList:
                self.G[node1].append(node2)
        self.M = [[1 for _ in range(self.nodes)] for _ in range(self.nodes)]
        for i in range(len(self.M)):
            for j in range(len(self.M[i])):
                if j in self.G[i]:
                    self.M[i][j] = 0
                    self.M[j][i] = 0
    def update_dsat_cmin_N(self, v, dsat, A, cmin):
        for neb in self.G[v]:
            max_cmin = 0
            colors = []
            val = 0
            neb_colors = set()
            for nebb in self.G[neb]:
                neb_colors.add(cmin[nebb])
                if not(nebb in A) and not(cmin[nebb] in colors):
                    colors.append(cmin[neb])
                    val += 1
            while max_cmin in neb_colors:
                max_cmin += 1
            cmin[neb] = max_cmin
            dsat[neb] = val
    def select_prob(self, k, solution, cmin, dsat, A):
        probs = []
        for v in A:
            des = dsat[v]
            trail = 0
            if len(solution[cmin[v]]) == 0:
                trail = 1
            else:
                for x in solution[cmin[v]]:
                    if not(x in self.G[v]):
                        trail += self.M[x][v]
                trail = trail / len(solution[cmin[v]])
            denom_sum = 0
            for u in A:
                tr = 0
                if len(solution[cmin[u]]) == 0:
                    tr = 1
                else:
                    tr = 0
                    for x in solution[cmin[u]]:
                        if not(x in self.G[u]):
                            tr += self.M[x][u]
                    tr = tr / len(solution[cmin[u]])
                denom_sum += (dsat[u] ** self.beta)*(tr**self.alpha)
            if denom_sum in [0, 0.0]:
                denom_sum = 1
            probs.append(((des ** self.beta) * (trail ** self.alpha))/denom_sum)
        if sum(probs) == 0:
            return A[random.randint(0,len(A)-1)]
        probs = [i/sum(probs) for i in probs]
        p = random.uniform(0,1)
        cdf = 0
        idx = 0
        for i in probs:
            if cdf <= p <= cdf + i:
                return A[idx]
                break
            cdf = cdf + i
            idx += 1
    def construct_coloring(self):
        cmin = [0 for _ in range(self.nodes)] 
        dsat = [0 for _ in range(self.nodes)] 
        solution = [set() for _ in range(self.nodes)] 
        A = [i for i in range(self.nodes)] 
        max_val = 0
        v = None
        for u in A:
            if len(self.G[u]) > max_val:
                max_val = len(self.G[u])
                v = u
        solution[0].add(v)
        q = 0
        for k in range(1,self.nodes):
            self.update_dsat_cmin_N(v, dsat, A, cmin) 
            A.remove(v) 
            v = self.select_prob(k, solution, cmin, dsat, A)
            c = cmin[v] 
            solution[c].add(v)
            if c == q+1:
                q += 1
        return solution
    def run(self):
        for _ in range(self.iterations):
            current_fitness = []
            print(f"Iteration No. {_}")
            dM = [[0 for _ in range(self.nodes)] for _ in range(self.nodes)]
            for a in range(self.ant_size):
                s = self.construct_coloring()
                q = 0
                for i in s:
                    if len(i) != 0:
                        q += 1
                current_fitness.append(q)
                if q < self.best_val:
                    self.best_val = q
                    self.best_sol = s
                for i in s:
                    for j in i:
                        for k in i:
                            if not(j in self.G[k]) and j != k:
                                dM[j][k] += 1/q
            for r in range(len(self.M)):
                for s in range(len(self.M[r])):
                    if not(r in self.G[s]):
                        self.M[r][s] = self.M[r][s] * (1-self.rho) + dM[r][s]
            self.avg_so_far.append(sum(current_fitness)/len(current_fitness))
            self.best_so_far.append(self.best_val)
        self.get_plot()
    def get_plot(self):
        n = [i for i in range(1,self.iterations+1)]
        plt.plot(n, self.best_so_far)
        plt.plot(n, self.avg_so_far)
        plt.legend(["Best So Far", "Average So Far"])
        plt.title("ACO on Graph Coloring")
        plt.show()


