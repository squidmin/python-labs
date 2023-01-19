def main():
    try:
        integer_amount = int(input('Enter an integer amount: '))
        float_amount = float(input('Enter a float amount: '))
        result = integer_amount * float_amount
        print('Result: ', format(result, ',.2f'), sep='')
    except ValueError:
        print('ERROR: Input must be valid numeric data.')


main()
