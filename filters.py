from checks import *
from gymnastics_warmups import *
import random


def filter_pop_and_select(dictionary, organized_times_list, tally_organized_times_sum, prescribed_time):
    """
    This is the POP FILTER. Describe better in upcoming update.

    dictionary = dict of ordered tally
    organized_times_list = list of times organized high to low
    tally_organized_times_sum = int sum of organized times list
    prescribed time = time alloted by  def get_all_movement_times
    return: selected list
    """
    x = tally_organized_times_sum

    popped_items = []

    pop_dict = dictionary.copy()
    pop_organized_time_list = organized_times_list.copy()

    while x > prescribed_time:
        popped_items.append(pop_dict.popitem())
        pop_organized_time_list.pop()
        x = sum(pop_organized_time_list)

    print('pooper',popped_items)

    return list(pop_dict.keys()), popped_items
