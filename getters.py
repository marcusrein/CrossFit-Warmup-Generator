from exercises import *
from droms import *
from metcons import *
from checks import *
from filters import *
from barbell_warmups import *
import re
import string
import random
from collections import defaultdict


def convert(s):
    # initialization of string to ""
    new = ""
    # traverse in the string
    for x in s:
        new += x
        # return string
    return new


def get_cat_from_todays_wod(todays_wod, dictionary):
    """Gets todays wod and finds the categories associated with a supplied dictionary"""
    todays_cat_with_dupes = []
    todays_cat = []
    for w in todays_wod:
        for k, v in dictionary.items():
            if w == k:
                x = v.get("category")
                for item in x:
                    todays_cat_with_dupes.append(item)
    # Cleans the duplicates:
    for i in todays_cat_with_dupes:
        if i not in todays_cat:
            todays_cat.append(i)
    return list(todays_cat)


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


def get_all_movement_times(todays_wod, tough_exercises):
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
        drom_time += 10
        barbell_time += 10
        kb_time += 5
        tough_gymnastics_time += 10
    elif check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10
        barbell_time += 10
        kb_time += 5
    elif check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10
        barbell_time += 10
        tough_gymnastics_time += 10
    elif check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10
        barbell_time += 10
    elif not check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10
        kb_time += 5
        tough_gymnastics_time += 10
    elif not check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10
        kb_time += 5
    elif not check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10
        tough_gymnastics_time += 10
    elif not check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 10

    if len(tough_exercises) == 1:
        drom_time += 2

    if len(tough_exercises) > 1:
        drom_time += 4

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


