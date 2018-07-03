import random as random
from datetime import datetime
from fractions import gcd

def median ( list, k ):
    if( k==0 ):
        k = int(len(list) / 2)+1
    randomindex = random.randint(0, len(list) -1)
    x = list[ randomindex ]
    counter = 0
    listgreater = []
    listlesser = []
    for num in list:
        if( num <= x):
            counter+=1
        if( num <= x):
            listlesser.append(num)
        else:
            listgreater.append(num)
    print('list ' + str(list))
    print('x ' + str(x)+ ' from index '+ str(randomindex))
    print('k ' + str(k))
    print('m ' + str(counter))
    print('listlesser ' + str(listlesser))
    print('listgreater ' + str(listgreater))
    if(counter == k):
        print('median found ' + str(x))
    else:
        if(counter < k):
            median(listgreater, k-counter)
        if(counter > k):
            median(listlesser, k)
#[1,1,2,2,3,4,23,51,51]
#median([2,1,3,1,51,2,51,23,4],0)
            
def jacobi(n, m):
    j = 1

    # rule 5
    n %= m
    
    while n:
        # rules 3 and 4
        t = 0
        while not n & 1:
            n /= 2
            t += 1
        if t&1 and m%8 in (3, 5):
            j = -j

        # rule 6
        if (n % 4 == m % 4 == 3):
            j = -j

        # rules 5 and 6
        n, m = m % n, n

    return j if m == 1 else 0

def probprime (num):
    a = random.randint(1, num-1)
    if(gcd(a, num)>1):
        print('composite')
        return 0
    #print('no GCD with ' + str(a))
    b = (a ** ( (num-1)/2)) % num
    #print( '('+ str(a) + ' ** (' + str(num) + ' - 1) / 2) % ' + str(num))
    #print(str(b))
    if( 1 < b < num-1):
        print('composite')
        return 0
    #print('euler says could be prime')
    j = jacobi(a,num)
    #print(str(j) + ' == ' + str(b) + ' mod ' + str(num))
    if(not(j == b % num)):
        print('composite')
        return 0
    print('could be prime')

probprime(17)

    
