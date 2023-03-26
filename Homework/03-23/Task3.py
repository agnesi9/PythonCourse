def palindrome(text:str):
    length=len(text)
    textr =''
    for i in range(length,0,-1):
        textr = textr + text[i-1]
    if str(textr)==text:
        return True
    else:
        return False
print(palindrome("madam"))


