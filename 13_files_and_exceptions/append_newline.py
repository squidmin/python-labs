def main():
    print('Enter some items as strings.')
    item_1 = input('Item #1: ')
    item_2 = input('Item #2: ')
    item_3 = input('Item #3: ')

    input_file = open('items_2.txt', 'w')

    input_file.write(item_1 + '\n')
    input_file.write(item_2 + '\n')
    input_file.write(item_3 + '\n')

    input_file.close()
    print('Items were written to items_2.txt.')


main()