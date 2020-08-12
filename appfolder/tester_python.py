import droms
import exercises
from fuzzywuzzy import fuzz

exercises = exercises.get_exercises()
warmups = droms.get_warmups()
warmup_metcons = droms.get_warmup_metcons()

#
# def check_exercise_fuzz_80(exercise1_prefuzz):
#     for j in list(exercises.keys()):
#         if (fuzz.ratio(exercise1_prefuzz, j)) > 80:
#             return j
#         else:
#             print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
#
# todays_wod = []
#
# exercise1_prefuzz = input('enter exercise1 prefuzz>>>\n\n>>>')
#
# # if check_exercise_fuzz_80(exercise1_prefuzz):
# #     todays_wod.append(exercise1_prefuzz)
# #     print(todays_wod)