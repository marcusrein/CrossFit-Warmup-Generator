# CURRENT CATEGORIES: 'cleans, 'core', 'deadlifts,' 'dumbbells', 'gymnastics lower', 'gymnastics upper', 'handstand',
# 'jerks, 'kettlebells','kettlebell olympic', 'kettlebell overhead', 'lunges', 'plyos', 'snatches', 'squats', 'swings'

# RPE ORGANIZATION
# rpe 1 = banded/warmup tools/pvc
# 2  = core
# 3 = bw droms (wgs, seal walks, inchworms)
# 4 = bw dynamics (kicking, walking stretches, burpees etc)
# 5 = full range motions (air squats
# 6 = plyos


droms_dict = {
    'air squats': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'snatches'],
        'time': 1,
        'reps': ['10-20 reps', '15-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://thumbs.gfycat.com/ParchedSpitefulDeviltasmanian-size_restricted.gif',
        'rpe': 5,
    },
    # 'ring dips (assisted or jumping)': {
    #     'categories': ['gymnastics upper', 'jerks', 'overhead presses', 'saggital presses', 'snatches'],
    #     'time': 1,
    #     'reps': ['10 forward, 10 backward', '20 forward, 20 backward','30 forward, 30 backward'],
    #     'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
    #     'img': 'https://data.whicdn.com/images/306295449/original.gif',
    #     'rpe': 1,
    # },
    'banded side steps': {
        'categories': ['cleans', 'deadlifts', 'jerks', 'lunges', 'snatches', 'squats', 'kettlebells'],
        'time': 1,
        'reps': ['20 reps', '30 reps', '40 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media4.s-nbcnews.com/j/newscms/2019_05/2738466/better_standing_lateral_band_walk_4a7c397f4668e1be769cc7b6bddc339f.fit-560w.gif ',
        'rpe': 1,
        'equipment': 'one band'
    },
    'bear crawls': {
        'categories': ['cleans', 'core', 'deadlifts', 'gymnastics upper', 'gymnastics lower', 'kettlebells',
                       'saggital presses', 'snatches', 'squats'],
        'time': 1,
        'reps': ['30s', '45s', '45s'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://tinyurl.com/yasf6uep',
        'rpe': 3,
    },
    'broad jumps': {
        'categories': ['cleans', 'jerks', 'kettlebells', 'plyos', 'snatches'],
        'time': 1,
        'reps': ['5-10 reps', '10-15 reps', '15-20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media3.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
        'rpe': 6,
    },
    'burpees': {
        'categories': ['gymnastics lower', 'gymnastics upper', 'saggital presses'],
        'time': 1,
        'reps': ['5 reps', '5-10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media3.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
        'rpe': 4,
    },
    'core rolling': {
        'categories': ['cleans', 'core', 'deadlifts', 'gymnastics upper', 'jerks', 'squats'],
        'time': 1,
        'reps': ['5 reps', '5-10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://i.imgur.com/dcwuwLs.gif',
        'rpe': 2,
    },
    'cossack lunges': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'kettlebells', 'lunges', 'squats'],
        'time': 1,
        'reps': ['15 reps', '15-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://tinyurl.com/yajsco2y',
        'rpe': 5,
    },
    'dead bugs': {
        'categories': ['cleans', 'core', 'deadlifts', 'gymnastics upper', 'jerks', 'squats'],
        'time': 1,
        'reps': ['15 reps', '15-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://thumbs.gfycat.com/DecentSarcasticAmethystsunbird-size_restricted.gif',
        'rpe': 2,
    },
    'down dog to up dog': {
        'categories': ['gymnastics lower', 'gymnastics upper', 'saggital presses'],
        'time': 1,
        'reps': ['5 reps', '5-10 reps', '10 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media1.popsugar-assets.com/files/thumbor/t2JA-yhWz775S2EFLvtdtaz2Fd8/fit-in/1024x1024/filters'
               ':format_auto-!!-:strip_icc-!!-/2013/12/16/734/n/1922729/b15fc22c292d8369_Tuck-Toe-Up-Dog.gif',
        'rpe': 3,
    },
    'frog walk': {
        'categories': ['cleans', 'snatches', 'squats'],
        'time': 1,
        'reps': ['30s', '45s', '45s'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://i.pinimg.com/originals/ca/f1/29/caf12983c2cfa59546814d3051f423df.gif',
        'rpe': 5,
    },
    'inchworms': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'gymnastics upper', 'kettlebells',
                       'overhead presses', 'saggital presses', 'squats'],
        'time': 1,
        'reps': ['3 reps', '3-5 reps', '5 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media1.giphy.com/media/UTXzXAwUHGx8MDEtPS/giphy-downsized.gif',
        'rpe': 3,
    },
    'push ups': {
        'categories': ['gymnastics upper', 'jerks', 'saggital presses', 'snatches'],
        'time': 1,
        'reps': ['10 reps', '10-15 reps', '15 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://thumbs.gfycat.com/GlossySkinnyDuckbillcat-small.gif',
        'rpe': 6,
    },
    # 'seal walk': {
    #     'categories': ['gymnastics upper', 'jerks', 'saggital presses'],
    #     'time': 1,
    #     'reps': ['30s', '1 min', '1 min'],
    #     'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
    #     'img': 'https://media.giphy.com/media/8Ag4AORS8xPYHdeU6f/giphy.gif',
    #     'rpe': 3,
    # },
    'shoulder passthroughs': {
        'categories': ['gymnastics upper', 'jerks', 'overhead presses', 'rows', 'saggital presses', 'snatches'],
        'time': 1,
        'reps': ['10 reps', '10-20 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://www.goldsgym.com/wp-content/uploads/sites/1/2019/10/PVC_min.gif',
        'rpe': 1,
        'equipment': 'pvc pipe'
    },
    'spidermans': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'snatches', 'squats'],
        'time': 1,
        'reps': ['30s', '45s', '45s'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media1.tenor.com/images/1d67a12af3ce871fd0601723bf86f5c2/tenor.gif?itemid=10818779',
        'rpe': 3,
    },
    'supermans': {
        'categories': ['core', 'deadlifts'],
        'time': 1,
        'reps': ['10-15 reps', '15-20 reps', '20-25 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media3.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
        'rpe': 2,
    },
    'thoracic bridges': {
        'categories': ['cleans', 'gymnastics upper', 'kettlebells', 'overhead presses', 'saggital presses', 'snatches'],
        'time': 1,
        'reps': ['3 each arm', '4 each arm', '5 each arm'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://jensinkler.com/wp-content/uploads/2019/06/Bodyweight-Thoracic-Bridge-With-Reach.gif',
        'rpe': 3,
    },
    'vertical jumps': {
        'categories': ['cleans', 'jerks', 'plyos', 'snatches'],
        'time': 1,
        'reps': ['10 reps', '15 reps', '20 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media3.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
        'rpe': 6,
    },
    'walking back kicks': {
        'categories': ['cleans', 'deadlifts', 'jerks', 'kettlebells', 'lunges', 'snatches', 'squats'],
        'time': 1,
        'reps': ['10-20 reps', '15-25 reps', '20-30 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://media.tenor.com/images/c50ca435dffdb837914e7cb32c1e7edf/tenor.gif',
        'rpe': 4,
    },
    'walking forward kicks': {
        'categories': ['cleans', 'deadlifts', 'jerks', 'kettlebells', 'lunges', 'snatches', 'squats'],
        'time': 1,
        'reps': ['10-20 reps', '15-25 reps', '20-30 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://i0.wp.com/thumbs.gfycat.com/MarvelousRespectfulLeech-size_restricted.gif?w=1155&h=840',
        'rpe': 4,
    },
    'walking lunges': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'kettlebells', 'lunges', 'squats'],
        'time': 1,
        'reps': ['10-15 reps', '15-20 reps', '20-30 reps'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://tinyurl.com/y8a86uhh',
        'rpe': 5,
    },
    'worlds greatest stretch': {
        'categories': ['cleans', 'deadlifts', 'gymnastics lower', 'gymnastics upper', 'lunges', 'snatches', 'squats', 'plyos'],
        'time': 1,
        'reps': ['3 each side', '4 each side', '5 each side'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://misterbackpain.com/wp-content/uploads/2020/01/worlds-greatest-stretch.gif',
        'rpe': 3,
    },
    'banded hip activation series': {
        'categories': ['cleans', 'deadlifts', 'lunges', 'snatches', 'squats'],
        'time': 1,
        'reps': ['10 reps each', '15 reps each', '20 reps each'],
        'url': 'https://www.youtube.com/watch?v=a8vaVbT_lX0',
        'img': 'https://thumbs.gfycat.com/DemandingDigitalGuanaco-mobile.mp4',
        'rpe': 1,
        'equipment': 'two bands'
    },
    'bootstrappers': {
        'categories': ['cleans', 'deadlifts', 'lunges', 'snatches', 'squats'],
        'time': 1,
        'reps': ['10 reps', '15 reps', '15 reps'],
        'url': 'https://www.youtube.com/watch?v=qxrQkR8H0Pg',
        'img': 'https://misterbackpain.com/wp-content/uploads/2020/01/worlds-greatest-stretch.gif',
        'rpe': 3,
    },
    'pvc front rack stretch': {
        'categories': ['cleans', 'deadlifts', 'snatches', 'jerks', 'squats'],
        'time': 1,
        'reps': ['30s hold', '45s hold', '45s hold'],
        'url': 'https://www.youtube.com/watch?v=iXgLGsyuUhY',
        'img': 'https://media0.giphy.com/media/fH3M6a0ssy9HxUtYVN/giphy.gif?cid=ecf05e478576e27904475e55b821e01d332928b340a77354&rid=giphy.gif',
        'rpe': 1,
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
