def dividers_equal_to_sum_generator(size_of_dish=2)->int:
    """
    A function of a generator that calculates the numbers whose sum of divisors is equal to the number itself.
    :param size_of_dish:The number from which The generator function starts calculating.
    :return:Perfect number for division.
    """
    while True:
        sum_dividers = sum([divider for divider in range(1, size_of_dish) if size_of_dish % divider == 0])
        (yield sum_dividers) if sum_dividers == size_of_dish else None
        size_of_dish += 1


if __name__== '__main__':
    perfect_dividers_generator=dividers_equal_to_sum_generator()
    for perfect_divider_number in perfect_dividers_generator:
        print (perfect_divider_number)
