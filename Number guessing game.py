import random

val=random.randint(1,100)
count=0
while True:
    a=int(input('Enter a number between 1 to 100: '))
    count+=1
    if a<val:
        print('Think big')
    elif a>val:
        print('Think less number')
    else:
        print('You cracked number')
        break
print(f'You took {count} attempts to crack the number')