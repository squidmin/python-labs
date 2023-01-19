def main():
    filename = input('Enter a filename: ')  # Enter the name of a non-existent file.
    try:
        infile = open('filename', 'r')
        contents = infile.read()
        print(contents)
        infile.close()
    except IOError:
        print('An error occurred trying to read the file', filename)


main()