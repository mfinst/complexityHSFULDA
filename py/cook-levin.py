import json

test = {
    "start": ['0'],
    "end": "5",
    "alphabet": ['>', ' ', '0'],
    'states': ['0', '5'],
    "0": {
        ">>>": {
            "write": [">", ">", ">"],
            "move": [1, 1, 1],
            "newState": "5"}
    }
}


# initState =

# Appearance of SAT by Max Finsterbusch
# variables = ['A', 'B']
# formula = 'A$nB'
# $n = AND; $v = OR; ~ = NOT; () = Brackets
# forbidden symbolcombinations in turing machine: $n, $v, ~, (, ),

def cook_levin(tm_json):
    print('#START######################################################################################')
    line_length = 6
    variables = set()
    formula = ''
    # tm = json.loads(tmjson)
    print(tm_json)
    # Rule 1 Initial State of the Machine
    initial = tm_json['start']
    inputFormula = ''
    for i in range(0, len(initial)):
        iSymVar = 'T' + str(i) + str(initial[i]) + '0'
        variables.add(iSymVar)
        inputFormula = inputFormula + iSymVar + '$n'
    print('input mapped: ' + inputFormula)
    formula = formula + inputFormula
    # Rule 2 initiale Kopfpositionen AND Rule 3 Maschine im Startzustand
    # Startzustand enthaelt Kopf Position
    stateFormula = ''
    for key in tm_json['0']:
        for stateindex in range(0, len(key)):
            variables.add('H0' + str(stateindex))
            stateFormula = stateFormula + 'H0' + str(stateindex) + '$n'
    print('initial headposition mapped: ' + stateFormula)
    variables.add('Q00')
    formula = formula + 'Q00$n' + stateFormula
    # Rule 4 At Most one Symbol per Cell
    # i Zellen
    # Band ist 10 Zellen lang
    atMostOneFormula = ''
    for key in tm_json['0']:
        # for k lines
        for k in range(0, len(key)):
            # in i cells; has to be bigger than the input and maximal output
            # for palindrom line lenght of 6 is fine in this example
            for i in range(0, line_length):
                atMostForCellFormula = ''
                cellvariable = ''
                activeWord = ' '
                if i == 0:
                    # first symbol is always the same
                    cellvariable = 'T>' + str(k)
                    activeWord = '>'
                elif k == 0 and i < len(initial):
                    # first line detected; write initial in cells
                    cellvariable = 'T' + str(initial[i]) + str(k)
                    activeWord = str(initial[i])
                else:
                    # cell of line k is empty
                    cellvariable = 'T ' + str(k)
                variables.add(cellvariable)
                atMostForCellFormula = '~' + cellvariable + '$v'
                # add all symbols to the formula for the cellvariable, that are not on it
                for word in tm_json['alphabet']:
                    if word != activeWord:
                        othercellvariable = 'T' + word + str(k)
                        variables.add(othercellvariable)
                        atMostForCellFormula = atMostForCellFormula + othercellvariable + '$n'
                atMostOneFormula = atMostOneFormula + atMostForCellFormula
    print('At Most One Symbol mapped: ' + atMostOneFormula)
    formula = formula + atMostOneFormula
    # Rule 5 At Least One Symbol per Cell
    atLeastFormula = ''
    for key in tm_json['0']:
        # for k lines
        for k in range(0, len(key)):
            # in i cells; has to be bigger than the input and maximal output
            # for palindrom line lenght of 6 is fine in this example
            for i in range(0, line_length):
                atLeastCellFormula = ''
                for word in tm_json['alphabet']:
                    atLeastVariable = 'T' + str(i) + str(word) + str(k)
                    variables.add(atLeastVariable)
                    atLeastCellFormula = atLeastCellFormula + atLeastVariable + '$n'
                atLeastFormula = atLeastFormula + atLeastCellFormula
    print('At Least One Symbol mapped: ' + atLeastFormula)
    formula = formula + atLeastFormula
    # Rule 6 Nur ein Zustand pro Schritt
    onlyOneStateFormula = ''
    for key in tm_json['0']:
        # for k lines
        for k in range(0, len(key)):
            for state1 in tm_json['states']:
                for state2 in tm_json['states']:
                    onlyOneStatePairFormula = ''
                    if state1 != state2:
                        stateVariable1 = 'Q' + str(k) + str(state1)
                        stateVariable2 = 'Q' + str(k) + str(state2)
                        variables.add(stateVariable1)
                        variables.add(stateVariable2)
                        # enthaelt Redundanz: Q1 UND Q2 ODER Q2 UND Q1
                        onlyOneStatePairFormula = onlyOneStatePairFormula + '~' + stateVariable1 + '$v~' + stateVariable2 + '$n'
                    onlyOneStateFormula = onlyOneStateFormula + onlyOneStatePairFormula
    print('Only one state per Step mapped: ' + onlyOneStateFormula)
    formula = formula + onlyOneStateFormula
    # Rule 7 Nur eine Kopf Position pro Schritt bzw. Rule 1 aus der Vorlesung
    onlyOnePosFormula = ''
    for i in range(0, line_length):
        for inot in range(0, line_length):
            for key in tm_json['0']:
            # for k lines
                for k in range(0, len(key)):
                    # enthaelt Redundanz: Q1 UND Q2 ODER Q2 UND Q1
                    if i != inot:
                        pos1 = 'H' + str(i) + str(k)
                        pos2 = 'H' + str(inot) + str(k)
                        variables.add(pos1)
                        variables.add(pos2)
                        onlyOnePosFormula = onlyOnePosFormula + '~' + pos1 + '$v~' + pos2 + '$n'
    print('Only One Pos mapped: ' + onlyOnePosFormula)
    formula = formula + onlyOnePosFormula
    # Rule 8 Transitions fuer k an position i
    # My Machines can only have 9 states due to how comparison of strings work so lets assume this
    # if a number 0 - 9 exists as property, the transition exists;
    # the states array has all states!
    for state in tm_json['states']:
        print(str(state))
    # Rule 9 Es muss einen Akzeptierenden Zustand geben
    # My Machines always accept in one state only
    acceptingVariable = 'Q' + tm_json['end']
    variables.add(acceptingVariable)
    formula = formula + acceptingVariable
    print('Acc State: ' + acceptingVariable)
    print('Result Formula')
    print(formula)
    print(variables)
    print(str(len(formula)) + ' char long Formula with ' + str(len(variables)) + ' different variables')
    print('#END########################################################################################')
    return formula


