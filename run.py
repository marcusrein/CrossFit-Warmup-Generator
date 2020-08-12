from appfolder import app

# JJ HELP TODOS
# TODO: NOT SECURE EMAIL at init.py. Cannot import enviornment varibles from bash? Weird!
# TODO: expanding to XL messes with formatting
# TODO Padding on L of R big screen column does not respond
# TODO: better dropdowns/navbar ideas
#  TODO: * Get screen orientation to lock in portrait mode
# TODO: login with user database
#

# MDR TODOS
# TODO: Continue to update gifs/vids (ended on kb_warmups.py)
# TODO: Get all links to not be separate buttons but the title or image of the movement
# TODO: ONLY ONE CORE WARMUP IN DROMS
# TODO: Default selected length is "normal". Fix the way its carrying over after submit.
# TODO: need to differentiate olympic lift warmup and strength/squat warmup. If olympic lift is in 'easy' warm up one way, if olympic lift is 'tough' warm up another. If strength movement is combined with oly movement in a WOD...?
# TODO: need an overhead squat category. see barbellwarmups.py 'overhead squat warmup'
# TODO: If forced core exercise, only allow one core exercise in output (line 62 getters.py)


# LONG TERM TODOS:
# TODO: add draggable inputs
# TODO: Create banded section.
# TODO: 1. Create DB category throughout code, 2. fix bug in index.html that doubles-up input (it lookslike
#  I can put in airsquat 2x) 3. create 'equipment' thing. 4. have users log in


if __name__ == '__main__':
    app.run(debug=True)
