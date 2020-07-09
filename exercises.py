from collections import OrderedDict

exercises = {
    # GYMNASTICS
    'air squat': {
        'category': ['gymnastics lower', 'squats'],
        'loaded': False,
    },
    'burpee': {
        'category': ['gymnastics upper', 'gymnastics lower'],
        'loaded': False
    },
    'push up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'strict pull up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'kipping pull up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'butterfly pull up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'chin up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'sit up': {
        'category': ['gymnastics upper'],
        'loaded': False
    },
    'hollow rock': {
        'category': ['gymnastics upper', 'core'],
        'loaded': False
    },
    'mountain climber': {
        'category': ['core'],
        'loaded': False
    },
    'ring row': {
        'category': ['gymnastics upper'],
        'loaded': False
    },


    # KETTLEBELLS

    'kettlebell swing': {
        'category': ['kettlebells', 'swings'],
        'loaded': 'kb'
    },
    'goblet squat': {
        'category': ['kettlebells', 'kettlebell squats'],
        'loaded': 'kb'
    },
    'kettlebell snatch': {
        'category': ['kettlebells', 'kettlebell olympic'],
        'loaded': 'kb'
    },
    'kettlebell clean': {
        'category': ['kettlebells', 'kettlebell olympic'],
        'loaded': 'kb'
    },
    'kettlebell jerk': {
        'category': ['kettlebells', 'kettlebell olympic', 'kettlebell overhead'],
        'loaded': 'kb'
    },
    'kettlebell press': {
        'category': ['kettlebells', 'kettlebell overhead'],
        'loaded': 'kb'
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
        'loaded': 'kb'
    },

    # DUMBBELLS

    'dumbbell swing': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell front squat': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell snatch': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell clean': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell jerk': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell press': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell romanian deadlift': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell single leg romanian deadlift': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },
    'dumbbell turkish get up': {
        'category': ['dumbbells'],
        'loaded': 'kb'
    },

    # LUNGES

    'lunge': {
        'category': ['lunges'],
        'loaded': False
    },
    'jumping lunge': {
        'category': ['lunges', 'plyos'],
        'loaded': False
    },
    'kettlebell lunge': {
        'category': ['lunges'],
        'loaded': 'kb'
    },
    'dumbbell lunge': {
        'category': ['lunges'],
        'loaded': 'db'
    },
    'barbell lunge': {
        'category': ['lunges'],
        'loaded': 'barbell'
    },

    # SQUATS

    'squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'front squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'back squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'box squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'back pause squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'front box squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'front pause squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'high bar back squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'low bar back squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'overhead squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'split squat': {
        'category': ['squats'],
        'loaded': 'barbell'
    },
    'zurcher squat': {
        'category': ['squats']
    },

    # CLEANS

    'clean': {
        'category': ['cleans'],
        'loaded': 'barbell'
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
# alpha = OrderedDict(sorted(droms.items(), key=lambda x: x[0]))
#
# for k, v in alpha.items():
#     print(k, v)

# for i, j in droms2.items():
#     sorted_dict = {i: sorted(j['categories'])}
#     print(sorted_dict)
