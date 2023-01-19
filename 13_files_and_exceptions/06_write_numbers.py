def main():
    outfile = open('numbers.txt', 'w')

    num_1 = int(input('Enter a number: '))
    num_2 = int(input('Enter a number: '))
    num_3 = int(input('Enter a number: '))

    outfile.write(str(num_1) + '\n')
    outfile.write(str(num_2) + '\n')
    outfile.write(str(num_3) + '\n')

    outfile.close()
    print('Data written to numbers.txt.')


main()
