# Spell Check Starter
import re

# Load data files into lists

def main():
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWordsFull = loadWordsFromFile("data-files/AliceInWonderLand.txt")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" SPELL CHECK ASSIGNMENT MENU")
    print("1: Single Word Spell Check")
    print("2: Spell Check Alice In Wonderland")
    spellCheck = input("Enter Menu Selection: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    #Single word spell check
    if spellCheck == "1":
        print("Single Word Spell Check Selected. Please Choose Search Type")
        print("1: linear search")
        print("2: binary search")
        searchType = input("Enter Search Selection: ")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if searchType == "1":
            word = input("linear search choosen, please enter word: ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            arrayPosition = linearSearch(dictionary, word)
            if arrayPosition >= 0:
                print(word + " is in the dictionary at position " + str(arrayPosition))
                main()
            else:
                print(word + " is not in the dictionary")
                main()
        elif searchType == "2":
            word = input("binary search choosen, please enter word: ")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            arrayPosition = binarySearch(dictionary, word)
            if arrayPosition >= 0:
                print(word + " is in the dictionary at position " + str(arrayPosition))
                main()
            else:
                print(word + " is not in the dictionary")
                main()
        else:
            print("!!Invalid Input!!")
            main()

    #Alice in wonderland check
    if spellCheck == "2":
        print("Alice In Wonderlan Check Selected. Please Choose a Search Type:")
        print("1: linear search")
        print("2: binary search")
        searchType = input("Enter Search Selection: ")
        if searchType == "1":
            wordCount = 0
            for i in range(len(aliceWordsFull)):
                word = linearSearch(dictionary, aliceWordsFull[i])
                if word == -1: # not found in dictionary
                    print(aliceWordsFull[i])
                    wordCount+=1
            print("There were " + str(wordCount) + " missing words")
            main()
        elif searchType == "2":
            wordCount = 0
            for i in range(len(aliceWordsFull)):
                word = binarySearch(dictionary, aliceWordsFull[i])
                if word == -1: # not found in dictionary
                    print(aliceWordsFull[i])
                    wordCount+=1
            print("There were " + str(wordCount) + " missing words")
            main()
        else:
            print("!!Invalid Input!!")
            main()
    else:
        print("!!Invalid Input!!")
        main()

# end main()


def linearSearch(anArray, item):
    for i in range(len(anArray)):
        if anArray[i] == item:
            return i
    return -1

def binarySearch(anArray, item):
    li = 0
    ui = len(anArray) - 1
    
    while ui >= li:
        mi = (li + ui) // 2
        if anArray[mi] == item:
            return mi
        elif item < anArray[mi]:
            ui = mi - 1
        else:
            li = mi + 1
    return -1

def loadWordsFromFile(fileName):
    # Read file into an array of words
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    return re.findall(r"[\w]+", textData)

# Call main() to begin program
main()
