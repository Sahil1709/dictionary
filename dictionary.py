import json
import difflib
from difflib import get_close_matches 

ans = "n"
while ans == "n":
    word = input("Enter word to search :")
    word = word.lower()
    file = json.load(open("data.json","r"))
    close_match = get_close_matches(word,file.keys())
    if type(close_match) == list:
            print(close_match)
            index = int(input("Enter Index:"))
            if index > len(close_match) - 1:
                print("Wrong index typed")
            else: 
                print(f"Do u wanted to type {close_match[index]} !")
                yesOrNo = input("(y/n) :")
                yesOrNo = yesOrNo.lower()
                if yesOrNo == "y":
                    word = close_match[index]
                elif yesOrNo == "n":
                    word = "usdfhyurewygrt"
                else:
                    print("u have to enter y or n !")
    else:
        word = close_match
    if word in file:
        output = file[word]
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(file[word])
    else:
        print("Word not found")
    user_ans = input("Are you done y/n :")
    user_ans = user_ans.lower()
    if user_ans == "n" or user_ans == "y":
        ans = user_ans
    else:
        print("I'm guessing u typed y !")
        ans = "y"

