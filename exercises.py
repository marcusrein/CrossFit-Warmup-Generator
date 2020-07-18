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
        'force drom': ['walking lunges']
    },
    'jumping lunge': {
        'category': ['lunges'],
        'loaded': False,
        'force drom': ['walking lunges'],
    },
    'kettlebell lunge': {
        'category': ['lunges'],
        'loaded': 'kb',
        'force drom': ['walking lunges'],
    },
    'dumbbell lunge': {
        'category': ['lunges'],
        'loaded': 'db',
        'force drom': ['walking lunges'],
    },
    'barbell lunge': {
        'category': ['lunges'],
        'loaded': 'barbell',
        'force drom': ['walking lunges'],
    },

    # SQUATS

    'squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],

},
    'front squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs'],
    },
    'back squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },
    'box squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },
    'back pause squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },
    'front box squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs'],
    },
    'front pause squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'dead bugs'],
    },
    'high bar back squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },
    'low bar back squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
    },
    'overhead squat': {
        'category': ['squats', 'overhead squats'],
        'loaded': 'barbell',
        'force drom': ['air squats', 'core rolling', 'inchworms'],
    },
    'split squat': {
        'category': ['squats'],
        'loaded': 'barbell',
        'force drom': ['air squats'],
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
        'force drom': ['air squats', 'dead bugs'],

    },
    'power clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'squat clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'clean extension': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'clean pull': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'hang clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'hang power clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'hang squat clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'muscle clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },
    'squat pause clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
    },

    # PRESSES

    'bench press': {
        'category': ['saggital presses'],
        'loaded': 'barbell',
    },
    'floor press': {
        'category': ['saggital presses'],
        'loaded': 'barbell'
    },
    'seated press': {
        'category': ['overhead presses'],
        'loaded': 'barbell'
    },
    'strict press': {
        'category': ['overhead presses'],
        'loaded': 'barbell'
    },
    'snatch grip push press': {
        'category': ['overhead presses'],
        'loaded': 'barbell'
    },
    'sotts press': {
        'category': ['overhead presses'],
        'loaded': 'barbell'
    },
    'shoulder press': {
        'category': ['overhead presses'],
        'loaded': 'barbell'
    },

    # JERKS

    'jerk balance': {
        'category': ['jerks'],
        'loaded': 'barbell'
    },
    'jerk dip': {
        'category': ['jerks'],
        'loaded': 'barbell'
    },
    'push jerk': {
        'category': ['jerks'],
        'loaded': 'barbell'
    },
    'split jerk': {
        'category': ['jerks'],
        'loaded': 'barbell'
    },
    'squat jerk': {
        'category': ['jerks'],
        'loaded': 'barbell'
    },

    # SNATCHES

    'hang power snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'hang squat snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'power snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'muscle snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'snatch balance': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'snatch extension': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'snatch pull': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'squat pause snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },
    'squat snatch': {
        'category': ['snatches'],
        'loaded': 'barbell'
    },

    # DEADLIFTS

    'deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell'
    },
    'romanian deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell'
    },
    'snatch grip deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell'
    },
    'stiff legged deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell'
    },
    'sumo deadlift': {
        'category': ['deadlifts'],
        'loaded': 'barbell'
    },
    'sumo deadlift high pull': {
        'category': ['deadlifts'],
        'loaded': 'barbell'
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
