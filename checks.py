from exercises import *
from checks import *
from fuzzywuzzy import fuzz


def check_exercise_fuzz_80(exercise1_prefuzz):
    for j in list(exercises.keys()):
        if (fuzz.ratio(exercise1_prefuzz, j)) > 80:
            return j


def remove_none_from_todays_wod(todays_wod):
    """Remove "none" from todays_wod to clean it up"""
    cleaned_array = []
    for wod in todays_wod:
        if wod != None:
            cleaned_array.append(wod)
    return cleaned_array


def check_kb_exercise(todays_wod):
    for wod in todays_wod:
        if exercises[wod]['loaded'] == 'kb':
            return True


def check_barbell_exercise(todays_wod):
    for wod in todays_wod:
        if exercises[wod]['loaded'] == 'barbell':
            return True


def check_tough_gymnastics(todays_wod):
    words = ['pistol', 'pistols', 'handstand', 'pull up', 'pull ups', 'kipping', 'ring', 'muscle up']
    check = any(item in words for item in todays_wod)
    if check:
        return True


def check_toggles_add_time(todays_wod, todays_wod_toggles, all_warmup_times_pre_toggle):
    """Adds appropriate times if toggles are engaged"""

    for i in range(len(todays_wod)):
        xxx = exercises.get(todays_wod[i])
        loaded_value = xxx.get('loaded')
        if todays_wod_toggles[i] == 'Yes':
            if loaded_value == 'kb':
                all_warmup_times_pre_toggle['focused_kb_time'] += 3
            elif loaded_value == 'barbell':
                all_warmup_times_pre_toggle['focused_barbell_time'] += 5
            elif loaded_value == False and check_tough_gymnastics(todays_wod) == True:
                all_warmup_times_pre_toggle['focused_gymanstics_time'] += 8

    all_warmup_times_post_toggle = all_warmup_times_pre_toggle

    return all_warmup_times_post_toggle
