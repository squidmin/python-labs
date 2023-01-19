def main():
    levels_file = open('levels.txt', 'r')
    line = levels_file.readline()
    while line != '':
        temperature = float(line)
        print(format(temperature, '.2f'))
        line = levels_file.readline()

    levels_file.close()


main()
