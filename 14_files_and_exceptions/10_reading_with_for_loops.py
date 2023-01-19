def main():
    levels_file = open('levels.txt', 'r')
    for line in levels_file:
        temperature = float(line)
        print(format(temperature, '.2f'))

    levels_file.close()


main()
