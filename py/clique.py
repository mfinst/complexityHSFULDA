# Clique for undirected graphs
# representation of a graph
nodes1 = ['A', 'B', 'C']
neighbors1 = [('A','B'), ('B','C'), ('A','C')]

nodes2 = ['A', 'B', 'C', 'D']
neighbors2 = [('A','B'), ('B','C'), ('A','C'), ('A', 'D')]

nodes3 = ['A', 'B', 'C']
neighbors3 = [('A','B'), ('B','C')]

nodes4 = ['A']
neighbors4 = []

def find_clique(nodes, neighbors, clique):
    if len(clique) == len(nodes):
        # whole graph is a clique
        print(str(len(clique)) + ' ' + str(len(nodes)))
        print('clique size equals graph size found: ' + str(clique))
    if len(clique) == 0:
        # Ausgangspunkt
        for node in nodes:
            find_clique(nodes, neighbors, [node])
    else:
        # pruefen
        actualnode = clique[-1]
        for node in nodes:
            test = []
            if node != actualnode:
                for cliquemember in clique:
                    for neig in neighbors:
                        tuple = (cliquemember, node)
                        # print(tuple)
                        if (cliquemember, node) == neig or (node, cliquemember) == neig:
                            # print('neighbor found')
                            test.append(neig)
            if len(clique) == len(test):
                # node is in clique
                # print(' node ' + str(node) + ' in clique')
                clique.append(node)
                # print(str(clique) + ' ' + str(test))
                find_clique(nodes, neighbors, clique)
            else:
                # not in clique
                print('clique of size ' + str(len(clique)) + ' found ' + str(clique))


find_clique(nodes2, neighbors2, [])
