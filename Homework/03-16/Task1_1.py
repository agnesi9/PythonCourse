text = input("Enter a text: ")

for i in range(0,text.__len__()):
    char = text[i]
    amount = text.count(char)
    if amount > 0:
        print("Character " + char + " is used " + str(amount) + " times in a text")