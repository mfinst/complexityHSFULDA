//Configurations
var test = {
    'start': '0',
    'end': '5',
    '0': {
        ">>>": {
            'write': ['>', '>', '>'],
            // 1=right, -1=left, 0=stay
            'move': [1, 1, 1],
            'newState': '5'
        }
    }
}
var abc = {
    'start': '0',
    'end': '9',
    'word': ['>', 'a', 'a', 'b', 'c', 'c'],
    '0': {
        ">>>": {
            'write': ['>', '>', '>'],
            'move': [1, 1, 1],
            'newState': '1'
        }
    },
    '1': {
        "a  ": {
            'write': ['a', 'a', ' '],
            'move': [1, 1, 0],
            'newState': '1'
        },
        "b  ": {
            'write': ['b', 'b', ' '],
            'move': [1, 1, 0],
            'newState': '1'
        },
        "c  ": {
            'write': ['c', 'c', ' '],
            'move': [1, 1, 0],
            'newState': '1'
        },
        "   ": {
            'write': [' ', ' ', ' '],
            'move': [-1, -1, 0],
            'newState': '2'
        }
    },
    '2': {
        "cc ": {
            'write': ['c', 'c', ' '],
            'move': [0, -1, 0],
            'newState': '2'
        },
        "cb ": {
            'write': ['c', 'b', ' '],
            'move': [-1, -1, 0],
            'newState': '2'
        },
        "aa ": {
            'write': ['a', 'a', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "bb ": {
            'write': ['b', 'b', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "ca ": {
            'write': ['c', 'a', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "c> ": {
            'write': ['c', '>', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "b> ": {
            'write': ['b', '>', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "a> ": {
            'write': ['a', '>', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "ba ": {
            'write': ['b', 'a', ' '],
            'move': [0, 0, 0],
            'newState': '3'
        }
    },
    '3': {
        "ba ": {
            'write': ['b', 'a', ' '],
            'move': [-1, -1, 0],
            'newState': '3'
        },
        "a> ": {
            'write': ['a', '>', '1'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "b> ": {
            'write': ['b', '>', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "aa ": {
            'write': ['a', 'a', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        },
    }
}

var palindrom = {
    'start': '0',
    'end': '4',
    'word': ['>', '1', '0', '1'],
    '0': {
        ">>>": {
            'write': ['>', '>', '>'],
            // 1=right, -1=left, 0=stay
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

var binaryAdd = {
    'start': '0',
    'end': '9',
    'word': ['>', '1', '+', '1'],
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
        "+  ": {
            'write': ['+', '+', ' '],
            'move': [1, 0, 1],
            'newState': '2'
        }
    },
    '2': {
        "1+ ": {
            'write': ['1', '+', ' '],
            'move': [1, 0, 1],
            'newState': '2'
        },
        "0+ ": {
            'write': ['0', '+', ' '],
            'move': [1, 0, 1],
            'newState': '2'
        },
        " + ": {
            'write': [' ', '+', ' '],
            'move': [-1, -1, -1],
            'newState': '3'
        }
    },
    // Rechenstate Add
    '3': {
        "00 ": {
            'write': ['0', '0', '0'],
            'move': [-1, -1, -1],
            'newState': '3'
        },
        "01 ": {
            'write': ['0', '1', '1'],
            'move': [-1, -1, -1],
            'newState': '3'
        },
        "10 ": {
            'write': ['1', '0', '1'],
            'move': [-1, -1, -1],
            'newState': '3'
        },
        "11 ": {
            'write': ['1', '1', '0'],
            'move': [0, 0, 0],
            'newState': '4'
        },
        // nicht sicher?
        "111": {
            'write': ['1', '1', '1'],
            'move': [0, 0, -1],
            'newState': '4'
        },
        "101": {
            'write': ['1', '0', '0'],
            'move': [0, 0, -1],
            'newState': '4'
        },
        "011": {
            'write': ['0', '1', '0'],
            'move': [0, 0, -1],
            'newState': '4'
        },
        "001": {
            'write': ['0', '0', '1'],
            'move': [-1, -1, -1],
            'newState': '3'
        },
        "+> ": {
            'write': ['>', '>', ' '],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "+>1": {
            'write': ['>', '>', '1'],
            'move': [0, 0, 0],
            'newState': '9'
        },
        "+>0": {
            'write': ['>', '>', '0'],
            'move': [0, 0, 0],
            'newState': '9'
        }
    },
    // Zwischenschritt Merken
    '4': {
        "111": {
            'write': ['1', '1', '1'],
            'move': [0, 0, -1],
            'newState': '4'
        },
        "110": {
            'write': ['1', '1', '0'],
            'move': [0, 0, -1],
            'newState': '4'
        },
        "11 ": {
            'write': ['1', '1', '1'],
            'move': [-1, -1, 0],
            'newState': '3'
        },
    }
}
// turingStart(palindrom, 3, palindrom.word, palindrom.start, palindrom.end)
// a^n, b^n, c^n
// False
turingStart(abc, 3, ['>', 'a', 'b', 'b', 'c'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a', 'b', 'c', 'c'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a', 'a', 'b', 'c'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a', 'a', 'b', 'b'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a', 'b'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'b', 'c'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a', 'c'], abc.start, abc.end);
// True
turingStart(abc, 3, ['>', 'a', 'b', 'c'], abc.start, abc.end);
turingStart(abc, 3, ['>', 'a', 'a', 'b', 'b', 'c', 'c'], abc.start, abc.end);
// Bedingung Zaheln müssen gleich lang sein!
turingStart(binaryAdd, 3, ['>', '0', '0', '1', '0', '+', '1', '0', '1', '1'], binaryAdd.start, binaryAdd.end);

function turingStart(program, tapes, word, currentstate, endstate) {
    console.log('+++++++Input Word+++++++++++++++++')
    console.log(word)
    let tapesArray = [];
    let pointers = [0];
    tapesArray.push(word)
    for (i = 1; i < tapes; i++) {
        pointers.push(0);
        tapesArray.push(['>']);
    }
    // Debug Logs Configuration
    // console.log('+++++++Turing Machine Setup+++++++')
    // console.log(tapesArray);
    // console.log(pointers);
    // console.log('+++++++Program++++++++++++++++++++')
    // console.log(program);
    // console.log('+++++++Steps++++++++++++++++++++++')
    while (currentstate < endstate) {
        let currentInputs = '';
        for (i = 0; i < tapes; i++) {
            currentInputs = currentInputs + tapesArray[i][pointers[i]];
        }
        // Debug Logs currentTransition
        // console.log('currentIns "' + currentInputs.replace(/undefined/g, ' ') + '"')
        let transition = program[currentstate][currentInputs.replace(/undefined/g, ' ')]
        // console.log(transition);
        for (i = 0; i < tapes; i++) {
            tapesArray[i][pointers[i]] = transition.write[i];
            pointers[i] += transition.move[i]
        }
        currentstate = transition.newState;
        // Debug Logs Afterstate
        // console.log(tapesArray);
        // console.log(pointers);
    }
    console.log('+++++++Result+++++++++++++++++++++')
    console.log(tapesArray)
}

