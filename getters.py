from exercises_dataset import *
from warmups_dataset import *
from checks import *
import random

def get_cat_from_todays_wod(todays_wod):
    todays_cat = []
    for w in todays_wod:
        for k, v in exercises.items():
            if w == k:
                todays_cat.append(v['category'])
    return todays_cat


def get_possible_droms_from_mov_cat(mov_cat):
    possible_warmups = []
    for cat in mov_cat:
        for k, v in warmups.items():
            if cat in v['categories']:
                possible_warmups.append(k)
    return possible_warmups


def get_organized_drom_tally_dict(todays_possible_droms):
    """

    :param todays_possible_droms: inputs todays possible DROMs, tallys them, sorts them, partially randomizes them if their
    values are equal, then sorts them again.
    :return: organized (partially random if equal) dictionary of todays possible DROMS
    """
    tally_of_warmups = {}
    for w in todays_possible_droms:
        if w in tally_of_warmups:
            tally_of_warmups[w] += 1
        else:
            tally_of_warmups[w] = 1
    ordered_tally = {k: v for k, v in sorted(tally_of_warmups.items(), key=lambda item: item[1], reverse=True)}
    ordered_tally_rand = ordered_tally
    ordered_tally_rand_list = list(ordered_tally_rand.items())
    random.shuffle(ordered_tally_rand_list)
    ordered_tally_rand_dict = dict(ordered_tally_rand_list)
    ordered_tally_rand_final = {k: v for k, v in sorted(ordered_tally_rand_dict.items(), key=lambda item: item[1], reverse=True)}


    # breakpoint()
    return ordered_tally_rand_final



# def get_rand_organized_drom_tally_dict(drom_tally_organized_dict):
#     """
#     :param drom_tally_organized_dict: has dict to partially randomize. if there are equal values in tally, this func
#     randomizes the grouping
#     :return: partially randomized dict for popping filter in the future
#     """
#
#     ## If the values of multiple k,v pairs equal eachother, then make a new dicitonary of those key value pairs. Do that
#     ## repeatedly until done. Randomize the mini dictionaries. Then combine the multiple dicitonaries into one big dictionary.
#
#     temp_dict_1 = {}
#     temp_dict_2 = {}
#     temp_dict_3 = {}
#     temp_dict_4 = {}
#     temp_dict_5 = {}
#     temp_dict_6 = {}
#     temp_dict_7 = {}
#     temp_dict_8 = {}
#     temp_dict_9 = {}
#     temp_dict_10 = {}
#
#
#     for k,v in drom_tally_organized_dict.items():
#         temp_v = copy.copy(v)
#         if v == temp_v:



    rand_organized_drom_tally_dict = {}



def get_times_of_organized_drom_tally_list(ordered_tally):
    """Puts times of organized warmup tally into a separate list"""
    tally_of_warmups_times = []
    for k, v in ordered_tally.items():
        for k2, v2 in warmups.items():
            if k == k2:
                tally_of_warmups_times.append(v2['time'])
    return tally_of_warmups_times


def get_sum_times_of_list(
        x):  ###ENDED CODING HERE. STARTING TO WORK ON FIGURING OUT HOW TO GET IDEAL TIME FOR WARMUP... ALSO TOTAL TIME... WRITE THIS OUT ON PAPER BEFORE GOING FARTHER
    """Sums any list of numbers"""
    sum_times = sum(x)
    return sum_times


def get_all_warmup_times(todays_wod, intensity):

    metcon_time = 0
    drom_time = 0

    gymnastics_time = 0
    barbell_time = 0
    kb_time = 0

    tough_gymnastics_time = 0

    focused_gymnastics_time = 0
    focused_barbell_time = 0
    focused_kb_time = 0

    ## LOW GYMNASTICS ##
    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        kb_time += 5
        tough_gymnastics_time += 10
        print('TTT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        kb_time += 5
        print('TTF')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        tough_gymnastics_time += 10
        print('TFT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        print('TFF')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 8
        kb_time += 5
        tough_gymnastics_time += 10
        print('FTT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 8
        kb_time += 5
        print('FTF')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 8
        tough_gymnastics_time += 10
        print('FFT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 8
        print('FFF')

    all_warmup_time = (
            metcon_time + drom_time + gymnastics_time + barbell_time + kb_time + focused_gymnastics_time + focused_barbell_time + focused_kb_time)

    all_warmup_times_pre_toggle = {'all_warmup_time': all_warmup_time, 'metcon_time': metcon_time,
                                   'drom_time': drom_time,
                                   'gymanstics_time': gymnastics_time, 'barbell_time': barbell_time, 'kb_time': kb_time,
                                   'focused_gymanstics_time': focused_gymnastics_time,
                                   'focused_barbell_time': focused_barbell_time,
                                   'focused_kb_time': focused_kb_time
                                   }
    return all_warmup_times_pre_toggle
