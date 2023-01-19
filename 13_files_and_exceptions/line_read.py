def main():
    infile = open('items_1.txt', 'r')

    line_1 = infile.readline()
    line_2 = infile.readline()
    line_3 = infile.readline()

    infile.close()

    print(line_1)
    print(line_2)
    print(line_3)


main()