file = open('text.txt')
# Read all the contents of file, si le colocamos un parámetro va leer hasta la línea que tenga esa longitud
#print(file.read(2))

# Read file line by line
#print(file.readline())
#print(file.readline())
#print(file.read())
#file.close()

# Using readline()
'''line = file.readline()

while line != '':
    print(line)
    line = file.readline()

file.close()'''

# Using readlines()
for line in file.readlines():
    if len(line) < 5:
        print(line)
file.close()