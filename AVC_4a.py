import numpy as np
with open("D:\\ChristiaanS\\Documents\\puzzle_input.txt") as f:
    input = f.read().splitlines()
result = 0

results = np.ones(len(input))*-1

def calculateResult(index):
    line = input[index]
    line = line.split()
    
    readWinning = False
    readNumbers = False
    winningNumbers = []
    numbers = []
    for item in line:
        if ":" in item:
            readWinning = True
        elif "|" in item:
            readWinning = False
            readNumbers = True
        elif readWinning:
            winningNumbers.append(int(item))
        elif readNumbers:
            numbers.append(int(item))
    tempresult = 1
    wins = 0
    for number in numbers:
        if number in winningNumbers:
            wins += 1
            if index == len(input) - 1:
                return tempresult
            if results[index + wins] != -1:
                tempresult += results[index + wins]
            else:
                tempresult += calculateResult(index + wins)
    results[index] = tempresult
    return tempresult

result = sum([calculateResult(i) for i in range(len(input))])

print(result)