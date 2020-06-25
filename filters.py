from checks import *
from loading import *
import random



def pop_and_select(dictionary, organized_times_list, tally_organized_times_sum, prescribed_time):
    """
    dictionary = dict of ordered tally
    organized_times_list = list of times organized high to low
    tally_organized_times_sum = int sum of organized times list
    prescribed time = time alloted by  def get_all_movement_times
    return: selected list
    """
    x = tally_organized_times_sum

    pop_dict = dictionary.copy()
    pop_organized_time_list = organized_times_list.copy()

    while x > prescribed_time:
        pop_dict.popitem()
        pop_organized_time_list.pop()
        x = sum(pop_organized_time_list)
    return list(pop_dict.keys())


def barbell_loader(todays_wod):
    """Delivers a warmup for barbell movements"""
    x = '5 reps at 40%, 5 reps at 50%, 3 reps at 60%'
    if check_barbell_exercise(todays_wod):
        return x

def kettlebell_loader(todays_wod):
    """Delivers a warmup for kettlebell movements"""
    x = '10 Goatbag Swings, 10 Goblet Squats, 10 KB Swings'
    if check_kb_exercise(todays_wod):
        return x

def gymnastics_loader(todays_wod):
    """Delivers a warmup for gymnastics movements (COULD BE CHANGED TO CHECKING FOR MINUTES OF GYMNASTICS"""
    tough_gymnastics_warmups = []
    for wod in todays_wod:
        for k,v in loading.items():
            for thing in v['exercises']:
                if wod == thing:
                    tough_gymnastics_warmups.append(thing)
    return tough_gymnastics_warmups

breakpoint()
def gymnastics_rep_finder(tough_gymnastics_warmups):
    tough_gymnastics_warmup_reps = []
    for wu in tough_gymnastics_warmups:
        x = loading.get(wu['reps'])
        tough_gymnastics_warmup_reps.append(x)
    return tough_gymnastics_warmup_reps
        