def which_movements_are_tough_gymnastics_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod"""
    tough_gymnastics_movements_from_todays_wod = []

    for x in todays_wod:
        if x == 'pull up' or x == 'pistol' or x == 'pistols' or x == 'handstand pushup' or x == 'handstand walk' \
                or x == 'kipping pull up' or x == 'ring muscle up' or x == 'bar muscle up':
            tough_gymnastics_movements_from_todays_wod.append(x.title())
    return tough_gymnastics_movements_from_todays_wod


def get_metcon_reps(selected_metcon):
    if selected_metcon:
        y = metcons.get(selected_metcon)
        z = y.get('reps')
        final = random.choice(z)
    else:
        final = ''
    return final


def get_reps(selected_movements, tough_exercises, dictionary):
    reps_big_list = []
    reps_chosen = []

    for movement in selected_movements:
        reps_big_list.append(dictionary.get(movement)['reps'])

    if len(tough_exercises) == 0:
        for x in reps_big_list:
            y = x[0]
            reps_chosen.append(y)
    elif len(tough_exercises) == 1:
        for x in reps_big_list:
            y = x[1]
            reps_chosen.append(y)
    elif len(tough_exercises) >= 2:
        for x in reps_big_list:
            y = x[2]
            reps_chosen.append(y)
    return reps_chosen


def get_selected_movements_addendum_droms(todays_wod, selected_movements, selected_metcon):
    """Adds dependencies. E.G. if air squats is in todays wod and not in selected movements, add airsquats
    to addendum (which will be added to selected movements for DROMS"""
    addendum = []
    # breakpoint()

    if 'push up' in todays_wod and 'push ups' not in selected_movements:
        addendum.append('push ups')
        # print('zxcv')

    if 'burpee' in todays_wod and 'burpees' not in selected_movements:
        addendum.append('burpees')
        # print('oijiojoij')

    if 'pull up' in todays_wod and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        # print('nnnnaaa')

    if any('squat' in wod for wod in todays_wod) and 'air squats' not in selected_movements:
        addendum.append('air squats')
        # print('gaaaaaaaa')

    if any('lunge' in wod for wod in todays_wod) and 'walking lunges' not in selected_movements:
        addendum.append('walking lunges')
        # print('feeee')

    if any('press' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        addendum.append('thoracic bridges')
        # print('foooo')
    if any('jerk' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        addendum.append('thoracic bridges')
        # print('fiiii')
    if any('snatch' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        addendum.append('thoracic bridges')
        # print('moo')
    if any('overhead' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        addendum.append('thoracic bridges')
        print('poooop')

    if any('squat' in wod for wod in todays_wod) and 'banded side steps' not in selected_movements:
        addendum.append('banded side steps')
        # print('asss')
    if any('clean' in wod for wod in todays_wod) and 'banded side steps' not in selected_movements:
        addendum.append('banded side steps')
        # print('asss')
    if any('snatch' in wod for wod in todays_wod) and 'banded side steps' not in selected_movements:
        addendum.append('banded side steps')
        # print('asss')
    if any('swing' in wod for wod in todays_wod) and 'banded side steps' not in selected_movements:
        addendum.append('banded side steps')
        # print('asss')
    if any('lunge' in wod for wod in todays_wod) and 'banded side steps' not in selected_movements:
        addendum.append('banded side steps')
        # print('asss')

    if any('turkish' in wod for wod in todays_wod) and 'thoracic bridges' \
            not in selected_movements:
        addendum.append('thoracic bridges')
        # print('goo')

    return addendum


def get_ordered_drom_list(selected_droms):
    ordered_drom_list = []

    for drom in selected_droms:
        for k, v in droms_dict.items():
            if drom == k:
                if v['rpe'] == 3:
                    ordered_drom_list.append(drom)

    for drom in selected_droms:
        for k2, v2 in droms_dict.items():
            if drom == k2:
                if v2['rpe'] == 2:
                    ordered_drom_list.insert(0, drom)

    for drom in selected_droms:
        for k2, v2 in droms_dict.items():
            if drom == k2:
                if v2['rpe'] == 1:
                    ordered_drom_list.insert(0, drom)

    return ordered_drom_list


def get_insert_remove_odd_conditionals_droms(selected_droms, selected_metcon):
    """After appending ^^, finds specific odd appendings"""
    if 'banded side steps' in selected_droms:
        selected_droms.remove('banded side steps')
        selected_droms.insert(0, 'banded side steps')

    if 'burpees' in selected_droms and 'burpees' in selected_metcon:
        selected_droms.remove('burpees')
        selected_droms.append('down dog to up dog')

    for selected_drom in selected_droms:
        for k, v in droms_dict.items():
            if selected_drom == k:
                if 'plyos' in v['categories']:
                    selected_droms.remove(selected_drom)
                    selected_droms.append(selected_drom)


    # print('selected DROMS after odd conditonasls', selected_droms)
    return selected_droms

    # print('selected: ',selected_droms)


def get_length_of_final_drom_dict_for_index_dropdowns(drom_reps):
    numbered_list = []
    for index, item in enumerate(drom_reps):
        numbered_list.append(index)
    return numbered_list


def get_random_word_for_accordions00(drom_reps):
    random_string_list = []
    N = 7
    for index, item in enumerate(drom_reps):
        res = ''.join(random.choices(string.ascii_lowercase, k=N))
        random_string_list.append(res)
    print(random_string_list)
    return random_string_list


def get_random_word_for_accordions0(drom_reps):
    random_string_list = []
    N = 7
    for index, item in enumerate(drom_reps):
        res = ''.join(random.choices(string.ascii_lowercase, k=N))
        random_string_list.append(res)
    print(random_string_list)
    return random_string_list


def get_random_word_for_accordions1(drom_reps):
    random_string_list = []
    N = 7
    for index, item in enumerate(drom_reps):
        res = ''.join(random.choices(string.ascii_lowercase, k=N))
        random_string_list.append(res)
    print(random_string_list)
    return random_string_list


def get_random_word_for_accordions2(drom_reps):
    random_string_list = []
    N = 7
    for index, item in enumerate(drom_reps):
        res = ''.join(random.choices(string.ascii_lowercase, k=N))
        random_string_list.append(res)
    print(random_string_list)
    return random_string_list


def get_movements_compiled(todays_wod, tough_exercises, dictionary, movement_time):
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
    all_warmup_times_pre_toggle = get_all_movement_times(todays_wod, tough_exercises)
    prescribed_time = all_warmup_times_pre_toggle[str(movement_time)]
    all_warmup_times_plus_toggles = check_tough_input_add_time(tough_exercises, all_warmup_times_pre_toggle)
    selected_movements = filter_pop_and_select(tally_organized_dict, tally_organized_times_list,
                                               tally_organized_times_sum, prescribed_time)

    return {'TODAYS WOD AND CHECKS: ''todays wod': todays_wod,
            'has kb exercise': has_kb_exercise,
            'has barbell exercise': has_barbell_exercise,
            'has_tough_gymnastics': has_tough_gymnastics, 'tough_exercises': tough_exercises,
            'ALL WARMUP TIMES PLUS TOGGLES ': all_warmup_times_plus_toggles,
            'CALCULATIONS: ''mov_cat': mov_cat,
            'todays possible movements': todays_possible_movements, 'TALLY ORGANIZED DICT': tally_organized_dict,
            'tally organized times list': tally_organized_times_list,
            'tally organized times sum': tally_organized_times_sum,
            'prescribed time': prescribed_time, 'SELECTED MOVEMENTS: ': selected_movements
            }


def get_images_for_display(selected_movements, dictionary):
    img_list = []
    for movement in selected_movements:
        img_test = dictionary[movement]['img']
        img_list.append(img_test)
    return img_list


def get_url_for_display(selected_movements, dictionary):
    vid_list = []
    for movement in selected_movements:
        vid_test = dictionary[movement]['url']
        vid_list.append(vid_test)
    return vid_list


def get_text_for_display(selected_movements, dictionary):
    text_list = []
    for movement in selected_movements:
        text_test = dictionary[movement]['text']
        text_list.append(text_test)
    return text_list


def get_barbell_warmup_movements(todays_wod):
    """Delivers a warmup for barbell movements"""

    selected_barbell_warmups_with_dupes = []
    selected_barbell_warmups = []
    #### ERROR NOT CORRECTED YET: ONLY MATCHES IF CATGORIES ARE PERFECTLY MATCHED, NOT IF MULTPLE CATEGORIES PRESENT

    for wod in todays_wod:
        for k, v in exercises.items():
            if wod == k:
                if 'cleans' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Basic Burgener Warmup With PVC Pipe')
                    selected_barbell_warmups_with_dupes.append('Barbell Clean Warmup')
                if 'jerks' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Basic Burgener Warmup With PVC Pipe')
                    selected_barbell_warmups_with_dupes.append('Barbell Jerk Warmup')
                if 'snatches' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Basic Burgener Warmup With PVC Pipe')
                    selected_barbell_warmups_with_dupes.append('Barbell Snatch Warmup')
                if 'presses' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Progressive Barbell Loading for Pressing')
                if 'overhead presses' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Progressive Barbell Loading for Pressing')
                if 'deadlifts' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Progressive Barbell Loading for Deadlifting')
                if 'squats' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Progressive Barbell Loading for Squatting')

    for i in selected_barbell_warmups_with_dupes:
        if i not in selected_barbell_warmups:
            selected_barbell_warmups.append(i)

    if 'Basic Burgener Warmup With PVC Pipe' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Basic Burgener Warmup With PVC Pipe')
        selected_barbell_warmups.insert(0, 'Basic Burgener Warmup With PVC Pipe')
    if 'Barbell Jerk Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Jerk Warmup')
        selected_barbell_warmups.insert(1, 'Barbell Jerk Warmup')
    if 'Barbell Snatch Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Snatch Warmup')
        selected_barbell_warmups.insert(1, 'Barbell Snatch Warmup')
    if 'Barbell Clean Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Clean Warmup')
        selected_barbell_warmups.insert(1, 'Barbell Clean Warmup')
    return selected_barbell_warmups


def get_kettlebell_warmup(todays_wod):
    """Delivers a warmup for kb movements"""

    selected_kb_warmups_with_dupes = []
    selected_kb_warmups = []

    for wod in todays_wod:
        for k, v in exercises.items():
            if wod == k:
                if 'swings' in v['category']:
                    selected_kb_warmups_with_dupes.append('Kettlebell Swings')
                    selected_kb_warmups_with_dupes.append('Goatbag Swings')
                if 'kettlebell overhead' in v['category']:
                    selected_kb_warmups_with_dupes.append('Kettlebell Halos')
                if 'kettlebell squats' in v['category']:
                    selected_kb_warmups_with_dupes.append('Goblet Squats')
                if 'kettlebells' in v['category']:
                    selected_kb_warmups_with_dupes.append('Goblet Squats')
                    selected_kb_warmups_with_dupes.append('Goatbag Swings')

    for i in selected_kb_warmups_with_dupes:
        if i not in selected_kb_warmups:
            selected_kb_warmups.append(i)

    if 'Goatbag Swings' in selected_kb_warmups:
        selected_kb_warmups.remove('Goatbag Swings')
        selected_kb_warmups.insert(0, 'Goatbag Swings')
    if 'Goblet Squats' in selected_kb_warmups:
        selected_kb_warmups.remove('Goblet Squats')
        selected_kb_warmups.insert(1, 'Goblet Squats')
    if 'Kettlebell Halos' in selected_kb_warmups:
        selected_kb_warmups.remove('Kettlebell Halos')
        selected_kb_warmups.insert(1, 'Kettlebell Halos')
    if 'Kettlebell Swings' in selected_kb_warmups:
        selected_kb_warmups.remove('Kettlebell Swings')
        selected_kb_warmups.append('Kettlebell Swings')
    return selected_kb_warmups


def get_gymnastics_warmup(todays_wod):
    """Delivers a warmup for gymnastics movements (COULD BE CHANGED TO CHECKING FOR MINUTES OF GYMNASTICS"""
    tough_gymnastics_warmups = []
    for wod in todays_wod:
        for k, v in gymnastics_warmups.items():
            for thing in v['exercises']:
                if wod == thing:
                    tough_gymnastics_warmups.append(k)
    return tough_gymnastics_warmups


def get_gymnastics_warmup_reps(tough_gymnastics_warmups):
    """Finds reps for tough gymnastics movements in WOD and outputs in a list"""
    tough_gymnastics_warmup_reps_post_random = []

    for wu in tough_gymnastics_warmups:
        x = gymnastics_warmups[wu].get('reps')
        y = random.choice(x)
        tough_gymnastics_warmup_reps_post_random.append(y)

    return tough_gymnastics_warmup_reps_post_random


def get_why_drom_selected_dict(drom_final_dict, todays_wod):
    """If a drom is selected, what does it warm up? Compare that list to what is in the WOD. Output list of what that
    DROM warms up"""
    drom_chosen = []
    exercises_chosen = []
    for key in drom_final_dict.keys():
        print(key)
        for drom_category in droms_dict[key]['categories']:
            for wod in todays_wod:
                for exercise_cat in exercises[wod]['category']:
                    if drom_category == exercise_cat:
                        drom_chosen.append(key)
                        exercises_chosen.append(wod)

    print('DROM CHOSEN: ',drom_chosen)
    print('EXERCISES CHOSEN:', exercises_chosen)

    # list = [(k, v) for k, v in dict.items()]


    combo = tuple(zip(drom_chosen, exercises_chosen))
    print('COMBO', combo)

    # print('COMBO', list(zip(drom_chosen, exercises_chosen)))
    return combo

def add_why_drom_selected_to_drom_final_dict(drom_final_dict, why_drom):
    """THIS CODE ADDS WHAT THE DROM IS TARGETING but I cant get rid of dupes in the 'targets' output"""
    # breakpoint()
    drom_tester_dict = dict(drom_final_dict)

    for k,v in drom_final_dict.items():
        bb = []

        # print(k)
        for x in why_drom:
            # print(x)
    #         # breakpoint()
            for y in x:
                if y == k:
                    print('yaaaa')
                    print(x[1])

                    bb.append(x[1])

                    drom_final_dict[k]['targets'] = bb
    #
    print('DROMTESTERDICT:', drom_final_dict)

    result_with_dup_targets = {}
    for k, v in drom_tester_dict.items():
        if v not in result_with_dup_targets.values():
            result_with_dup_targets[k] = v

    print("RESULTSSSOIJFEWOIFJEWOIEWJF", result_with_dup_targets)

    return result_with_dup_targets