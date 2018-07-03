# setup of a graph
nodesT = ['A', 'B', 'C', 'D', 'E', 'F']
neighborsT = {}
neighborsT['A'] = ['B', 'F']
neighborsT['B'] = ['C', 'E']
neighborsT['C'] = ['D', 'A', 'B']
neighborsT['D'] = ['C', 'A']
neighborsT['E'] = ['A', 'E']
neighborsT['F'] = ['D']
# one Solution would be A>F>E>D>C>B

def dHamPath(nodes, neighbors, node, hampath):
    print('nodes: ' + str(nodes) + ' neighbors: ' + str(neighbors) + ' node: ' + str(node) + ' hampath: ' + str(hampath))
    if len(nodes) == 0:
        print('Hamiltonian cycle found : ' + str(hampath))
        return hampath
    if node in hampath:
        #check if ok or bad
        if len(nodes) != 1:
            thisnode = node
            # letzten Knoten holen
            node = hampath[-1]
            if len(neighbors[node]) == 0:
                # wuut
                print('no Hamlitonian Path found')
                return False
            # letzten Knoten in die nodesliste packen
            nodes.append(node)
            # Nachbar löschen
            neighbors[node].remove(thisnode)
            # vorherigen Knoten aus der Loesung streichen
            del hampath[-1]
            dHamPath(nodes, neighbors ,node , hampath)

        else:
            print('Hamiltonian path found: ' + str(hampath))
            return hampath
    for neighbor in neighbors[node]:
        if neighbor in nodes: # Nachbar kann besucht werden
            nodes.remove(node)
            hampath.append(node)
            # print('can visit neighbor: ' + neighbor)
            # print('remaining nodes: ' + str(nodes) + ' with path of: ' + str(hampath))
            # print('neighbor of ' + node + neighbors)
            dHamPath(nodes, neighbors, neighbor, hampath)
        if neighbor == hampath[0]:
            print('nodes: ' + str(nodes) + ' neighbors: ' + str(neighbors) + ' node: ' + str(node) + ' hampath: ' + str(hampath))
            # Problem: Backtracking muss gefixt werden
            nodes.remove(node)
            hampath.append(node)
            dHamPath(nodes, neighbors, neighbor, hampath)


dHamPath(nodesT, neighborsT, nodesT[0], [])
