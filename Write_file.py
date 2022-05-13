# De esta forma el archivo se abre y cierra además
with open('text.txt', 'r') as reader:
    # Guarda todo en una lista
    content = reader.readlines()
    a = reversed(content)
    # Para guardarlo en el mismo archivo
    with open('test.text', 'w') as writer:
        for line in a:
            writer.write(line)