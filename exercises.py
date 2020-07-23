from collections import OrderedDict

# CURRENT CATEGORIES: 'cleans, 'core', 'deadlifts,' 'dumbbells', 'gymnastics lower', 'gymnastics upper', 'handstand',
# 'jerks, 'kettlebells','kettlebell olympic', 'kettlebell overhead', 'lunges', 'plyos', 'snatches', 'squats', 'swings'
#

# CATEGORIES TO ADD: rows, rings


### CATEGORY talks to DROMS.PY

exercises_dict = {
    # GYMNASTICS
    'air squat': {
        'category': ['gymnastics lower'],
        'loaded': False,
    },
    'burpee': {
        'category': ['gymnastics upper', 'gymnastics lower'],
        'loaded': False,
        'force drom': ['burpees']
    },
    'push up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['push ups']
    },
    'strict pull up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs']
    },
    'kipping pull up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs'],
        'force gymnastics': ['scap pull ups', 'kipping warm up']
    },
    'butterfly pull up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs'],

    },
    'chin up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs'],

    },
    'sit up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'hollow rock': {
        'category': ['gymnastics upper', 'core'],
        'loaded': False,
        'force drom': ['core rolling'],
    },
    'mountain climber': {
        'category': ['core'],
        'loaded': False,
        'force drom': ['down dog to up dog'],
    },
    'handstand': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],

    },
    'handstand pushup': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],

    },
    'handstand hold': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],

    },
    'box pike pushup': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],

    },
    'ring dip': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],

    },
    'ring muscle up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'bear crawls'],

    },
    'bar muscle up': {
        'category': ['gymnastics upper'],
        'loaded': False,
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],

    },
    'ring row': {
        'category': ['gymnastics upper'],
        'loaded': False
    },

    # KETTLEBELLS

    'kettlebell swing': {
        'category': ['kettlebells'],
        'loaded': 'kb'
    },
    'goblet squat': {
        'category': ['kettlebells'],
        'loaded': 'kb'
    },
    'kettlebell snatch': {
        'category': ['kettlebells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],

    },
    'kettlebell clean': {
        'category': ['kettlebells'],
        'loaded': 'kb'
    },
    'kettlebell jerk': {
        'category': ['kettlebells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],
    },
    'kettlebell press': {
        'category': ['kettlebells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],
    },
    'kettlebell romanian deadlift': {
        'category': ['kettlebells'],
        'loaded': 'kb'
    },
    'kettlebell single leg romanian deadlift': {
        'category': ['kettlebells'],
        'loaded': 'kb'
    },
    'turkish get up': {
        'category': ['kettlebells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges', 'core rolling'],
    },

    # DUMBBELLS

    'dumbbell swing': {
        'category': ['dumbbells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],
    },
    'dumbbell front squat': {
        'category': ['dumbbells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],
    },
    'dumbbell snatch': {
        'category': ['dumbbells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],
    },
    'dumbbell clean': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell jerk': {
        'category': ['dumbbells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges'],
    },
    'dumbbell press': {
        'category': ['dumbbells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'inchworms', 'thoracic bridges'],
    },
    'dumbbell romanian deadlift': {
        'category': ['dumbbells'],
        'loaded': 'kb',
    },
    'dumbbell single leg romanian deadlift': {
        'category': ['dumbbells'],
        'loaded': 'kb',
    },
    'dumbbell turkish get up': {
        'category': ['dumbbells'],
        'loaded': 'kb',
        'force drom': ['shoulder passthroughs', 'thoracic bridges', 'core rolling'],
},

    # LUNGES

    'lunge': {
        'category': ['lunges'],
        'loaded': False,
        'force drom': ['walking lunges', 'worlds greatest stretch']
    },
    'jumping lunge': {
        'category': ['lunges'],
        'loaded': False,
        'force drom': ['walking lunges', 'worlds greatest stretch']
    },
    'kettlebell lunge': {
        'category': ['lunges'],
        'loaded': 'kb',
        'force drom': ['walking lunges', 'worlds greatest stretch']
    },
    'dumbbell lunge': {
        'category': ['lunges'],
        'loaded': 'db',
        'force drom': ['walking lunges', 'worlds greatest stretch']
    },
    'barbell lunge': {
        'category': ['lunges'],
        'loaded': 'barbell',
        'force drom': ['walking lunges', 'worlds greatest stretch']
    },

    # SQUATS

    'squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'worlds greatest stretch'],

},
    'front squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],
    },
    'back squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'worlds greatest stretch'],
    },
    'box squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },
    'back pause squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'worlds greatest stretch'],
    },
    'front box squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch'],
    },
    'front pause squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'dead bugs', 'worlds greatest stretch'],
    },
    'high bar back squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch'],
    },
    'low bar back squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch'],
    },
    'overhead squat': {
        'category': ['squats', 'overhead squats'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'core rolling', 'inchworms', 'worlds greatest stretch'],
    },
    'split squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['walking lunges', 'worlds greatest stretch', 'inchworms'],
    },
    'zurcher squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },

    # CLEANS

    'clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'power clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

},
    'squat clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['banded side steps', 'air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'clean extension': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'clean pull': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

},
    'hang clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'hang power clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'hang squat clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'muscle clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },
    'squat pause clean': {
        'category': ['cleans'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs', 'worlds greatest stretch', 'inchworms'],

    },

    # PRESSES

    'bench press': {
        'category': ['saggital presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups']
    },
    'floor press': {
        'category': ['saggital presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups']

    },
    'seated press': {
        'category': ['overhead presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'down dog to up dog']

},
    'strict press': {
        'category': ['overhead presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'down dog to up dog']

},
    'snatch grip push press': {
        'category': ['overhead presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'down dog to up dog', 'thoracic bridges']

},
    'sotts press': {
        'category': ['overhead presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'down dog to up dog', 'worlds greatest stretch', 'thoracic bridges']

    },
    'shoulder press': {
        'category': ['overhead presses'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'down dog to up dog', 'thoracic bridges']

},

    # JERKS

    'jerk balance': {
        'category': ['jerks'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'down dog to up dog', 'thoracic bridges']

    },
    'jerk dip': {
        'category': ['jerks'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog', 'thoracic bridges']

    },
    'push jerk': {
        'category': ['jerks'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                                 'thoracic bridges']

},
    'split jerk': {
        'category': ['jerks'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                       'thoracic bridges', 'walking lunges']
    },
    'squat jerk': {
        'category': ['jerks'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },

    # SNATCHES

    'hang power snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
    'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'hang squat snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
    'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'power snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
    'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'muscle snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
    'force drom': ['shoulder passthroughs', 'push ups', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
    'force drom': ['shoulder passthroughs', 'worlds greatest stretch', 'inchworms', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'snatch balance': {
        'category': ['snatches'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'worlds greatest stretch', 'inchworms', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'snatch extension': {
        'category': ['snatches'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'inchworms', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'snatch pull': {
        'category': ['snatches'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'inchworms', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'squat pause snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'worlds greatest stretch', 'inchworms', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },
    'squat snatch': {
        'category': ['snatches'],
        'loaded': 'barbell',
        'force drom': ['shoulder passthroughs', 'worlds greatest stretch', 'inchworms', 'core rolling', 'down dog to up dog',
                       'thoracic bridges']
    },

    # DEADLIFTS

    'deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell',
    'force drom': ['worlds greatest stretch', 'inchworms', 'core rolling']

    },
    'romanian deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell',
        'force drom': ['worlds greatest stretch', 'inchworms', 'core rolling']

    },
    'snatch grip deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell',
        'force drom': ['worlds greatest stretch', 'inchworms', 'core rolling']

    },
    'stiff legged deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell',
        'force drom': ['worlds greatest stretch', 'inchworms', 'core rolling']

    },
    'sumo deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell',
        'force drom': ['worlds greatest stretch', 'inchworms', 'core rolling']

    },
    'sumo deadlift high pull': {
        'category': ['deadlifts'],
        'loaded': 'barbell',
        'force drom': ['worlds greatest stretch', 'inchworms', 'core rolling']

    }
}

#
# for k in exercises:
#     del exercises[k]['intensity']
#
# print(exercises)

# for i in sorted (droms) :
#     print ((i, droms[i]), end =" ")
#

alpha = OrderedDict(sorted(exercises_dict.items(), key=lambda x: x[0]))

for k, v in alpha.items():
    print(k, v)

# for i, j in droms2.items():
#     sorted_dict = {i: sorted(j['categories'])}
#     print(sorted_dict)
