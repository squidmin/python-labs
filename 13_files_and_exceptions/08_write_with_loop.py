def main():
    num_levels = int(input('How many levels? '))
    levels_file = open('levels.txt', 'w')
    for count in range(1, num_levels + 1):
        temperature = input('Enter the temperature in level #' + str(count) + ': ')
        levels_file.write(str(temperature) + '\n')
    levels_file.close()
    print('Data written to levels.txt.')


main()
