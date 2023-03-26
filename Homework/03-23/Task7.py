def dicteven(d:dict):
    for key in d:
        if d.get(key)%2==0:
            print(key)
dicteven({'num1':2,'num2':4, 'num3':5,'num4':8})
