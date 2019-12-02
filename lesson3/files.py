with open('referat.txt', 'r') as f:
    file_contents = f.read()

print(len(file_contents)) #1509

print(len(file_contents.split())) #163

with open('referat2.txt', 'w') as f:
    f.write(file_contents.replace('.', '!'))