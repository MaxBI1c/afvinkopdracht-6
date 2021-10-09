#import random
#def lotery_numbers():
#digit1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#digit2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#digit3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#digit4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#digit5 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#digit6 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#digit7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#main():
 #   lotery_numbers()
#main:
import random
i = 1
l = []
while i <= 7:
    i = i + 1
    x = random.randint(0,9)
    l.append(x)

print(l)
for position in l:
    print(position)
