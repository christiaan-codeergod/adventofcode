f = open("D:\\ChristiaanS\\Documents\\puzzle_input.txt", "r")
input = f.readlines()
result = 0
for i in range(len(input)):
    line = input[i]
    line = line.split()
    number = 0
    largest = [0,0,0]
    for j in range(len(line)):
        word = line[j]
        if word.isnumeric():
            number = int(word)
        else:
            if "Game" not in word and ":" not in word:
                if "red" in word:
                    if number > largest[0]:
                        largest[0] = number
                elif  "green" in word:
                    if number > largest[1]:
                        largest[1] = number
                elif  "blue" in word:
                    if number > largest[2]:
                        largest[2] = number

    result += largest[0] * largest[1] * largest[2]
print(result)
