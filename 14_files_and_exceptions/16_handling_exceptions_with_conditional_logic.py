def main():
    num_1 = int(input('Enter an number: '))
    num_2 = int(input('Enter another number: '))

    """
    The following code can throw a ZeroDivisionError.
    """
    # result = num_1 / num_2
    # print(num_1, 'divided by', num_2, 'is', result)

    """
    The following code checks for division by zero to handle the division-by-zero scenario. 
    """
    if num_2 != 0:
        result = num_1 / num_2
        print(num_1, 'divided by', num_2, 'is', result)
    else:
        print('Cannot divide by zero.')


main()
