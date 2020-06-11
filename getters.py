


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


def get_organized_drom_tally_dict(possible_warmups):
    tally_of_warmups = {}
    for w in possible_warmups:
        if w in tally_of_warmups:
            tally_of_warmups[w] += 1
        else:
            tally_of_warmups[w] = 1
    ordered_tally = {k: v for k, v in sorted(tally_of_warmups.items(), key=lambda item: item[1], reverse=True)}
    return ordered_tally


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
    focused_gymnastics_time = 0
    focused_barbell_time = 0
    focused_kb_time = 0

    # print(check_focus_barbell(focus))
    # print(check_barbell_exercise(todays_wod))
    # print(check_tough_gymnastics(todays_wod))

    ## LOW GYMNASTICS ##
    if intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 8
        barbell_time += 5
        kb_time += 5
        focused_gymnastics_time += 10
        print('TTT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 7
        barbell_time += 5
        kb_time += 5
        print('TTF')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 7
        barbell_time += 5
        focused_gymnastics_time += 10
        print('TFT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == True \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 6
        barbell_time += 5
        print('TFF')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 6
        kb_time += 5
        focused_gymnastics_time += 10
        print('FTT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == True \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 2
        drom_time += 6
        kb_time += 5
        print('FTF')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == True:
        metcon_time += 2
        drom_time += 6
        focused_gymnastics_time += 10
        print('FFT')

    elif intensity == 'low' \
            and check_barbell_exercise(todays_wod) == None \
            and check_kb_exercise(todays_wod) == None \
            and check_tough_gymnastics(todays_wod) == None:
        metcon_time += 3
        drom_time += 7
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
