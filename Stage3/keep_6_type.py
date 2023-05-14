# List of words to filter out
words_to_filter = ['LANGUAGE', 'TIME', 'NORP', 'QUANTITY', 'WORK_OF_ART', 'DATE', 'ORDINAL', 'PRODUCT', 'CARDINAL']

with open('result.txt', 'r') as f_in, open('result_6.txt', 'w') as f_out:
    for line in f_in:
        # Check if any of the words to filter is in the line
        if not any(word in line for word in words_to_filter):
            f_out.write(line)
