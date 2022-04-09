import functools
import itertools


def interleave(*iterables)->list:
    """
    A function that connects lists in the order of the values.
    :param iterables:A Tuple of list to merge.
    :return:A merge list of the  lists she get by the order of the values.
    """
    return list(functools.reduce(lambda first_item, second_item: first_item + second_item, [iterable for iterable in itertools.zip_longest(*iterables)]))


def interleave_generator(*iterables)->list:
    """
     A function that connects lists in the order of the values.
    :param iterables:A Tuple of list to merge.
    :return:A merge list of the  lists she get by the order of the values.
    """
    save_interleave_list=[]
    for iterable in itertools.zip_longest(*iterables):
        save_interleave_list += interleave(iterable)
        yield save_interleave_list


if __name__== '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    interleave_lists = interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
    for interleave_list in  interleave_lists:
        print(interleave_list)
