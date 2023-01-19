def main():
    another = 'y'
    records_file = open('records.txt', 'a')
    while another == 'y' or another == 'Y':
        print('Enter the following records data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        records_file.write(descr + '\n')
        records_file.write(str(qty) + '\n')

        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    records_file.close()
    print('Data appended to records.txt.')


main()
