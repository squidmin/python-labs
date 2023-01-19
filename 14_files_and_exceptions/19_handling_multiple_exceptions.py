def main():
    """Demonstrates handling multiple exceptions."""
    total = 0.0

    try:
        infile = open('records_2.txt', 'r')
        for line in infile:
            amount = float(line)
            total += amount

        infile.close()

        print(format(total, ',.2f'))

    except IOError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file.')

    except Exception as ex:  # Aliasing
        print('An error occurred: ' + str(ex))

    else:  # Must appear after all 'except' clauses.
        print('Reached the else clause.')

    finally:  # Must appear after all the 'except' clauses, after any 'finally' clauses.
        print('Reached the \'finally\' clause.')


main()
