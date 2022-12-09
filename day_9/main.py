instructions = []
with open('input.txt', 'r') as f:
    for i in f.read().split('\n'):
        direction, steps = i.split()
        instructions.append((direction, int(steps)))

visited = set()
visited.add((0, 0))
knots = tuple([[0, 0] for i in range(10)])
# tail = [0, 0]
for i in instructions:
    for j in range(i[1]):
        if i[0] == "R":
            knots[0][0] += 1
        if i[0] == "U":
            knots[0][1] += 1
        if i[0] == "L":
            knots[0][0] -= 1
        if i[0] == "D":
            knots[0][1] -= 1
        
        for k in range(len(knots)-1):
            if (abs(knots[k][0]-knots[k+1][0]) > 1 or abs(knots[k][1]-knots[k+1][1]) > 1):
                correctX = True
                correctY = True

                # same y-axis
                if knots[k][1] == knots[k+1][1]:
                    correctY = False

                # same x-axis
                if knots[k][0] == knots[k+1][0]:
                    correctX = False

                if correctX:
                    if knots[k+1][0] > knots[k][0]:
                        knots[k+1][0] -= 1
                    else:
                        knots[k+1][0] += 1

                if correctY:
                    if knots[k+1][1] > knots[k][1]:
                        knots[k+1][1] -= 1
                    else:
                        knots[k+1][1] += 1
        
        visited.add((knots[k+1][0],knots[k+1][1]))
            # catch up

print(len(visited))
# print(sorted(list(visited)))