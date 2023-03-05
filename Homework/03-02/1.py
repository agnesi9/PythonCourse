
a = input("What is your age?")
b = input("Do you have a driver's license?")

c = int(a) > 17
d = b == "yes" or b == "Yes"

g = c and d

print(g)
print("You are able to drive: " + str(g))