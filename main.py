import leaderboard

# Current week's number.
current_week = 2

# Use background?
background = True

# Make a clip?
make_clip = False

# Duration of clip in seconds.
duration = 5.0

# Frames per second.
frames_per_second = 60

leaderboard.generate_leaderboard(current_week, background, make_clip, duration, frames_per_second)