#Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped.


def swapped(tup:tuple):
    tup = list(tup)
    first = tup[0]
    last = tup[len(tup)-1]
    tup[0]=last
    tup[len(tup)-1]=first
    return tuple(tup)

print(swapped((2,7,4,3,7)))