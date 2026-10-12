import random

def dice_roll():
    return random.randint(1, 6)

count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
for i in range(15):
    n = dice_roll()
    print(n, end=' ')
    count[n] += 1
print('\nFrequency:')
for i in count:
    print(i, ":", count[i])
