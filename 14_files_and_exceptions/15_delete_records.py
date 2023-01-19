import os


def main():
    found = False
    is_file_empty = False

    search = input('Which record do you want to delete? ')

    records_file = open('records.txt', 'r')
    temp_file = open('temp.txt', 'w')

    descr = records_file.readline()

    while descr != '':
        qty = float(records_file.readline())

        descr = descr.rstrip('\n')

        if descr != search:
            temp_file.write(descr + '\n')
            temp_file.write(str(qty) + '\n')
            found = True

        descr = records_file.readline()
        if descr == '':
            is_file_empty = True

    records_file.close()
    temp_file.close()

    os.remove('records.txt')
    os.rename('temp.txt', 'records.txt')

    if found or is_file_empty:
        print('The file has been updated.')
    else:
        print('That item was not found in the file.')


main()
