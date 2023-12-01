data = []
with open("input.txt") as f:
    data = f.readlines()
out = []
LUT = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for line in data:
    numbers = []
    first = [float('inf'),-1]
    last = [-1,-1]
    for i, num in enumerate(LUT):
        if num in line:
            f = line.index(num)
            # print(f)
            if f < first[0]:
                first = [f,i+1]
            l = line.rindex(num)
            if l > last[0]:
                last = [l,i+1]
    print(first, last)
    for i,character in enumerate(line):
        if character.isdigit():
            numbers.append((i,int(character)))
    print(numbers)
    if first[0]< numbers[0][0]:
        o1 = first[1]
    else:
        o1 = numbers[0][1]
    if last[0]>numbers[-1][0]:
        o2 = last[1]
    else:
        o2 = numbers[-1][1]
    out.append(o1 * 10 + o2)
print(out, sum(out))
