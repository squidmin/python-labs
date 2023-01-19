def main():
    infile = open('numbers.txt', 'r')

    num_1 = int(infile.readline())
    num_2 = int(infile.readline())
    num_3 = int(infile.readline())

    infile.close()

    total = num_1 + num_2 + num_3

    print('Numbers::', num_1, num_2, num_3)
    print('Total:', total)


main()
