import functools
import itertools


def interleave(*iterables):
    return list(functools.reduce(lambda x, y: x + y, [iterable for iterable in itertools.zip_longest(*iterables)]))

def interleave_generator(*iterables):
    x=[]
    for iterable in itertools.zip_longest(*iterables):
        x+=interleave(iterable)
        yield x

if __name__== '__main__':
    print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    interleave_f=interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
    for i in  interleave_f:
        print(i)
