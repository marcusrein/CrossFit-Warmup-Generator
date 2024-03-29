from appfolder.drom_warmups import *
from appfolder.exercises import *
from appfolder.gymnastics_warmups import *
from appfolder.metcon_warmups import *
from appfolder.filters import *
from appfolder.checks import *
import random


def get_new_drom_dict_considering_equipment(warmup_equip_list, droms_dict):
    """Looks at the checkboxed warmup equipment and removes items droms_dict if they are unchecked"""

    # NOT SURE IF I NEED A TUPLE OUTPUT?

    droms_with_equip = {}
    removed_droms = []
    for k2, v2 in droms_dict.items():
        if warmup_equip_list:
            for equip in warmup_equip_list:
                if droms_dict[k2]['equipment'] == 'none':
                    droms_with_equip[k2] = v2
                elif droms_dict[k2]['equipment'] == equip:
                    droms_with_equip[k2] = v2
        else:
            if droms_dict[k2]['equipment'] == 'none':
                droms_with_equip[k2] = v2
            elif droms_dict[k2]['equipment']:
                removed_droms.append(k2)

    return droms_with_equip


# THIS THOUGHT PROCESS HAS TO HAPPEN MUCH EARLIER
def get_new_drom_warmup_list_considering_equipment(drom_warmup, new_drom_dict):
    list_of_removed_droms = list(new_drom_dict[1])
    new_drom_dict_just_dict = new_drom_dict[0]

    for removed_item in list_of_removed_droms:
        drom_warmup.pop(removed_item)
        # for drom in drom_warmup[0]:
        #     if removed_item == drom:
        #         del new_drom_dict_just_dict[removed_item]


    return drom_warmup


def get_force_from_todays_wod(todays_wod, exercises_dict):
    """
    :param todays_wod:
    :param exercises_dict:
    :return: list of forced movements that MUST be in the warmups
    """

    forced_droms = []
    forced_gymnastics = []
    forced_kb = []
    forced_barbell = []

    for item in todays_wod:
        for k, v in exercises_dict.items():
            if item == k:
                try:
                    if v['force drom']:
                        for thang in v['force drom']:
                            forced_droms.append(thang)
                except KeyError:
                    pass
                try:
                    if v['force gymnastics']:
                        for thing in v['force gymnastics']:
                            forced_gymnastics.append(thing)
                except KeyError:
                    pass
                try:
                    if v['force kb']:
                        for abc in v['force kb']:
                            forced_kb.append(abc)
                except KeyError:
                    pass
                try:
                    if v['force barbell']:
                        for foo in v['force barbell']:
                            forced_barbell.append(foo)
                except KeyError:
                    pass

    return {'forced droms': forced_droms, 'forced gymnastics': forced_gymnastics, 'forced kb': forced_kb,
            'forced barbell':
                forced_barbell}


def get_combined_drom_warmup(forced_droms, initially_selected_droms):
    drom_warmup = []
    for item in forced_droms['forced droms']:
        drom_warmup.append(item)
    for ab12 in initially_selected_droms:
        warmup = ab12
        not_in_list = warmup not in drom_warmup
        if not_in_list:
            drom_warmup.append(ab12)

    return drom_warmup


def get_cat_from_todays_wod(todays_wod, dictionary):
    """
    Gets todays_wod and finds the categories associated to todays_wod with a supplied dictionary
    """
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
    """
    Gets possible movements that align with movement categories (mov_cat).
    Has duplicates (WHICH IS OKAY because future code removes them)
    """
    possible_warmups = []
    for cat in mov_cat:
        for k, v in dictionary.items():
            if cat in v['categories']:
                possible_warmups.append(k)

    return possible_warmups


def Merge(dict1, dict2, dict3, dict4):
    res = {**dict1, **dict2, **dict3, **dict4}
    return res


def remove_double_core_band_pvc(tally_organized_dict):

    ## REFORMAT??
    pvc = {}
    core = {}
    band = {}
    other = {}

    for k, v in tally_organized_dict.items():
        if droms_dict[k]['rpe'] == 0:
            pvc[k] = v
        elif droms_dict[k]['rpe'] == 1:
            band[k] = v
        elif droms_dict[k]['rpe'] == 2:
            core[k] = v
        else:
            other[k] = v

    while len(core) > 1:
        core.popitem()
    ## REFORMAT??
    while len(band) > 1:
        band.popitem()
    while len(pvc) > 1:
        pvc.popitem()

    returned_list = Merge(core, band, pvc, other)
    ordered_tally = {k: v for k, v in sorted(returned_list.items(), key=lambda item: item[1], reverse=True)}

    return ordered_tally


