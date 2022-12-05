rucksacks = []
rucksacks2 = []
with open('input.txt','r') as f:
    temp = []
    for i in f.readlines():
        a = i
        a = a[:-1]
        rucksacks.append( (a[0:len(a)//2], a[len(a)//2:]))
        rucksacks2.append(a)
    
def com_Letters(strings):
    print(strings)
    return set.intersection(*map(set,strings))

def getPriotiry(s):
    x = ord(s)
    if x>=97:
        x-=96
    else:
        x-=38

    print(x)
    return x

total = 0
for i in range(0,len(rucksacks2),3):
    print(i)
    total+=getPriotiry(com_Letters((rucksacks2[i],rucksacks2[i+1],rucksacks2[i+2])).pop())
print(total)