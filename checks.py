from exercises import *
from checks import *


# DONT NEED?
# def check_exercise_fuzz_80(exercise1_prefuzz):
#     for j in list(exercises.keys()):
#         if (fuzz.ratio(exercise1_prefuzz, j)) > 80:
#             return j


# DONT NEED?
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


def check_tough_input_add_time(tough_exercises, all_warmup_times_pre_toggle):
    """Adds appropriate times for tough exercises"""
    for tough_exercise in tough_exercises:
        xxx = exercises.get(tough_exercise)
        loaded_value = xxx.get('loaded')
        if loaded_value == 'kb':
            all_warmup_times_pre_toggle['focused_kb_time'] += 3
        elif loaded_value == 'barbell':
            all_warmup_times_pre_toggle['focused_barbell_time'] += 5
        elif loaded_value == False and check_tough_gymnastics(tough_exercises) == True:
            all_warmup_times_pre_toggle['focused_gymanstics_time'] += 8

    all_warmup_times_post_toggle = all_warmup_times_pre_toggle
    return all_warmup_times_post_toggle