def modify_tally(mov_cat, possible_movements, warmup_equipment):
    returned_list = []

    for cat in mov_cat:
        if cat == 'squats':
            x = 'air squats'
            y = ['worlds greatest stretch', 'inchworms']
            if 'loop resistance band' in warmup_equipment:
                z = ['banded side steps', 'banded hip activation series']
                print('yaaaaa')
            for i in range(50):
                returned_list.append(x)
            for i in range(40):
                returned_list.append(random.choice(y))
            try:
                for i in range(30):
                    returned_list.append(random.choice(z))
            except:
                UnboundLocalError
        if cat == 'cleans':
            x = 'worlds greatest stretch'
            y = 'inchworms'
            yy = ['dead bugs', 'core rolling']
            if 'loop resistance band' in warmup_equipment:
                z = ['banded side steps', 'banded hip activation series']
            for i in range(55):
                returned_list.append(x)
            for i in range(45):
                returned_list.append(y)
            for i in range(65):
                returned_list.append(random.choice(yy))
            try:
                for i in range(30):
                    returned_list.append(random.choice(z))
            except:
                UnboundLocalError
        if cat == 'deadlifts':
            x = 'worlds greatest stretch'
            y = 'inchworms'
            if 'loop resistance band' in warmup_equipment:
                z = ['banded side steps', 'banded hip activation series']
            for i in range(60):
                returned_list.append(x)
            for i in range(65):
                returned_list.append(y)
            try:
                for i in range(30):
                    returned_list.append(random.choice(z))
            except:
                UnboundLocalError
        if cat == 'snatches':
            x = 'worlds greatest stretch'
            y = 'inchworms'
            z = 'thoracic bridges'
            zz = ['banded side steps', 'banded hip activation series']
            a = random.choice(zz)
            zzz = 'shoulder passthroughs'

            if 'loop resistance band' in warmup_equipment:
                for i in range(45):
                    returned_list.append(a)
                    # breakpoint()
            if 'pvc pipe' in warmup_equipment:
                for i in range(35):
                    returned_list.append(zzz)
            for i in range(30):
                returned_list.append(x)
            for i in range(25):
                returned_list.append(y)
            for i in range(20):
                returned_list.append(z)

        if cat == 'jerks':
            x = 'worlds greatest stretch'
            y = 'thoracic bridges'
            for i in range(75):
                returned_list.append(x)
            for i in range(80):
                returned_list.append(y)
        if cat == 'saggital presses':
            x = 'push ups'
            if 'pvc pipe' in warmup_equipment:
                zzz = ['shoulder passthroughs']
            for i in range(77):
                returned_list.append(x)
            try:
                for i in range(30):
                    returned_list.append(random.choice(zzz))
            except:
                UnboundLocalError
        if cat == 'pull up':
            x = 'thoracic bridges'
            for i in range(43):
                returned_list.append(x)
            if 'pvc pipe' in warmup_equipment:
                zzz = ['shoulder passthroughs']
            try:
                for i in range(54):
                    returned_list.append(random.choice(zzz))
            except:
                UnboundLocalError


    for forced_movement in returned_list:
        possible_movements.append(forced_movement)

    return possible_movements


def get_organized_tally_dict(possible_movements):
    """
    :param possible_movements: inputs todays possible DROMs, tallys them, sorts them, partially randomizes them if their
    values are equal, then sorts them again.
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
    """ Big list of all the movement times alloted """
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
        drom_time += 6
        barbell_time += 10
        kb_time += 5
        tough_gymnastics_time += 10
    elif check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6
        barbell_time += 10
        kb_time += 5
    elif check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6
        barbell_time += 10
        tough_gymnastics_time += 10
    elif check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6
        barbell_time += 10
    elif not check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6
        kb_time += 5
        tough_gymnastics_time += 10
    elif not check_barbell_exercise(todays_wod) \
            and check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6
        kb_time += 5
    elif not check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6
        tough_gymnastics_time += 10
    elif not check_barbell_exercise(todays_wod) \
            and not check_kb_exercise(todays_wod) \
            and not check_tough_gymnastics(todays_wod):
        metcon_time += 2
        drom_time += 6

    if len(todays_wod) > 3:
        drom_time += 1

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


def get_which_movements_are_barbell_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod"""
    barbell_movements_from_todays_wod = []

    for movement in todays_wod:
        for k in exercises_dict.keys():
            if movement == k and exercises_dict[k]['loaded'] == 'barbell':
                barbell_movements_from_todays_wod.append(movement)

    return barbell_movements_from_todays_wod


