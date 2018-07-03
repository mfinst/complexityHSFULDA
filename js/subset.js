"use strict"
// set => [1,3,5,7,12,45]; search => 5
subSet([1, 2, 3, 4, 5], 8);

//subSet([2, 4, 6, 8], 7);

function subSet(set, search) {
    let result = 0;
    let newSet = [];
    while (true) {
        let biggest = 0;
        for (let i = 0; i < set.length; i++) {
            if (set[i] <= search) {
                if (set[i] >= biggest) {
                    biggest = set.splice(i, 1);
                    console.log('biggest found' + biggest);
                }
            }
        }
        // console.log(set)
        result = result + biggest - 0;
        console.log('new result '+result)
        if (result === search) {
            newSet.push(biggest);
            console.log(newSet);
            return true
        }
        if (result > search) {
            console.log('reset '+result)
            result = result - biggest - 0;
        }
        if (set.length === 0) {
            console.log(result)
            console.log('no set found')
            return false;
        }
        if (result < search) newSet.push(biggest)
        biggest = 0;
    }
}