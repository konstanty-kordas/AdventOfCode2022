from pprint import pprint


trees = []
with open('input.txt', 'r') as f:
    for i in f.read().split('\n'):
        trees.append([int(j) for j in i])
visible = [[0 for j in range(len(trees[i]))] for i in range(len(trees))]

# PART 1
# LEFT
for i in range(len(trees)):
    for j in range(len(trees)):
        if i == 0 or j == 0 or i == len(trees)-1 or j == len(trees)-1:
            visible[i][j] = 1
            continue
        if trees[i][j] > max(trees[i][:j]):
            visible[i][j] = 1


# RIGHT
for i in reversed(range(1, len(trees)-1)):
    for j in reversed(range(1, len(trees)-1)):
        if trees[i][j] > max(trees[i][j+1:]):
            visible[i][j] = 1

# UP
for i in range(1, len(trees)):
    for j in range(1, len(trees)):
        if trees[i][j] > max([trees[k][j] for k in range(i)]):
            visible[i][j] = 1

# DOWN
for i in reversed(range(1, len(trees)-1)):
    for j in reversed(range(1, len(trees)-1)):
        # print(i,j)
        # print([trees[k][j] for k in range(i+1, len(trees))])
        if trees[i][j] > max([trees[k][j] for k in range(i+1, len(trees))]):
            visible[i][j] = 1


# print(sum([sum(i) for i in visible]))
# pprint(visible)
pprint(trees)

scores = [[0 for j in range(len(trees[i]))] for i in range(len(trees))]
for i in range(1, len(trees)-1):
    for j in range(1, len(trees)-1):
        # if not (i==3 and j==2):
        #     continue

        right = 0
        left = 0
        up = 0
        down = 0

        # RIGHT
        for k in range(j+1, len(trees)):
            if trees[i][k] < trees[i][j]:
                right += 1
                continue
            if trees[i][k] == trees[i][j]:
                right += 1
                break
            else:
                right+=1
                break
        # DOWN
        for k in range(i+1, len(trees)):
            if trees[k][j] < trees[i][j]:
                down+=1
                continue
            if trees[k][j]==trees[i][j]:
                down+=1
                break
            else:
                down+=1
                break

        # LEFT
        for k in reversed(range(j)):
            if trees[i][k] < trees[i][j]:
                left+=1
                continue
            if trees[i][k] == trees[i][j]:
                left+=1
                break
            else:
                left+=1
                break
        
        #UP
        for k in reversed(range(i)):
            if trees[k][j] < trees[i][j]:
                up+=1
                continue
            if trees[k][j] == trees[i][j]:
                up+=1
                break
            else:
                up+=1
                break
        scores[i][j] = up*down*left*right
        # if i==1 and j==2:
        # print(up, left, right, down)
pprint(max([max(i) for i in scores]))


    