def get_which_movements_are_kb_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod"""
    kb_movements_from_todays_wod = []

    for movement in todays_wod:
        for k in exercises_dict.keys():
            if movement == k and exercises_dict[k]['loaded'] == 'kb':
                kb_movements_from_todays_wod.append(movement)

    return kb_movements_from_todays_wod


def get_which_movements_are_db_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod"""
    kb_movements_from_todays_wod = []

    for movement in todays_wod:
        for k in exercises_dict.keys():
            if movement == k and exercises_dict[k]['loaded'] == 'db':
                kb_movements_from_todays_wod.append(movement)

    return kb_movements_from_todays_wod


def get_which_movements_are_tough_gymnastics_movements(todays_wod):
    """Delivers a list of barbell movements only from todays wod
    THIS IS UGLY MAKE THIS NICER
    """
    tough_gymnastics_movements_from_todays_wod = []

    for x in todays_wod:
        if x == 'pull up' or x == 'pistol' or x == 'pistols' or x == 'handstand pushup' or x == 'handstand walk' \
                or x == 'kipping pull up' or x == 'ring muscle up' or x == 'bar muscle up' or x == 'butterfly pull up':
            tough_gymnastics_movements_from_todays_wod.append(x.title())
    return tough_gymnastics_movements_from_todays_wod


