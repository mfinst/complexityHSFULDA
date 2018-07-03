# Gerichteter Graph
colors = ['Red', 'Blue', 'Green']
nodes = ['A', 'B', 'C', 'D', 'E']
neighbors = dict()
neighbors['A'] = ['B']
neighbors['B'] = ['A']
neighbors['C'] = ['A']
neighbors['D'] = ['A']
neighbors['E'] = ['D', 'A', 'C']
colors_of_states = {}


def promising(node, color):
    for neighbor in neighbors.get(node):
        color_of_neighbor = colors_of_states.get(neighbor)
        # print( str(color_of_neighbor) + color)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_state(node):
    for color in colors:
        if promising(node, color):
            return color


def main():
    for node in nodes:
        colors_of_states[node] = get_color_for_state(node)
    print(colors_of_states)


main()