cook_levin(test)

palindrom = {
    'start': [">", "a", "b", "b", "c"],
    'end': '4',
    'word': ['>', '1', '0', '1'],
    'alphabet': ['>', ' ', 'a', 'b', 'c', '1', '0'],
    'states': ['0', '1', '2', '3', '4'],
    '0': {
        ">>>": {
            'write': ['>', '>', '>'],
            'move': [1, 1, 1],
            'newState': '1'
        }
    },
    '1': {
        "1  ": {
            'write': ['1', '1', ' '],
            'move': [1, 1, 0],
            'newState': '1'
        },
        "0  ": {
            'write': ['0', '0', ' '],
            'move': [1, 1, 0],
            'newState': '1'
        },
        "   ": {
            'write': [' ', ' ', ' '],
            'move': [0, -1, 0],
            'newState': '2'
        }
    },
    '2': {
        " 1 ": {
            'write': [' ', '1', ' '],
            'move': [0, -1, 0],
            'newState': '2'
        },
        " 0 ": {
            'write': [' ', '0', ' '],
            'move': [0, -1, 0],
            'newState': '2'
        },
        " > ": {
            'write': [' ', '>', ' '],
            'move': [-1, 1, 0],
            'newState': '3'
        }
    },
    '3': {
        "11 ": {
            'write': ['1', '1', ' '],
            'move': [-1, 1, 0],
            'newState': '3'
        },
        "00 ": {
            'write': ['0', '0', ' '],
            'move': [-1, 1, 0],
            'newState': '3'
        },
        "01 ": {
            'write': ['0', '1', '0'],
            'move': [0, 0, 0],
            'newState': '4'
        },
        "10 ": {
            'write': ['1', '0', '0'],
            'move': [0, 0, 0],
            'newState': '4'
        },
        ">  ": {
            'write': ['>', ' ', '1'],
            'move': [0, 0, 0],
            'newState': '4'
        }
    }
}
cook_levin(palindrom)
