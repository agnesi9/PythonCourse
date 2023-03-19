list = []
while True:
    word = input("Enter a word: ")
    if word == "":
        break
    list.append(word)

amount = len(list)

count = 1
while count > 0:
    for i in range(0,amount-1):
            count = 0
            if list[i]>list[i+1]:
                list.insert(i,list[i+1])
                list.pop(i+2)
                count += 1

print(list)

