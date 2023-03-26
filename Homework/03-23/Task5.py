def sumint(l:list,sum:int):
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if l[i]+l[j]==sum:
                print(str(l[i])+' '+str(l[j]))

sumint([2,4,5,8,3],6)
