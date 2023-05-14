def modify_line(line):
    # Find the first "-" in the line
    dash_pos = line.find('-')
    if dash_pos == -1:
        return line  # return the original line if there's no "-"

    # Split the line into the part before the "-" and the part after
    before_dash = line[:dash_pos].strip()
    after_dash = line[dash_pos:]

    # Check if there's only one pair of parentheses in the part before the dash
    if before_dash.count('(') == 1 and before_dash.count(')') == 1:
        # Duplicate the content in parentheses, add a comma, and wrap with another pair of parentheses
        before_dash = '(' + before_dash + ', ' + before_dash + ')'

    # Combine the modified part before the dash with the part after the dash
    return before_dash + ' ' + after_dash

with open('gorfy.txt', 'r') as f_in, open('output_gorfy.txt', 'w') as f_out:
    for line in f_in:
        modified_line = modify_line(line)
        f_out.write(modified_line)
