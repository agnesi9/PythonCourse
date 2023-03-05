a,b = input("Enter 2 integers: ").split()
c = not bool(int(a)%2)
d = not bool(int(b)%2)

y = c and d
z = c or d

print("Both numbers are even: "+str(y))
print("At least one number is even: "+str(z))
