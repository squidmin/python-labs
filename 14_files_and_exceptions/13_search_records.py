def main():
    """Searches for a record from the file 'records.txt'."""
    found = False
    search = input('Enter a description to search for: ')
    records_file = open('records.txt', 'r')
    descr = records_file.readline()

    while descr != '':
        qty = float(records_file.readline())
        descr = descr.rstrip('\n')
        if descr == search:
            print('Description:', descr)
            print('Quantity:', qty)
            print()
            found = True

        descr = records_file.readline()

    records_file.close()

    if not found:
        print('That item was not found in the file.')


main()
