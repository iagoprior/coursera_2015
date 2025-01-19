while True:
    line = input('Enter a text:')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done')