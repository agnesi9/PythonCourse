number = int(input("Enter a number to find all its factors: "))

if number > 0:
    for i in range(1,number+1):
        if number%i == 0:
            print(i)

if number < 0:
    for i in range(-1, number-1,-1):
        if number%i == 0:
            print(i)