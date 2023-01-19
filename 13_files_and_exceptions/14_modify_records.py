import os


def main():
    found = False

    search = input('Enter a description to search for: ')
    new_qty = int(input('Enter the new quantity for the record associated with description: ' + search + '\n'))

    records_file = open('records.txt', 'r')
    temp_file = open('temp.txt', 'w')

    descr = records_file.readline()
    while descr != '':
        qty = float(records_file.readline())
        descr = descr.rstrip('\n')

        if descr == search:
            temp_file.write(descr + '\n')
            temp_file.write(str(new_qty) + '\n')
            found = True
        else:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')

        descr = records_file.readline()

    records_file.close()
    temp_file.close()

    os.remove('records.txt')
    os.rename('temp.txt', 'records.txt')

    if found:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')


main()
