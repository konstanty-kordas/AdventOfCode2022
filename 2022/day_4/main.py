overlapping = 0
with open('input.txt','r') as f:
    temp = []
    for i in f.readlines():
        elf1, elf2 = i.split(',')
        start1, end1 = [int(k) for k in elf1.split('-')]
        start2, end2 = [int(k) for k in elf2.split('-')]
        # # break
        if (start1 <= start2)  and not (end1 < start2):
            print(elf1, elf2)

            overlapping+=1
        else:
             if (start2 <= start1) and not (end2 < start1):
                # print(elf1, elf2)   
                overlapping+=1
print(overlapping)
        
            