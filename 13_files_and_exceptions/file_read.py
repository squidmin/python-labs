def main():
    infile = open('items.txt')

    file_contents = infile.read()

    infile.close()

    print(file_contents)


main()
