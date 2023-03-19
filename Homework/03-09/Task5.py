number = int(input("Enter an integer number: "))

count = 0
if number > 1:
    for i in range(1,number+1):
        if number%i == 0:
            count +=1
    if count == 2:
        print("The number is prime")
    else:
        print("The number is not prime") 

else:
    print("The number is not prime")