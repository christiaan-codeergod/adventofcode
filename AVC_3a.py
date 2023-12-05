import numpy as np
import re

with open("D:\\ChristiaanS\\Documents\\puzzle_input.txt") as f:
    input = f.read().splitlines()
result = 0
data = np.zeros((len(input), len(input[0])-1))
for i in range(len(input)):
    line = input[i]
    line = line.split(".")
    prevline = []
    nextLine = []
    if i != 0:
        prevline = input[i-1]
        prevline = prevline.split(".")
    if len(input) > i+1:
        nextLine = input[i+1]
        nextLine = nextLine.split(".")

    #prep previous line
    counter = 0
    previousChars = []
    for j in range(len(prevline)):
        word = prevline[j]
        if len(word) > 0:
            if not word.isnumeric():
                for k in range(len(word)):
                    if not word[k].isnumeric():
                        previousChars.append(counter+k)
        counter += len(word) + 1

    #prep next line
    counter = 0
    nextChars = []
    for j in range(len(nextLine)):
        word = nextLine[j]
        if len(word) > 0:
            if not word.isnumeric():
                for k in range(len(word)):
                    if not word[k].isnumeric():
                        nextChars.append(counter+k)
        counter += len(word) + 1
    counter = 0

    #read this line
    for j in range(len(line)):
        
        word = line[j]
        if len(word) > 0:
            if word.isnumeric():
                for k in range(counter-1, counter + len(word)+1):
                    if k in nextChars or k in previousChars:
                        result += int(word)
                        break
            else:
                if len(word) > 1:
                    if any(char.isdigit() for char in word):
                        result += sum(map(int, re.findall(r'\d+', word)))
        counter += len(word) + 1
print(result)
