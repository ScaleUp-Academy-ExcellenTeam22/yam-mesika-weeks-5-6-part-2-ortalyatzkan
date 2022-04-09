from contextlib import contextmanager
import time


@contextmanager
def open_file_decorator(file_to_open:str,mode:str):
    """
    A decorator function for safe opening of the file.
    :param file_to_open:The path to open a file.
    :param mode:Mode for opening a file.
    :return: file open.
    """
    file_open = open(file_to_open,mode)
    yield file_open
    file_open.close()


def search_word(words:[list,set],word_to_search:str)->float:
    """
    A function that get a list or set and searches in it a word 1000 times and returns the average search time.
    :param words:List or set to search within them.
    :param word_to_search:A word to search.
    :return:Average time to search for a word.
    """
    number_of_times = 1000
    start_time = time.time()
    number_of_searches = 0
    while number_of_searches < number_of_times:
        if_in_list = word_to_search in words
        number_of_searches += 1
    end_time = time.time()
    return (end_time - start_time)/1000


def open_and_search_word()->None:
    """
    A function that opens a file of words and creates a list and set of words within it.
    Then it calculates how long on average it takes search within each of them a word and prints the time.
    :return: Does not return anything (None).
    """
    with open_file_decorator("C:\\Users\\user\\Desktop\\Notebooks-master\\week06\\resources\\words.txt", 'r') as fileWord:
        words_list = fileWord.read().split()
        words_set = set(words_list)
        print("{} seconds.".format(search_word(words_list,"zwitterion")))
        print("{} seconds.".format(search_word(words_set,"zwitterion")))


if __name__== '__main__':
    open_and_search_word()
