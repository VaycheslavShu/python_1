import os
import sys


def CountText(text:str)->str:
    if len(text)%2==0:
        mid = len(text) // 2
        print(text[mid - 1:mid + 1])
    else:
        mid = len(text) // 2
        print(text[mid])


def main()->str:
    word = input("Введите слово: ")
    CountText(word)



if __name__ == "__main__":
    main()