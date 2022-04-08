def dividers_equal_to_sum_generator(start=2):
    """
    A function of a generator that calculates the numbers whose sum of divisors is equal to the number itself.
    :param start:The number from which The generator function starts calculating.
    :return:
    """
    while True:
        sum_dividers = sum([num for num in range(1, start) if start % num == 0])
        (yield sum_dividers) if sum_dividers == start else None
        start += 1


if __name__== '__main__':
    perfect_dividers_generator=dividers_equal_to_sum_generator()
    for perfect_divider_number in perfect_dividers_generator:
        print (perfect_divider_number)
