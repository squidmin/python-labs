def main():
    """Sums a range of integers."""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sum_1 = range_sum(numbers, 2, 5)
    print('The sum of items 2 through 5 is ' + str(sum_1) + '.')


def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)


main()
