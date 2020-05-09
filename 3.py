def count_vowels(x):
    y = 0
    for i in x:
        if(i=="a" or i=="i" or i=="u" or i=="e" or i=="o"):
            y = y+1

    print(y)
count_vowels("sahrul kais")