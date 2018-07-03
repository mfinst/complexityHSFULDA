# Graph Faerbe Problem
colors = ['Red', 'Blue', 'Green']
nodes = ['A', 'B', 'C', 'D', 'E']
neighbors = {}
neighbors['A'] = ['B']
neighbors['B'] = ['A']
neighbors['C'] = ['A']
neighbors['D'] = ['A']
neighbors['E'] = ['D', 'A', 'C']


# ~ NOT
# $n AND
# $v OR
# VAR
# ()
# Reduktion von 3Col nach Sat
def main ():
    sat = ''
    for node in nodes:
        sat = sat + '(' + colors[0] + node + '$v' + colors[1] + node  + '$v' + colors[2] + node + ')$n'
    # festlegen, wer nicht die selbe Farbe haben darf
    for node in nodes:
        sat = sat + '('
        for color in colors:
            sat = sat + '~' + color + node
            for neighbor in neighbors.get(node):
                sat = sat + '$v-' + color + neighbor
        sat = sat + ')' + '$n'
    sat = sat[:-2]
    print(sat)
main()