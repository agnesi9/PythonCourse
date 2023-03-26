def evens(li:list):
    lieven =[]
    for element in li:
        if element%2==0:
            lieven.append(element)
    return lieven
print(evens([1,2,3,4,5,6,6,6]))



