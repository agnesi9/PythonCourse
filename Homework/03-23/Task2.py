def vowel(text:str):
    number = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
    return number
text = input("Enter a text: ")
print(vowel(text))

