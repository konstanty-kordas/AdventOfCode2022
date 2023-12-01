instructions = []
with open('input.txt', 'r') as f:
    for i in f.read().split('\n'):
        if i == 'noop':
            instructions.append(0)
        else:
            instructions.append(int(i.split()[1]))


x = 1
cycle = 0
# strength = 0
msg = ''
display = '\n'
# msg[2] = '#'
for i in instructions:
    opLen = 2
    if i == 0:
        opLen = 1
    for k in range(opLen):
        cycle += 1
        if abs((cycle % 40) -1- x) <= 1:
            msg += '#'
        else:
            msg += '.'
        # print("cycle: ", cycle%40)
        # print(x)
        # print(msg)
        if cycle % 40 == 0:
            # strength += cycle*x
            display += msg
            display += '\n'
            msg = ''
    # if cycle>=20:
    #     break 
    x += i

print(display)
# print(strength)
