def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max
list1 = list(map(int,input().Split()))
print("Largest element is:myMax(list)")