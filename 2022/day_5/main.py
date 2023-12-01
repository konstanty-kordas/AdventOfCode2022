crates = {}
commands = []
with open('input.txt', 'r') as f:
    comms = False
    prepped = False
    for i in f.readlines():
        if not prepped:
            for k in range(len(i)//4):
                crates[k+1] = [] #stack
            prepped = True
        if comms:
            if i.strip()=='':
                continue
            # print(i)
            # print()
            c = i.strip().split(" ")
            # print(c)
            # break
            commands.append((int(c[1]), int(c[3]), int(c[5])))
            continue
        if (i[1]=='1'):
            comms=True
            for k in crates:
                crates[k] = (crates[k][::-1])
            # print(crates)
            continue
        for z in range(len(crates)):
            crate = i[z*4+1]
            if crate!=' ':
                crates[z+1].append(crate)

# print(commands)
for k in commands:
    how_many, source, target = k
    temp = []
    for i in range(how_many):
        if len(crates[source])!=0:
            temp.append(crates[source].pop())
    temp = temp[::-1]
    for t in temp:
        crates[target].append(t)
# print(crates)
for k in crates:
    print(crates[k][-1], end='')