def get_metcon_reps(selected_metcon):
    if selected_metcon:
        y = metcons_dict.get(selected_metcon)
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
        # print('foooo')
    if any('jerk' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        # print('fiiii')
    if any('snatch' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        # print('moo')

    if any('overhead squat' in wod for wod in todays_wod) and 'shoulder passthroughs' not in selected_movements:
        addendum.append('shoulder passthroughs')
        # print('poooop')
    if any('overhead squat' in wod for wod in todays_wod) and 'core rolling' not in selected_movements:
        addendum.append('core rolling')
    if any('overhead squat' in wod for wod in todays_wod) and 'inchworms' not in selected_movements:
        addendum.append('inchworms')

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


def get_rpe(drom):
    """
    Used in 'get_ordered_drom_list' func to provide a key to organize droms by their RPE level
    """
    return droms_dict[drom]['rpe']


def get_ordered_drom_list(selected_droms):
    selected_droms.sort(key=get_rpe)
    return selected_droms


def get_insert_remove_odd_conditionals_droms(selected_droms, selected_metcon):
    """After appending ^^, finds specific odd appendings"""

    if 'burpees' in selected_droms and 'burpees' in selected_metcon:
        selected_droms.remove('burpees')
        selected_droms.append('down dog to up dog')

    # print('selected DROMS after odd conditonasls', selected_droms)
    return selected_droms

    # print('selected: ',selected_droms)


def get_length_of_final_drom_dict_for_index_dropdowns(drom_reps):
    numbered_list = []
    for index, item in enumerate(drom_reps):
        numbered_list.append(index)
    return numbered_list


def get_movements_compiled(todays_wod, tough_exercises, dictionary, movement_time):
    """This is a function that compiles DROMS for viewing."""
    ##CLEANER##
    todays_wod = remove_none_from_todays_wod(todays_wod)

    ##CHECKS##
    has_kb_exercise = check_kb_exercise(todays_wod)
    had_db_exercise = check_db_exercise(todays_wod)
    has_barbell_exercise = check_barbell_exercise(todays_wod)
    has_tough_gymnastics = check_tough_gymnastics(todays_wod)
    ##GETTERS##
    force_list = get_force_from_todays_wod(todays_wod, exercises_dict)
    mov_cat = get_cat_from_todays_wod(todays_wod, exercises_dict)
    todays_possible_movements = get_possible_movements_from_mov_cat(mov_cat, dictionary)
    tally_organized_dict = get_organized_tally_dict(todays_possible_movements)
    tally_organized_times_list = get_times_of_organized_tally_list(tally_organized_dict, dictionary)
    tally_organized_times_sum = get_sum_times_of_list(tally_organized_times_list)
    all_warmup_times_pre_toggle = get_all_movement_times(todays_wod, tough_exercises)
    prescribed_time = all_warmup_times_pre_toggle[str(movement_time)]
    all_warmup_times_plus_toggles = check_tough_input_add_time(tough_exercises, all_warmup_times_pre_toggle)
    selected_movements = filter_pop_and_select(tally_organized_dict, tally_organized_times_list,
                                               tally_organized_times_sum, prescribed_time)[0]

    return {'TODAYS WOD AND CHECKS: ''todays wod': todays_wod, 'FORCE LIST: ': force_list,
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


def get_initial_drom_compiled(todays_wod, tough_exercises, dictionary, movement_time, warmup_equipment):
    """This is a function that compiles DROMS for viewing."""
    ##CLEANER##
    todays_wod = remove_none_from_todays_wod(todays_wod)

    ##CHECKS##
    has_kb_exercise = check_kb_exercise(todays_wod)
    has_barbell_exercise = check_barbell_exercise(todays_wod)
    has_tough_gymnastics = check_tough_gymnastics(todays_wod)
    ##GETTERS##
    force_list = get_force_from_todays_wod(todays_wod, exercises_dict)
    mov_cat = get_cat_from_todays_wod(todays_wod, exercises_dict)
    todays_possible_movements = get_possible_movements_from_mov_cat(mov_cat, dictionary)
    todays_possible_movements_modified = modify_tally(mov_cat, todays_possible_movements, warmup_equipment)


    tally_organized_dict = get_organized_tally_dict(todays_possible_movements_modified)
    cleaned_core_pvc_dict = remove_double_core_band_pvc(tally_organized_dict)
    tally_organized_times_list = get_times_of_organized_tally_list(cleaned_core_pvc_dict, dictionary)
    tally_organized_times_sum = get_sum_times_of_list(tally_organized_times_list)
    all_warmup_times_pre_toggle = get_all_movement_times(todays_wod, tough_exercises)
    prescribed_time = all_warmup_times_pre_toggle[str(movement_time)]
    all_warmup_times_plus_toggles = check_tough_input_add_time(tough_exercises, all_warmup_times_pre_toggle)
    selected_movements = filter_pop_and_select(cleaned_core_pvc_dict, tally_organized_times_list,
                                               tally_organized_times_sum, prescribed_time)[0]
    return {'TODAYS WOD AND CHECKS: ''todays wod': todays_wod, 'FORCE LIST: ': force_list,
            'has kb exercise': has_kb_exercise,
            'has barbell exercise': has_barbell_exercise,
            'has_tough_gymnastics': has_tough_gymnastics, 'tough_exercises': tough_exercises,
            'ALL WARMUP TIMES PLUS TOGGLES ': all_warmup_times_plus_toggles,
            'CALCULATIONS: ''mov_cat': mov_cat,
            'todays possible movements': todays_possible_movements, 'TALLY ORGANIZED DICT': tally_organized_dict,
            'tally organized times list': tally_organized_times_list,
            'tally organized times sum': tally_organized_times_sum,
            'prescribed time': prescribed_time, 'SELECTED MOVEMENTS: ': selected_movements, 'cleaned core pvc dict: ':
            cleaned_core_pvc_dict
            }


def get_droms_compiled(todays_wod, tough_exercises, drom_time, selected_metcon, warmup_duration_short,
                       warmup_duration_long, droms_dict_equipment_considered, warmup_equipment):
    droms_compiled = get_initial_drom_compiled(
        todays_wod, tough_exercises, droms_dict_equipment_considered, drom_time, warmup_equipment)
    # initially_selected_droms = droms_compiled.get('SELECTED MOVEMENTS: ')
    # breakpoint()

    cleaned_core_pvc_dict_imported = droms_compiled.get('cleaned core pvc dict: ')
    tally_drom_warmup_times_list = get_times_of_organized_tally_list(cleaned_core_pvc_dict_imported, droms_dict_equipment_considered)
    tally_drom_warmup_organized_times_sum = get_sum_times_of_list(tally_drom_warmup_times_list)
    drom_warmup_times_pre_toggle = get_all_movement_times(todays_wod, tough_exercises)
    drom_warmup_prescribed_time = drom_warmup_times_pre_toggle[str(drom_time)]
    if warmup_duration_short:
        drom_warmup_prescribed_time -= 2
    if warmup_duration_long:
        drom_warmup_prescribed_time += 2
    selected_movements = filter_pop_and_select(cleaned_core_pvc_dict_imported, tally_drom_warmup_times_list,
                                               tally_drom_warmup_organized_times_sum, drom_warmup_prescribed_time)[0]
    # popped_items = filter_pop_and_select(cleaned_core_pvc_dict_imported, tally_drom_warmup_times_list,
    #                                      tally_drom_warmup_organized_times_sum, drom_warmup_prescribed_time)[1]
    # ADDING BACK IN DROMS THAT WERE REMOVED DUE TO CORE POPPAGE
    # if core_diff > 0:
    #     for i in range(core_diff):
    #         selected_movements.append(popped_items[i-1][0])


    selected_droms_after_odd_conditionals = get_insert_remove_odd_conditionals_droms(
        selected_movements, selected_metcon)

    selected_droms_ordered_list = get_ordered_drom_list(selected_droms_after_odd_conditionals)
    drom_warmup = selected_droms_ordered_list

    return [drom_warmup, drom_warmup_prescribed_time]


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
        for k, v in exercises_dict.items():
            if wod == k:
                if 'cleans' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Basic Burgener Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Clean Warmup')
                if 'jerks' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Basic Burgener Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Overhead Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Jerk Warmup')
                if 'snatches' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Basic Burgener Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Overhead Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Snatch Warmup')
                if 'presses' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Barbell Overhead Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Press Warmup')
                if 'overhead presses' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Barbell Overhead Warmup')
                    selected_barbell_warmups_with_dupes.append('Barbell Press Warmup')
                if 'overhead squats' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Barbell Overhead Warmup')
                if 'deadlifts' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Barbell Deadlift Warmup')
                if 'squats' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Barbell Squat Warmup')
                if 'lunges' in v['category']:
                    selected_barbell_warmups_with_dupes.append('Barbell Lunge Warmup')

        ## REMOVES DUPLICATES
    for i in selected_barbell_warmups_with_dupes:
        if i not in selected_barbell_warmups:
            selected_barbell_warmups.append(i)

        ## ORGANIZES THE OUTPUT IN ORDER FROM LAST TO FIRST)

    # print('111:',selected_barbell_warmups)

    if 'Basic Burgener Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Basic Burgener Warmup')
        selected_barbell_warmups.insert(0, 'Basic Burgener Warmup')
    if 'Barbell Overhead Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Overhead Warmup')
        selected_barbell_warmups.append('Barbell Overhead Warmup')
    if 'Barbell Squat Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Squat Warmup')
        selected_barbell_warmups.append('Barbell Squat Warmup')

    if 'Barbell Clean Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Clean Warmup')
        selected_barbell_warmups.append('Barbell Clean Warmup')
    if 'Barbell Jerk Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Jerk Warmup')
        selected_barbell_warmups.append('Barbell Jerk Warmup')
    if 'Barbell Snatch Warmup' in selected_barbell_warmups:
        selected_barbell_warmups.remove('Barbell Snatch Warmup')
        selected_barbell_warmups.append('Barbell Snatch Warmup')

    # print('222', selected_barbell_warmups)

    return selected_barbell_warmups


