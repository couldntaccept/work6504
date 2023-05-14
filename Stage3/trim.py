def remove_after_equal(line):
    # Find the equal sign in the line and slice the string up to this position
    equal_pos = line.find('=')
    if equal_pos != -1:
        return line[:equal_pos].strip()
    else:
        return line.strip()

with open('result_6.txt', 'r') as f_in, open('result_trimmed.txt', 'w') as f_out:
    for line in f_in:
        modified_line = remove_after_equal(line)
        f_out.write(modified_line + '\n')
