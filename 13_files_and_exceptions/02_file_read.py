def main():
    infile = open('items_1.txt')

    file_contents = infile.read()

    infile.close()

    print(file_contents)


main()
