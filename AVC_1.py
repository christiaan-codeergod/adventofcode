import re

def findDigits(line):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    highest = [0,-1]
    lowest = [len(line) + 1, -1]
    for i in range(len(numbers)):
        position = line.find(numbers[i])
        positionHigh = line[::-1].find(numbers[i][::-1])
        if positionHigh != -1:
            positionHigh = len(line) - positionHigh
            if positionHigh > highest[0]:
                highest[0] = positionHigh
                highest[1] = (i+1)%9
                if highest[1] == 0:
                    highest[1] = 9
        if position != -1:
            if position < lowest[0]:
                lowest[0] = position
                lowest[1] = (i+1)%9
                if lowest[1] == 0:
                    lowest[1] = 9
    return [lowest[1], highest[1]]

f = open("D:\\ChristiaanS\\Documents\\puzzle_input.txt", "r")
input = f.readlines()
result = 0
for line in input:
    digits = findDigits(line)
    result += int(digits[0]) *10 + int(digits[len(digits)-1])
    print(digits)
print(result)


