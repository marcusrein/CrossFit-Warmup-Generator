from exercises import *
from droms import *
from metcons import *
from checks import *
from filters import *
import random


def get_cat_from_todays_wod(todays_wod, dictionary):
    todays_cat = []
    for w in todays_wod:
        for k, v in dictionary.items():
            if w == k:
                todays_cat.append(v['category'])
    return todays_cat


def get_possible_movements_from_mov_cat(mov_cat, dictionary):
    possible_warmups = []
    for cat in mov_cat:
        for k, v in dictionary.items():
            if cat in v['categories']:
                possible_warmups.append(k)
    return possible_warmups


def get_organized_tally_dict(possible_movements):
    """
    :param possible_movements: inputs todays possible DROMs, tallys them, sorts them, partially randomizes them if their
    values are equal, then sorts them againnn.
    :return: organized (partially random if equal) dictionary of todays possible DROMS
    """
    tally_of_movements = {}
    for w in possible_movements:
        if w in tally_of_movements:
            tally_of_movements[w] += 1
        else:
            tally_of_movements[w] = 1
    ordered_tally = {k: v for k, v in sorted(tally_of_movements.items(), key=lambda item: item[1], reverse=True)}
    ordered_tally_rand = ordered_tally
    ordered_tally_rand_list = list(ordered_tally_rand.items())
    random.shuffle(ordered_tally_rand_list)
    ordered_tally_rand_dict = dict(ordered_tally_rand_list)
    ordered_tally_rand_final = {k: v for k, v in
                                sorted(ordered_tally_rand_dict.items(), key=lambda item: item[1], reverse=True)}

    return ordered_tally_rand_final


def get_times_of_organized_tally_list(organized_tally, dictionary):
    """Puts times of organized warmup tally into a separate list"""
    tally_of_times = []
    for k, v in organized_tally.items():
        for k2, v2 in dictionary.items():
            if k == k2:
                tally_of_times.append(v2['time'])
    return tally_of_times


def get_sum_times_of_list(x):
    """Sums any list of ints"""
    sum_times = sum(x)
    return sum_times


def get_all_movement_times(todays_wod):
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
    if check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        kb_time += 5
        tough_gymnastics_time += 10
        print('TTT')
    elif check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        kb_time += 5
        print('TTF')
    elif check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        tough_gymnastics_time += 10
        print('TFT')
    elif check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        barbell_time += 10
        print('TFF')
    elif not check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        kb_time += 5
        tough_gymnastics_time += 10
        print('FTT')
    elif not check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        kb_time += 5
        print('FTF')
    elif not check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 8
        tough_gymnastics_time += 10
        print('FFT')
    elif not check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
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


def which_movements_are_barbell_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod"""
    barbell_movements_from_todays_wod = []

    for movement in todays_wod:
        for k in exercises.keys():
            if movement == k and exercises[k]['loaded'] == 'barbell':
                barbell_movements_from_todays_wod.append(movement)

    return barbell_movements_from_todays_wod

def which_movements_are_kb_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod"""
    kb_movements_from_todays_wod = []

    for movement in todays_wod:
        for k in exercises.keys():
            if movement == k and exercises[k]['loaded'] == 'kb':
                kb_movements_from_todays_wod.append(movement)

    return kb_movements_from_todays_wod





def get_metcon_reps(selected_metcon):
    metcon_reps = []
    y = metcons.get(selected_metcon)
    # z = selected_metcon[y]
    z = y.get('reps')
    final = random.choice(z)
    return final


def get_movements_compiled(todays_wod, todays_wod_toggles, dictionary, movement_time):
    """This is a function that compiles DROMS for viewing."""
    ##CLEANER##
    todays_wod = remove_none_from_todays_wod(todays_wod)

    ##CHECKS##
    has_kb_exercise = check_kb_exercise(todays_wod)
    has_barbell_exercise = check_barbell_exercise(todays_wod)
    has_tough_gymnastics = check_tough_gymnastics(todays_wod)

    ##GETTERS##
    mov_cat = get_cat_from_todays_wod(todays_wod, exercises)
    todays_possible_movements = get_possible_movements_from_mov_cat(mov_cat, dictionary)
    tally_organized_dict = get_organized_tally_dict(todays_possible_movements)
    tally_organized_times_list = get_times_of_organized_tally_list(tally_organized_dict, dictionary)
    tally_organized_times_sum = get_sum_times_of_list(tally_organized_times_list)
    all_warmup_times_pre_toggle = get_all_movement_times(todays_wod)
    prescribed_time = all_warmup_times_pre_toggle[str(movement_time)]
    all_warmup_times_plus_toggles = check_toggles_add_time(todays_wod, todays_wod_toggles, all_warmup_times_pre_toggle)
    selected_movements = pop_and_select(tally_organized_dict, tally_organized_times_list,
                                        tally_organized_times_sum, prescribed_time)

    return {'TODAYS WOD AND CHECKS: ''todays wod': todays_wod,
            'has kb exercise': has_kb_exercise,
            'has barbell exercise': has_barbell_exercise,
            'has_tough_gymnastics': has_tough_gymnastics, 'todays_wod_toggles': todays_wod_toggles,
            'ALL WARMUP TIMES PLUS TOGGLES ': all_warmup_times_plus_toggles,
            'CALCULATIONS: ''mov_cat': mov_cat,
            'todays possible movements': todays_possible_movements, 'TALLY ORGANIZED DICT': tally_organized_dict,
            'tally organized times list': tally_organized_times_list,
            'tally organized times sum': tally_organized_times_sum,
            'prescribed time': prescribed_time, 'SELECTED MOVEMENTS: ': selected_movements
            }