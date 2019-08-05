import symbols
import leaderboard

# ---------------------------------------------------------------

# PARAMETERS:

# Current week's number.
current_week = 3

# Extra 5 divisions?
extra = False

# Use background?
background = True

# Make a clip?
make_clip = False

# Duration of clip in seconds.
duration = 5.0

# Frames per second.
frames_per_second = 60

# Generate symbols and legend? (Set to False to skip it if you didn't make any changes to the pallete or templates)
gen_symbols = True

# ---------------------------------------------------------------

# RUNNING FUNCTIONS:

if gen_symbols:
    symbols.generate_symbols()
    symbols.generate_legend()

leaderboard.generate_leaderboard(current_week, extra, background, make_clip, duration, frames_per_second)