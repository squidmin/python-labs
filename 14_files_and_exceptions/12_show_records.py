def main():
    records_file = open('records.txt', 'r')
    descr = records_file.readline()
    while descr != '':
        qty = float(records_file.readline())
        descr = descr.rstrip('\n')

        print('Description:', descr)
        print('Quantity:', qty)

        descr = records_file.readline()

    records_file.close()


main()
