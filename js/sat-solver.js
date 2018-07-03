"use strict"
// Strat
// Literals
// a-x => Variables
// A, O, (, ), N => Symbols
// aANDb
// var test = "aA((bANc)ANd)A(eONe)";
// solver(test, ['a', 'b', 'c', 'd', 'e']);
var wichtel = '(aANb)A(aANc)A(aANd)'
solver(wichtel, ['a', 'b', 'c', 'd'])

function solver (literal, values) {
    let table = [];
    for (let i = (Math.pow(2, values.length) - 1) ; i >= 0 ; i--) {
        for (let j = (values.length - 1); j >= 0; j--) {
            table[j] = (i & Math.pow(2, j)) ? 1 : 0;
        }
        // Setups
        // console.log(table);
        if(solve(literal, table, values)){
            console.log('solvable with:' + table + ' ' + values);
            // return true; // if only one is needed
        }
    }
    console.log('Done');
    return false;
}

function solve (literal, setup, values) {
    //substitute
    let newLiteral = literal;
    for(let k = 0; k< values.length; k++) {
        let regex = new RegExp(values[k],'g');
        newLiteral = newLiteral.replace( regex , setup[k]);
    }
    console.log('solving...')
    while(true) {
        // resolve NOT
        newLiteral = newLiteral.replace(/N1/g, '0')
        newLiteral = newLiteral.replace(/N0/g, '1')
        // resolve AND
        newLiteral = newLiteral.replace(/1A1/g, '1')
        newLiteral = newLiteral.replace(/\dA0|0A\d/g, '0')
        // resolve OR
        newLiteral = newLiteral.replace(/\dO1|1O\d/g, '1')
        newLiteral = newLiteral.replace(/0O0/g, '0')
        // resolve Brackets
        newLiteral = newLiteral.replace(/\(1\)/g, '1')
        newLiteral = newLiteral.replace(/\(0\)/g, '0')
        // Check if solved
        console.log(newLiteral);
        if(newLiteral.length == 1 ){
            return newLiteral[0] === '1' ? true : false;
        }
    }
    // Fallback
    return false;
}
