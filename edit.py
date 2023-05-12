with open('data.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()
print(data)
print("'" + data[0].strip() + "'" + "\n")

for i, d in enumerate(data):
    data[i] = "'" + data[i].strip() + "\\" + "n" + " '" + "\n"

with open('data.txt', 'w') as file:
    file.writelines( data )
