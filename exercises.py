def get_exercises():
    return new_exercise_dict



exercises = {

    ###GYMNASTICS

    'air squat': {
        'category': 'gymnastics lower',
        'intensity': 'high',
        'loaded': False
    },
    'push up': {
        'category': 'gymnastics upper',
        'intensity': 'high',
        'loaded': False
    },

    'burpee': {
        'category': 'gymnastics upper', 'gymnastics lower'
                                        'intensity': 'high',
        'loaded': False
    },

    'pull up': {
        'category': 'gymnastics upper',
        'intensity': 'high',
        'loaded': False
    },
    'sit up': {
        'category': 'gymnastics upper',
        'intensity': 'high',
        'loaded': False
    },

    'hollow rock': {
        'category': 'gymnastics upper',
        'intensity': 'high',
        'loaded': False
    },

    'mountain climber': {
        'category': 'gymnastics upper', 'gymnastics lower'
                                        'intensity': 'high',
        'loaded': False
    },

    'lunge': {
        'category': 'gymnastics lower',
        'intensity': 'high',
        'loaded': False
    },

    'jumping lunge': {
        'category': 'gymnastics lower',
        'intensity': 'high',
        'loaded': False
    },

    ###KETTLEBELLS

    'kettlebell swing': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },
    'goblet squat': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },

    'kettlebell snatch': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },

    'kettlebell clean': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },

    'kettlebell jerk': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },

    'kettlebell press': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },

    'turkish get up': {
        'category': 'kettlebells',
        'intensity': 'high',
        'loaded': 'kb'
    },

    ## KB or DB

    'kettlebell lunge': {
        'category': ['kettlebells', 'dumbbells'],
        'intensity': 'high',
        'loaded': 'kb'
    },
    'dumbbell lunge': {
        'category': ['kettlebells', 'dumbbells', ],
        'intensity': 'high',
        'loaded': 'kb'
    },

    ###BB SQUATS

    'squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'front squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'back squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'box squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'back pause squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'front box squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'front pause squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'high bar back squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'low bar back squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'overhead squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'split squat': {
        'category': 'squats',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'zurcher squat': {
        'category': 'squats',
        'intensity': 'high',
    },

    ###BB CLEANS

    'clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell',
        'tech': 'https://www.youtube.com/watch?v=DEZx3PmXU4c',
        'reg_warm': 'https://www.youtube.com/watch?v=1_IK2yYA3ig'

    },

    'power clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'squat clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'clean extension': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'clean pull': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'hang clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'hang power clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'hang squat clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'muscle clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'squat pause clean': {
        'category': 'cleans',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    ###PRESSES
    'bench press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell',
        'tech': 'youtubelink for techbench',
        'reg_warm': 'youtubelink for regwarmbench',
    },
    'floor press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'seated press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'strict press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'snatch grip push press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'sotts press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'shoulder press': {
        'category': 'presses',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    ###JERKS
    'jerk balance': {
        'category': 'jerks',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'jerk dip': {
        'category': 'jerks',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'push jerk': {
        'category': 'jerks',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'split jerk': {
        'category': 'jerks',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'squat jerk': {
        'category': 'jerks',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    ###SNATCHES
    'hang power snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'hang squat snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'power snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'muscle snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'snatch balance': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'snatch extension': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'snatch pull': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'squat pause snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },
    'squat snatch': {
        'category': 'snatches',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    ###DEADLIFTS
    'deadlift': {
        'category': 'deadlifts',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'romanian deadlift': {
        'category': 'deadlifts',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'snatch grip deadlift': {
        'category': 'deadlifts',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'stiff legged deadlift': {
        'category': 'deadlifts',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'sumo deadlift': {
        'category': 'deadlifts',
        'intensity': 'high',
        'loaded': 'barbell'
    },

    'sumo deadlift high pull': {
        'category': 'deadlifts',
        'intensity': 'high',
        'loaded': 'barbell'
    },

}
