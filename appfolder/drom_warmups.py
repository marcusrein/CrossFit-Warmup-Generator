# CURRENT CATEGORIES: 'cleans, 'core', 'deadlifts,' 'dumbbells', 'gymnastics lower', 'gymnastics upper', 'handstand',
# 'jerks, 'kettlebells','kettlebell olympic', 'kettlebell overhead', 'lunges', 'plyos', 'snatches', 'squats', 'swings'
# 'dumbbells snatch','dumbbells clean', 'dumbbells deadlift','dumbbells overhead',
#                        'dumbbells squat', 'dumbbells', 'dumbbells core'


# RPE ORGANIZATION
# rpe 0 =pvc
# 1 = bands
# 2 = activation without equipment
# 3  = core
# 4 = bw droms (wgs, seal walks, inchworms)
# 5 = bw dynamics (kicking, walking stretches, burpees etc)
# 6 = full range motions (air squats
# 7 = plyos


droms_dict = {
    'air squats': {
        'categories': ['dumbbells squat', 'dumbbells clean', 'dumbbells snatch', 'cleans', 'deadlifts',
                       'gymnastics lower', 'snatches'],
        'time': 1,
        'reps': ['5-10 reps', '10-15 reps', '10-15 reps'],
        'url': 'https://www.youtube.com/watch?v=C_VtOYc6j5c',
        'img': 'https://thumbs.gfycat.com/ParchedSpitefulDeviltasmanian-size_restricted.gif',
        'rpe': 6,
        'equipment': 'none'
    },
    # 'ring dips (assisted or jumping)': {
    #     'categories': ['gymnastics upper', 'jerks', 'overhead presses', 'saggital presses', 'snatches'],
    #     'time': 1,
    #     'reps': ['10 forward, 10 backward', '20 forward, 20 backward','30 forward, 30 backward'],
    #     'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
    #     'img': 'https://data.whicdn.com/images/306295449/original.gif',
    #     'rpe': 1,
    #         'equipment': 'none'

    # },
    'banded side steps': {
        'categories': ['dumbbells squat', 'dumbbells clean', 'dumbbells snatch', 'cleans', 'deadlifts', 'jerks',
                       'lunges', 'snatches', 'squats', 'kettlebells'],
        'time': 1,
        'reps': ['20 reps', '30 reps', '40 reps'],
        'url': 'https://www.youtube.com/watch?v=5wUk8wQNUT8',
        'img': 'https://media4.s-nbcnews.com/j/newscms/2019_05/2738466/better_standing_lateral_band_walk_4a7c397f4668e1be769cc7b6bddc339f.fit-560w.gif',
        'rpe': 1,
        'equipment': 'loop resistance band'
    },
    'bear crawls': {
        'categories': ['cleans', 'core', 'deadlifts', 'gymnastics upper', 'gymnastics lower', 'kettlebells',
                       'saggital presses', 'snatches', 'squats', 'dummbells snatch', 'dumbbells core',
                       'dumbbells overhead'],
        'time': 1,
        'reps': ['30s', '45s', '45s'],
        'url': 'https://youtu.be/XPRO_L0-Wjw?t=9',
        'img': 'https://tinyurl.com/yasf6uep',
        'rpe': 4,
        'equipment': 'none'

    },
    'broad jumps': {
        'categories': ['cleans', 'jerks', 'kettlebells', 'plyos', 'snatches', 'swings', 'dumbbells clean',
                       'dumbbells snatch'],
        'time': 1,
        'reps': ['5-10 reps', '10-15 reps', '15-20 reps'],
        'url': 'https://youtu.be/96zJo3nlmHI?t=3',
        'img': 'https://j.gifs.com/1WAVLR.gif',
        'rpe': 7,
        'equipment': 'none'

    },
    'burpees': {
        'categories': ['gymnastics lower', 'gymnastics upper', 'saggital presses', 'dumbbells core'],
        'time': 1,
        'reps': ['5 reps', '5-10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=auBLPXO8Fww',
        'img': 'https://c.tenor.com/u2-VJiigKCkAAAAC/exercise-jump.gif',
        'rpe': 5,
        'equipment': 'none'

    },
    'core rolling': {
        'categories': ['cleans', 'core', 'deadlifts', 'gymnastics upper', 'jerks', 'squats', 'dumbbells core',
                       'dumbbells snatch',
                       'dummbells clean', 'dumbbells squat', 'dumbbells deadlift'],
        'time': 1,
        'reps': ['5 reps', '5-10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=cp6zN-xtp-M',
        'img': 'https://j.gifs.com/0YzAKv.gif',
        'rpe': 3,
        'equipment': 'none'

    },
    'cossack lunges': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'kettlebells', 'lunges', 'squats', 'dumbbells squat',
                       'dumbbells snatch', 'dumbbells clean'],
        'time': 1,
        'reps': ['15 reps', '15-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=J5GKEt2H4SU',
        'img': 'https://tinyurl.com/yajsco2y',
        'rpe': 6,
        'equipment': 'none'

    },
    'dead bugs': {
        'categories': ['cleans', 'core', 'deadlifts', 'gymnastics upper', 'jerks', 'squats', 'dumbbells core',
                       'dumbbells squat', 'dumbbells snatch', 'dumbbells clean', 'dumbbells deadlift'],
        'time': 1,
        'reps': ['15 reps', '15-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=g_BYB0R-4Ws&t=2s',
        'img': 'https://j.gifs.com/p85936.gif',
        'rpe': 3,
        'equipment': 'none'

    },
    'down dog to up dog': {
        'categories': ['gymnastics lower', 'gymnastics upper', 'saggital presses', 'dumbbells overhead',
                       'kettlebells overhead', 'jerks', 'snatches'],
        'time': 1,
        'reps': ['5 reps', '5-10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=j6UIpShRtkA',
        'img': 'https://media1.popsugar-assets.com/files/thumbor/t2JA-yhWz775S2EFLvtdtaz2Fd8/fit-in/1024x1024/filters'
               ':format_auto-!!-:strip_icc-!!-/2013/12/16/734/n/1922729/b15fc22c292d8369_Tuck-Toe-Up-Dog.gif',
        'rpe': 4,
        'equipment': 'none'

    },
    'frog walk': {
        'categories': ['cleans', 'snatches', 'squats'],
        'time': 1,
        'reps': ['5 reps', '10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=CUq6-N_H2FU',
        'img': 'https://j.gifs.com/ANk8Vz.gif',
        'rpe': 6,
        'equipment': 'none'

    },
    'goddess squats': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'kettlebells', 'lunges', 'squats', 'dumbbells squat',
                       'dumbbells snatch', 'dumbbells clean'],
        'time': 1,
        'reps': ['4 each side', '5 each side', '6 each side'],
        'url': 'https://www.youtube.com/watch?v=QhAIq42EipE',
        'img': 'https://j.gifs.com/1WZP0V.gif',
        'rpe': 4,
        'equipment': 'none'

    },
    'inchworms': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'gymnastics upper', 'kettlebells',
                       'overhead presses', 'saggital presses', 'squats', 'dumbbells snatch', 'dumbbells clean',
                       'dumbbells squat'],
        'time': 1,
        'reps': ['3 reps', '3-5 reps', '5 reps'],
        'url': 'https://www.youtube.com/watch?v=0HFXsIMKqUg',
        'img': 'https://j.gifs.com/Mwz7r3.gif',
        'rpe': 4,
        'equipment': 'none'

    },
    'loop band shoulder activation': {
        'categories': ['gymnastics upper', 'jerks', 'overhead presses', 'rows', 'saggital presses', 'snatches',
                       'kettlebells overhead', 'dumbbells overhead', 'dumbbells snatch'],
        'time': 1,
        'reps': ['3/3', '5/5', '7/7'],
        'url': 'https://www.youtube.com/watch?v=fZ4i8lI-xWI',
        'img': 'https://j.gifs.com/XLK2Z5.gif',
        'rpe': 1,
        'equipment': 'loop resistance band'
    },
    'push ups': {
        'categories': ['gymnastics upper', 'jerks', 'saggital presses', 'snatches', 'dumbbells core'],
        'time': 1,
        'reps': ['10 reps', '10-15 reps', '15 reps'],
        'url': 'https://www.youtube.com/watch?v=0pkjOk0EiAk',
        'img': 'https://j.gifs.com/VAMJE1.gif',
        'rpe': 7,
        'equipment': 'none'

    },
    'reach roll and lift': {
        'categories': ['gymnastics upper', 'jerks', 'overhead presses', 'snatches', 'dumbbells overhead',
                       'dumbbells snatch'],
        'time': 1,
        'reps': ['10 each side', '10-15 each side', '15 each side'],
        'url': 'https://www.youtube.com/watch?v=NZiCSWiL7m8',
        'img': 'https://j.gifs.com/p8AlyV.gif',
        'rpe': 2,
        'equipment': 'pvc pipe'
    },
    'shoulder passthroughs': {
        'categories': ['gymnastics upper', 'jerks', 'overhead presses', 'rows', 'saggital presses', 'snatches',
                       'kettlebells overhead', 'dumbbells overhead', 'dumbbells snatch'],
        'time': 1,
        'reps': ['10 reps', '10-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=MrKIfj397Gw',
        'img': 'https://j.gifs.com/1WAV8j.gif',
        'rpe': 0,
        'equipment': 'pvc pipe'
    },
    'spidermans': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'snatches', 'squats', 'dumbbells squat', 'core'],
        'time': 1,
        'reps': ['30s', '45s', '45s'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media1.tenor.com/images/1d67a12af3ce871fd0601723bf86f5c2/tenor.gif?itemid=10818779',
        'rpe': 4,
        'equipment': 'none'

    },
    'supermans': {
        'categories': ['core', 'deadlifts'],
        'time': 1,
        'reps': ['10-15 reps', '15-20 reps', '20-25 reps'],
        'url': 'https://youtu.be/z6PJMT2y8GQ?t=12',
        'img': 'https://j.gifs.com/gZ47g6.gif',
        'rpe': 3,
        'equipment': 'none'

    },
    'thoracic bridges': {
        'categories': ['cleans', 'gymnastics upper', 'kettlebells', 'overhead presses', 'saggital presses', 'snatches',
                       'dumbbells overhead', 'dumbbells snatch'],
        'time': 1,
        'reps': ['3 each arm', '4 each arm', '5 each arm'],
        'url': 'https://www.youtube.com/watch?v=RkUAm8o7ab4',
        'img': 'https://jensinkler.com/wp-content/uploads/2019/06/Bodyweight-Thoracic-Bridge-With-Reach.gif',
        'rpe': 4,
        'equipment': 'none'

    },
    'vertical jumps': {
        'categories': ['cleans', 'jerks', 'plyos', 'snatches', 'dumbbell cleans', 'dumbbells snatches'],
        'time': 1,
        'reps': ['10 reps', '15 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media3.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
        'rpe': 7,
        'equipment': 'none'

    },
    'walking back kicks': {
        'categories': ['cleans', 'deadlifts', 'jerks', 'kettlebells', 'lunges', 'snatches', 'squats', 'dumbbells clean',
                       'dumbbells snatch'],
        'time': 1,
        'reps': ['10-20 reps', '15-25 reps', '20-30 reps'],
        'url': 'https://www.youtube.com/watch?v=U-nRt31Ynk4',
        'img': 'https://j.gifs.com/oV4AqK.gif',
        'rpe': 5,
        'equipment': 'none'

    },
    'toy soldiers': {
        'categories': ['cleans', 'deadlifts', 'jerks', 'kettlebells', 'lunges', 'snatches', 'squats', 'dumbbells clean',
                       'dumbbells snatch'],
        'time': 1,
        'reps': ['10-20 reps', '15-25 reps', '20-30 reps'],
        'url': 'https://www.youtube.com/watch?v=cIqzwOUilR4',
        'img': 'https://j.gifs.com/q74Avr.gif',
        'rpe': 5,
        'equipment': 'none'

    },
    'birdpeckers': {
        'categories': ['cleans', 'deadlifts', 'jerks', 'kettlebells', 'lunges', 'snatches', 'squats', 'dumbbells clean',
                       'dumbbells snatch'],
        'time': 1,
        'reps': ['10-15 reps', '15 reps', '15-20 reps'],
        'url': 'https://www.youtube.com/watch?v=we-V2WKe1YI',
        'img': 'https://j.gifs.com/mOxgD9.gif',
        'rpe': 5,
        'equipment': 'none'

    },
    'walking lunges': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'kettlebells', 'lunges', 'squats'],
        'time': 1,
        'reps': ['10-15 reps', '10-15 reps', '15-20 reps'],
        'url': 'https://www.youtube.com/watch?v=L8fvypPrzzs',
        'img': 'https://j.gifs.com/E8oK5k.gif',
        'rpe': 6,
        'equipment': 'none'

    },
    'worlds greatest stretch': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'gymnastics upper', 'lunges', 'snatches', 'squats',
                       'plyos', 'dumbbells clean', 'dumbbells squat'],
        'time': 1,
        'reps': ['3 each side', '4 each side', '5 each side'],
        'url': 'https://www.youtube.com/watch?v=-CiWQ2IvY34',
        'img': 'https://j.gifs.com/OMBJrN.gif',
        'rpe': 4,
        'equipment': 'none'

    },
    'monkey': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'gymnastics upper', 'snatches', 'squats',
                       'dumbbells squat'],
        'time': 1,
        'reps': ['5 each way', '7 each way', '9 each way'],
        'url': 'https://www.youtube.com/watch?v=xtkyY-ALDNI',
        'img': 'https://j.gifs.com/GvmoBL.gif',
        'rpe': 6,
        'equipment': 'none'

    },
    'banded hip activation series': {
        'categories': ['cleans', 'deadlifts', 'lunges', 'snatches', 'squats', 'dumbbells clean', 'dumbbells snatch',
                       'dumbbells squat'],
        'time': 1,
        'reps': ['10 reps each', '15 reps each', '20 reps each'],
        'url': 'https://www.youtube.com/watch?v=l4hb5Md7i_I',
        'img': 'https://j.gifs.com/ANk8GP.gif',
        'rpe': 1,
        'equipment': 'loop resistance band'
    },
    'bootstrappers': {
        'categories': ['cleans', 'deadlifts', 'lunges', 'snatches', 'squats', 'dumbbells clean', 'dumbbells snatch',
                       'dumbbells squat'],
        'time': 1,
        'reps': ['5 reps', '10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=KSpAvJfdgh4',
        'img': 'https://j.gifs.com/2xBGVv.gif',
        'rpe': 4,
        'equipment': 'none'

    },
    'pvc front rack stretch': {
        'categories': ['cleans', 'deadlifts', 'snatches', 'jerks', 'squats'],
        'time': 1,
        'reps': ['30s hold', '45s hold', '45s hold'],
        'url': 'https://www.youtube.com/watch?v=iXgLGsyuUhY',
        'img': 'https://j.gifs.com/yog606.gif',
        'rpe': 0,
        'equipment': 'pvc pipe'
    },
}
# I USED THIS CODE TO ALPHABATIZE MY OLD DICT THAT IS NOW {DROMS} ##

from collections import OrderedDict

# for i in sorted (droms) :
#     print ((i, droms[i]), end =" ")
#
# alpha = OrderedDict(sorted(droms.items(), key=lambda x: x[0]))
#
# for k, v in alpha.items():
#     print(k, v)

# for i, j in droms2.items():
#     sorted_dict = {i: sorted(j['categories'])}
#     print(sorted_dict)
