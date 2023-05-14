def extract_numbers(line):
    # Extract the numbers after the first two parentheses and before the first right parenthesis
    start = line.find('((') + 2
    end = line.find(')', start)
    numbers = line[start:end].split(',')
    return int(numbers[0]), int(numbers[1])

with open('dups_removed.txt', 'r') as f:
    lines = f.readlines()

# Sort the lines based on the first digit
lines.sort(key=extract_numbers)

with open('dups_removed_sorted.txt', 'w') as f:
    for line in lines:
        f.write(line)