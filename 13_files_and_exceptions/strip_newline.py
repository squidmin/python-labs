def main():
    infile = open('items_2.txt', 'r')

    line_1 = infile.readline()
    line_2 = infile.readline()
    line_3 = infile.readline()

    line_1 = line_1.rstrip('\n')
    line_2 = line_2.rstrip('\n')
    line_3 = line_3.rstrip('\n')

    infile.close()

    print(line_1)
    print(line_2)
    print(line_3)


main()
