elves = []
with open('input.txt','r') as f:
    temp = []
    for i in f.read().split('\n'):
        if i == '':
            elves.append(tuple(temp))
            temp=[]
            continue
        temp.append(int(i))
# print(elves)
sums = [sum(i) for i in elves]
sums.sort(reverse=True)
print(sum(sums[0:3]))