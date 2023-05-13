with open('merge.txt', 'r') as f_in:
    lines = f_in.readlines()

# Remove duplicates by converting the list to a set, then convert it back to a list
lines = list(set(lines))

with open('final_annotation.txt', 'w') as f_out:
    for line in lines:
        f_out.write(line)
