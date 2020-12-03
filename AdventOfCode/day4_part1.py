

numbers = []
target_number = 2020

with open('day1.txt', mode='r') as f:
    for line in f:
        line = line.rstrip('\n')
        line = int(line)
        numbers.append(line)
