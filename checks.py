
def check_kb_exercise(todays_wod):
    # print(todays_wod)
    for wod in todays_wod:
        # print(wod)
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
        breakpoint()
        if todays_wod_toggles[i] == 'Yes':
            if loaded_value == 'kb':
                print(all_warmup_times_pre_toggle['focused_kb_time'])
                all_warmup_times_pre_toggle['focused_kb_time'] += 5
                print(all_warmup_times_pre_toggle['focused_kb_time'])
            elif loaded_value == 'barbell':
                print(all_warmup_times_pre_toggle['focused_barbell_time'])
                all_warmup_times_pre_toggle['focused_barbell_time'] += 10
                print(all_warmup_times_pre_toggle['focused_barbell_time'])
            elif loaded_value == False and check_tough_gymnastics(todays_wod) == None:
                print(all_warmup_times_pre_toggle['focused_gymanstics_time'])
                all_warmup_times_pre_toggle['focused_gymanstics_time'] += 8
                print(all_warmup_times_pre_toggle['focused_gymanstics_time'])
        else:
            print('poocake')
        print(all_warmup_times_pre_toggle)
        all_warmup_times_post_toggle = all_warmup_times_pre_toggle

    return all_warmup_times_post_toggle