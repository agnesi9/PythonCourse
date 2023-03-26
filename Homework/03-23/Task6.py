def product(l:list):
    prod=1
    for el in l:
        prod = prod*el
    return prod
print(product([2,4,3]))