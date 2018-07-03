# SUBSETSUM Solver
# Gegeben: Eine Menge von Werten M; eine Zahl Z
# Gesucht: Teilmenge von M, sodass die Summe gleich Z ist


def subsetsum(array, num):
    if num == 0:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:], (num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:], num)


print(subsetsum([4, 12, 4, 2, 8], 14))
subset1 = subsetsum([4, 23, 12, 97, 13, 21, 95, 54, 32, 12, 4, 2, 8], 90)
print(str(subset1))
print(sum(subset1))

