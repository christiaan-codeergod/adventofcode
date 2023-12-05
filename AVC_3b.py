import numpy as np
import re

with open("D:\\ChristiaanS\\Documents\\puzzle_input.txt") as f:
    input = f.read().splitlines()
finalResult = 0
lineLength = len(input[0])

def findSurroundingNumbers(i,j):
    all_numbers = []
    if i == 0:
        prevLine = []
    else:
        prevLine = input[i-1]
        all_numbers.extend(findNumbers(prevLine, j))
    if i == len(input)-1:
        nextLine = []
    else:
        nextLine = input[i+1]
        all_numbers.extend(findNumbers(nextLine, j))
    if j != 0:
        if input[i][j+1].isnumeric():
            all_numbers.append(int(findNextNumbers(input[i], j+1)))
    if j != lineLength-1:
        if input[i][j-1].isnumeric():
            all_numbers.append(int(findPrevNumbers(input[i], j-1)))
    return all_numbers
    
def findNumbers(inputString, middle):
    result = []
    if not inputString[middle].isnumeric():
        if middle != 0:
            if inputString[middle-1].isnumeric():
                result.append(int(findPrevNumbers(inputString, middle-1)))
        if middle != len(inputString)-1:
            if inputString[middle+1].isnumeric():
                result.append(int(findNextNumbers(inputString, middle+1)))
    else:
        if middle == 0:
                result.append(int(findPrevNumbers(inputString, middle) + findNextNumbers(inputString, middle+1)))
        else:
            result.append(int(findPrevNumbers(inputString, middle-1) + findNextNumbers(inputString, middle)))
    return result



def findPrevNumbers(inputString, position):
    if not inputString[position].isnumeric():
        return ''
    if position == 0:
        return inputString[position]
    return findPrevNumbers(inputString, position-1) + inputString[position]

def findNextNumbers(inputString, position):

    if not inputString[position].isnumeric():
        return ''
    if position == len(inputString)-1:
        return inputString[position]
    return inputString[position] + findNextNumbers(inputString, position+1)


for i in range(len(input)):
    line = input[i]
    for j in range(lineLength):
        char = line[j]
        if char == '*':
            numbers = findSurroundingNumbers(i,j)
            print(numbers)
            if len(numbers) == 2:
                finalResult += numbers[0] * numbers[1]
print(finalResult)