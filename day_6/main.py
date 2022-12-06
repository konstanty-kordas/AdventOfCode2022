
with open('input.txt', 'r') as f:
    signal = f.read()

print(signal)

for i in range(len(signal)-14):
    if len(set(signal[i:i+14]))==14:
        print(i+14)
        break