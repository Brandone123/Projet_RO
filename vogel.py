"""
By Chiegang Sape 20-02-2020 02:04

La Méthode d’Approximation de Vogel (VAM) est connue aussi par :l’heuristique de Balas-Hammer 
/la Méthode de la différence maximum / la méthode de pénalité unitaire /la méthode des regrets maximaux successifs.
– La méthode VAM est basée sur la notion de coût de pénalité où de regret.
– Un coût de pénalité est la différence entre le coût de case le plus grand et
le plus important d’une rangée (ligne où colonne).
– Dans VAM, la première étape consiste à développer un coût de pénalité
pour chaque source et destination.
– Le coût de pénalité est calculé en soustrayant le coût de case minimum du
coût de case supérieur suivant dans chaque rangée.

"""

from collections import defaultdict
 
costs  = {'W': {'A': 10, 'B': 10, 'C': 11},
          'X': {'A': 13, 'B': 14, 'C': 12},
          'Y': {'A': 9, 'B': 12, 'C': 5},
          'Z': {'A': 15, 'B': 10, 'C': 13}}
demand = {'A': 10, 'B': 15, 'C': 20}
cols = sorted(demand.keys())
supply = {'W': 14, 'X': 9, 'Y': 11, 'Z': 11}
res = dict((k, defaultdict(int)) for k in costs)
g = {}
for x in supply:
    g[x] = sorted(costs[x].keys(), key=lambda g: costs[x][g])
for x in demand:
    g[x] = sorted(costs.keys(), key=lambda g: costs[g][x])
 
while g:
    d = {}
    for x in demand:
        d[x] = (costs[g[x][1]][x] - costs[g[x][0]][x]) if len(g[x]) > 1 else costs[g[x][0]][x]
    s = {}
    for x in supply:
        s[x] = (costs[x][g[x][1]] - costs[x][g[x][0]]) if len(g[x]) > 1 else costs[x][g[x][0]]
    f = max(d, key=lambda n: d[n])
    t = max(s, key=lambda n: s[n])
    t, f = (f, g[f][0]) if d[f] > s[t] else (g[t][0], t)
    v = min(supply[f], demand[t])
    res[f][t] += v
    demand[t] -= v
    if demand[t] == 0:
        for k, n in supply.items():
            if n != 0:
                g[k].remove(t)
        del g[t]
        del demand[t]
    supply[f] -= v
    if supply[f] == 0:
        for k, n in demand.items():
            if n != 0:
                g[k].remove(f)
        del g[f]
        del supply[f]
 
for n in cols:
    print("\t", n)
print
cost = 0
for g in sorted(costs):
    print (g, "\t")
    for n in cols:
        y = res[g][n]
        if y != 0:
            print (y)
        cost += y * costs[g][n]
        print ("\t")
    print
print ("Total Cost = ", cost)