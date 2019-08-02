'''Generates the leader-board.'''

from PIL import Image, ImageDraw, ImageFont
from symbol_maker import colour_scheme

# ---------------------------------------------------------------

# LOADING STANDINGS:

# Getting previous week's standings from text file.
previous_txt = open('previous_week.txt', 'r')
previous = []
for line in previous_txt:
    previous.append(line.strip())
previous_txt.close()

# Getting current week's standings from text file.
current_txt = open('current_week.txt', 'r')
current = []
for line in current_txt:
    current.append(line.strip())
current_txt.close

# ---------------------------------------------------------------

# SYMBOL SUBLISTS:

# Creates lists to track which bots moved or which are new.
new_bots = []
moved_up = []
moved_down = []

# Loops through each bot in current standings.
for bot in current:
    # Finds if the bot is new.
    if bot not in previous:
        new_bots.append(bot)

    else:
        # Finds whether the bot moved and whether up or down.
        if current.index(bot) < previous.index(bot):
            moved_up.append(bot)
        elif current.index(bot) > previous.index(bot):
            moved_down.append(bot)

# Creates list for tracking who played last week.
played = []
# Gets last week's number and determines if it's odd or even.
even = (int(input('Last week number: ')) + 1) % 2 # 1 if week is even, 0 if week is odd.
# Adds bots who played last week to list.
for i in range(5):
    played += previous[i*8 + 4*even : i*8 + 4*even + 5]

# ---------------------------------------------------------------

# PARAMETERS FOR DRAWING:

# Divisions
divisions = ('Quantum', 'Overclocked', 'Processor', 'Circuit', 'Transistor', 'Abacus', 'Babbage', 'Colossus', 'Dragon', 'ENIAC')

# Start positions for drawing.
start_x = 540
start_y = 90

# Division emblem offsets from the division name position.
emb_x_offset = -530
emb_y_offset = -90

# Bot name offsets from the division name position.
bot_x_offset = -340
bot_y_offset = 210

# Offsets for the symbols from the bot name position.
sym_x_offset = 1300
sym_y_offset = 5

# Incremenets for x and y.
div_x_incr = 1790
div_y_incr = 790
bot_y_incr = 140

# ---------------------------------------------------------------

# DRAWING:

# Opening image for drawing.
leaderboard = Image.open('template/Leaderboard_empty.png')
draw = ImageDraw.Draw(leaderboard)

# Fonts.
div_font = ImageFont.truetype('MontserratAlternates-Regular.ttf',120)
bot_font = ImageFont.truetype('MontserratAlternates-Regular.ttf',80)

# Colours.
# div_colour = (255,255,255) # Now using colour_scheme instead
bot_colour = (0,0,0)

# For each divion, draw the division name, and each bot in the division.
for i, div in enumerate(divisions):

    # Calculates position for the division text.
    div_pos = (start_x + div_x_incr * (i // 5), start_y + div_y_incr * (i % 5))
    # Draws the division name.
    draw.text(xy=div_pos, text=div, fill=colour_scheme[div][0], font=div_font)

    # Draws the division emblem at an offset.
    try:
        # Opens the divicion emblem image.
        emblem = Image.open(f'emblems/{div}.png')
        # Calculates position of emblem.
        emb_pos = (div_pos[0] + emb_x_offset, div_pos[1] + emb_y_offset)
        # Pastes emblem onto image.
        leaderboard.paste(emblem, emb_pos, emblem)
    except:
        # Sends error message if it can't find the emblem.
        print(f'ERROR: Missing emblem for {div}.')

    # Loops through the four bots in the division and draws each.
    bot_index = i * 4
    for ii, bot in enumerate(current[bot_index : bot_index+4]):

        # Calculates position for the bot.
        bot_pos = (div_pos[0] + bot_x_offset, div_pos[1] + bot_y_offset + ii * bot_y_incr)
        # Draws the bot name.
        draw.text(xy= bot_pos, text=bot, fill=bot_colour, font=bot_font)

        # Calculates symbol position.
        sym_pos = (bot_pos[0] + sym_x_offset, bot_pos[1] + sym_y_offset)

        # Pastes appropriate symbol
        if bot in new_bots:
            symbol = Image.open(f'symbols/{div}_new.png')
            leaderboard.paste(symbol, sym_pos, symbol)

        elif bot in moved_up:
            symbol = Image.open(f'symbols/{div}_up.png')
            leaderboard.paste(symbol, sym_pos, symbol)

        elif bot in moved_down:
            symbol = Image.open(f'symbols/{div}_down.png')
            leaderboard.paste(symbol, sym_pos, symbol)

        elif bot in played:
            symbol = Image.open(f'symbols/{div}_played.png')
            leaderboard.paste(symbol, sym_pos, symbol)


# Shows and saves the image.
leaderboard.show()
leaderboard.save('Leaderboard.png', 'PNG')
