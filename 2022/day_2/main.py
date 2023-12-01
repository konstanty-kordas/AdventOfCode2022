rounds = []
with open('input.txt', 'r') as f:
    for i in f.readlines():
        rounds.append([a for a in i.split()])

vp = 0
# for opponent, mine in rounds:
#     if opponent=='A':
#         if mine=='X':
#             vp+=1+3
#         if mine=='Y':
#             vp+=2+6
#         if mine=='Z':
#             vp+=3+0
#     if opponent=='B':
#         if mine=='X':
#             vp+=1+0
#         if mine=='Y':
#             vp+=2+3
#         if mine=='Z':
#             vp+=3+6
#     if opponent=='C':
#         if mine=='X':
#             vp+=1+6
#         if mine=='Y':
#             vp+=2+0
#         if mine=='Z':
#             vp+=3+3

for opponent, mine in rounds:
    if opponent == 'A':
        if mine == 'X':
            vp += 3+0
        if mine == 'Y':
            vp += 1+3
        if mine == 'Z':
            vp += 2+6
    if opponent == 'B':
        if mine == 'X':
            vp += 1+0
        if mine == 'Y':
            vp += 2+3            
        if mine == 'Z':
            vp += 3+6
    if opponent == 'C':
        if mine == 'X':
            vp += 2+0
        if mine == 'Y':
            vp += 3+3
        if mine == 'Z':
            vp += 1+6


print(vp)
