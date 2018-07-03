# Inverted Graph = zwischen jedem Knoten wo im original eine Kante war, besteht keine
# zwischen jedem Knoten wo keine Kante war, besteht nun eine Kante
gnodes = ['A', 'B', 'C', 'D', 'E']
gneighbors = {}
gneighbors['A'] = ['B']
gneighbors['B'] = ['A']
gneighbors['C'] = ['A']
gneighbors['D'] = ['A']
gneighbors['E'] = ['D','A','C']


def invert_graph(neighbors, nodes):
    invertedNeighbors = {}
    for node in nodes:
        newneighbors = []
        for nnode in nodes:
            if (nnode in neighbors[node]) == False:
                print('not in')
                newneighbors.append(nnode)
        print(newneighbors)
        invertedNeighbors[node] = newneighbors
        # check if node is a neighbor
    print(invertedNeighbors)


invert_graph(gneighbors, gnodes)
# Clique