def get_kettlebell_warmup(todays_wod):
    """Delivers a warmup for kb movements"""

    selected_kb_warmups_with_dupes = []
    selected_kb_warmups = []

    for wod in todays_wod:
        for k, v in exercises_dict.items():
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

def get_dumbbell_warmup(todays_wod):
    """Delivers a warmup for kb movements"""

    selected_db_warmups_with_dupes = []
    selected_db_warmups = []

    for wod in todays_wod:
        for k, v in exercises_dict.items():
            if wod == k:
                if 'dumbbells overhead' in v['category']:
                    selected_db_warmups_with_dupes.append('Dumbbell Shoulder Press')
                if 'dumbbells squat' in v['category']:
                    selected_db_warmups_with_dupes.append('Dumbbell Goblet Squats')
                if 'dumbbells snatch' in v['category']:
                    selected_db_warmups_with_dupes.append('Dumbbell Goblet Squats')
                    selected_db_warmups_with_dupes.append('Dumbbell Shoulder Press')
                    selected_db_warmups_with_dupes.append('Dumbbell Hang Power Clean')
                    selected_db_warmups_with_dupes.append('Dumbbell Power Snatch')
                if 'dumbbells clean' in v['category']:
                    selected_db_warmups_with_dupes.append('Dumbbell Goblet Squats')
                    selected_db_warmups_with_dupes.append('Dumbbell Hang Power Clean')
                    selected_db_warmups_with_dupes.append('Dumbbell Power Clean')
                if 'dumbbells deadlift' in v['category']:
                    selected_db_warmups_with_dupes.append('Dumbbell Goblet Squats')
                    selected_db_warmups_with_dupes.append('Dumbbell Deadlift')
                if 'dumbbells core' in v['category']:
                    selected_db_warmups_with_dupes.append('Renegade Row')

    for i in selected_db_warmups_with_dupes:
        if i not in selected_db_warmups:
            selected_db_warmups.append(i)
    if 'Dumbbell Goblet Squats' in selected_db_warmups:
        selected_db_warmups.remove('Dumbbell Goblet Squats')
        selected_db_warmups.insert(0, 'Dumbbell Goblet Squats')
    if 'Dumbbell Power Snatch' in selected_db_warmups:
        selected_db_warmups.remove('Dumbbell Power Snatch')
        selected_db_warmups.insert(1, 'Dumbbell Power Snatch')
    if 'Dumbbell Hang Power Snatch' in selected_db_warmups:
        selected_db_warmups.remove('Dumbbell Hang Power Snatch')
        selected_db_warmups.insert(1, 'Dumbbell Hang Power Snatch')
    if 'Dumbbell Shoulder Press' in selected_db_warmups:
        selected_db_warmups.remove('Dumbbell Shoulder Press')
        selected_db_warmups.insert(1, 'Dumbbell Shoulder Press')
    if 'Dumbbell Hang Power Clean' in selected_db_warmups:
        selected_db_warmups.remove('Dumbbell Hang Power Clean')
        selected_db_warmups.insert(1, 'Dumbbell Hang Power Clean')
    if 'Dumbbell Deadlift' in selected_db_warmups:
        selected_db_warmups.remove('Dumbbell Deadlift')
        selected_db_warmups.insert(1, 'Dumbbell Deadlift')


    return selected_db_warmups


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
        # print(key)
        for drom_category in droms_dict[key]['categories']:
            for wod in todays_wod:
                for exercise_cat in exercises_dict[wod]['category']:
                    if drom_category == exercise_cat:
                        drom_chosen.append(key)
                        exercises_chosen.append(wod)

    # print('DROM CHOSEN: ',drom_chosen)
    # print('EXERCISES CHOSEN:', exercises_chosen)

    # list = [(k, v) for k, v in dict.items()]

    combo = tuple(zip(drom_chosen, exercises_chosen))
    # print('COMBO', combo)

    # print('COMBO', list(zip(drom_chosen, exercises_chosen)))
    return combo


