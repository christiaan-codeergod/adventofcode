from itertools import groupby
with open("D:\\ChristiaanS\\Documents\\puzzle_input.txt") as f:
    input = f.read().splitlines()
result = 0
seeds = input[0].split()[1:]
seeds = list(map(int, seeds))
newSeeds = []
maxSeeds = []
for i in range(0,len(seeds),2):
    newSeeds.append(seeds[i])
    maxSeeds.append(seeds[i]+seeds[i+1]-1)
index = 2
input = [list(g) for k, g in groupby(input, key=bool) if k]
input = input[1:]
newSeeds.sort()
maxSeeds.sort()

def partition_range(start, end, rules):
    prev_seed = start
    ranges = []
    changes = []
    for rule in rules:
        destination,source,rangeLength = rule
        if source > end:
            break
        elif source > prev_seed:
            ranges.append([prev_seed, source-1])
            changes.append(0)
            ranges.append([source, min(end, source + rangeLength - 1)])
            changes.append(destination-source)
            prev_seed = min(end, source + rangeLength - 1)+1
        elif source + rangeLength - 1 >= start:
            ranges.append([prev_seed, min(end, source + rangeLength - 1)])
            changes.append(destination-source)
            prev_seed = min(end, source + rangeLength - 1)+1
    if prev_seed < end:
        ranges.append([prev_seed, end])
        changes.append(0)
    return ranges, changes



def map_seeds(rules, newSeeds, maxSeeds):
    finalSeeds = []
    finalMaxSeeds = []
    for i in range(len(rules)):
            rule = rules[i]
            rule = rule.split()
            rule = [int(el) for el in rule]
            rules[i] = rule
    rules.sort(key=lambda x: int(x[1]))
    for i in range(len(newSeeds)):
        seed = newSeeds[i]
        highestSeed = maxSeeds[i]
        ranges, changes = partition_range(seed, highestSeed, rules)
        for j in range(len(ranges)):
            finalSeeds.append(ranges[j][0]+changes[j])
            finalMaxSeeds.append(ranges[j][1]+changes[j])
    return finalSeeds, finalMaxSeeds
        
for rules in input:
    newSeeds, maxSeeds = map_seeds(rules[1:], newSeeds, maxSeeds)

print(min(newSeeds))