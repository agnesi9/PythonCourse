#Write a function that takes a set as a parameter 
#and returns a new set that contains only the elements that are not divisible by 3.

s = {2,9,7,9,12}
set3 = set({})
for el in s:
    if el%3==0:
        set3.add(el)

print(set3)