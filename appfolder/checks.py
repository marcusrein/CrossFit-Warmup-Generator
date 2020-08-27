from appfolder.checks import *
from appfolder.exercises import *
from appfolder.drom_warmups import *

import random


# All of these should return True or False

def check_no_input_todays_wod(todays_wod):
    if not todays_wod:
        global error_message
        error_message = 'Please enter your exercises'
    else:
        error_message = ''
    return error_message


def remove_none_from_todays_wod(todays_wod):
    """Remove "none" from todays_wod to clean it up"""
    cleaned_array = []
    for wod in todays_wod:
        if wod != None:
            cleaned_array.append(wod)
    return cleaned_array


def check_kb_exercise(todays_wod):
    for wod in todays_wod:
        if exercises_dict[wod]['loaded'] == 'kb':
            return True


def check_db_exercise(todays_wod):
    for wod in todays_wod:
        if exercises_dict[wod]['loaded'] == 'db':
            return True



def check_barbell_exercise(todays_wod):
    for wod in todays_wod:
        if exercises_dict[wod]['loaded'] == 'barbell':
            return True


def check_tough_gymnastics(todays_wod):
    words = ['pistol', 'pistols', 'handstand', 'pull up', 'pull ups', 'kipping', 'ring', 'muscle up']
    check = any(item in words for item in todays_wod)
    if check:
        return True


def check_tough_input_add_time(tough_exercises, all_warmup_times_pre_toggle):
    """Adds appropriate times for tough exercises"""
    for tough_exercise in tough_exercises:
        xxx = exercises_dict.get(tough_exercise)
        loaded_value = xxx.get('loaded')
        if loaded_value == 'kb':
            all_warmup_times_pre_toggle['focused_kb_time'] += 3
        elif loaded_value == 'barbell':
            all_warmup_times_pre_toggle['focused_barbell_time'] += 5
        elif loaded_value == False and check_tough_gymnastics(tough_exercises) == True:
            all_warmup_times_pre_toggle['focused_gymanstics_time'] += 8

    all_warmup_times_post_toggle = all_warmup_times_pre_toggle
    return all_warmup_times_post_toggle


def check_core_in_lists(initially_selected_droms, forced_droms):
    """ If core in forced DROMS, choose 1. Superceded initially selected DROMS. Returns one core movement and the diff
    between the what was selected and the result so that number can be put back in from the popped info"""
    result = []
    initially_selected_core = []

    for core_warmup in initially_selected_droms:
        for drom in droms_dict:
            if core_warmup == drom:
                if droms_dict[drom]['rpe'] == 2:
                    initially_selected_core.append(core_warmup)

    forced_core = []

    for k, v in forced_droms.items():
        for drom in droms_dict:
            for value in v:
                if value == drom:
                    if droms_dict[value]['rpe'] == 2:
                        forced_core.append(value)

    if forced_core:
        result = random.choice(forced_core)
    elif initially_selected_core:
        if forced_core:
            result = random.choice(forced_core)
    elif initially_selected_core:
        result = random.choice(initially_selected_core)

    x = len(forced_core) + len(initially_selected_core)
    y = 1
    diff_for_pop = x-y

    return result, diff_for_pop
