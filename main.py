import string
def printPowerSet(set, SetSize):
    PowerSetSize = (int)(2**SetSize)
    outer = 0
    inner = 0
    for outer in range(0, PowerSetSize):
        for inner in range(0,SetSize):
            if(outer &(1 << inner) > 0):
                print(set[inner], end="")
        print("")
size = int(input("Enter array size:"))
set = []
for i in range(0, size):
    n = input("Enter element")
    set.append(n)
printPowerSet(set,len(set))
