def max(liste):
    maximum = 0
    for i in range(len(liste) + 1):
        if maximum < liste[i]:
            maximum = liste[i]
    return maximum

max([1,4,3,1,3,7])
max([-1,-3,-4,-2,-6])