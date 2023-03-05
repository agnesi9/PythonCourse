a = input("Enter a year for a program to check if it is a leap year")
b = ((not bool(int(a)%4)) and bool(int(a)%100)) or (not bool(int(a)%400))
print("Leap year: " + str(b))