def add_why_drom_selected_to_drom_final_dict(drom_final_dict, why_drom):
    """THIS CODE ADDS WHAT THE DROM IS TARGETING but I cant get rid of dupes in the 'targets' output"""
    # breakpoint()
    drom_tester_dict = dict(drom_final_dict)

    for k, v in drom_final_dict.items():
        bb = []

        # print(k)
        for x in why_drom:
            # print(x)
            #         # breakpoint()
            for y in x:
                warmup = x[1]
                is_not_in_list = warmup not in bb

                if y == k and is_not_in_list:
                    # print(warmup)
                    bb.append(warmup)
                    drom_final_dict[k]['targets'] = bb

    return drom_final_dict


def get_est_times_for_display(metcon_warmup, drom_warmup, gymnastics_warmups, kb_warmups, barbell_warmups):
    total_estimated_time = 0

    if metcon_warmup:
        total_estimated_time += 1
    if len(drom_warmup) <= 3:
        total_estimated_time += 3
    if len(drom_warmup) == 4:
        total_estimated_time += 4
    if len(drom_warmup) == 5:
        total_estimated_time += 5
    if len(drom_warmup) == 6:
        total_estimated_time += 6
    if len(drom_warmup) == 7:
        total_estimated_time += 7
    if len(drom_warmup) == 8:
        total_estimated_time += 9
    if len(drom_warmup) == 9:
        total_estimated_time += 12
    if len(drom_warmup) > 9:
        total_estimated_time += 13
    if gymnastics_warmups:
        total_estimated_time += 4
    if kb_warmups:
        total_estimated_time += 4
    if barbell_warmups:
        if len(barbell_warmups) == 1:
            total_estimated_time += 5
        if len(barbell_warmups) == 2:
            total_estimated_time += 8
        if len(barbell_warmups) == 3:
            total_estimated_time += 12
        if len(barbell_warmups) > 3:
            total_estimated_time += 14
    total_estimated_time = total_estimated_time - 3
    total_estimated_time_plus5 = total_estimated_time + 5
    return total_estimated_time, total_estimated_time_plus5
