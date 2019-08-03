'''Generates the leader-board.'''

from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip

from symbols import palette

def generate_leaderboard(current_week, background=True, make_clip=False, duration=5.0, frames_per_second=60):
    """ Creates a leaderboard for league play.
    
    Arguments:
        current_week {int} -- Current week's number, e.g. 1, 2, 3, etc.
    
    Keyword Arguments:
        background {bool} -- Whether to use a background for the leaderboard. (default: {True})
        make_clip {bool} -- Whether to also make an mp4 clip. (default: {False})
        duration {float} -- Duration of the clip in seconds. (default: {5})
        frames_per_second {int} -- frames per second of the clip. (default: {60})
    """

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

    # Takes current week's number and determines if it's odd or even.
    even = current_week % 2 # 1 if week is even, 0 if week is odd.

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
    if background:
        leaderboard = Image.open('templates/Leaderboard_empty.png')
    else:
        leaderboard = Image.open('templates/Leaderboard_no_background.png')
    draw = ImageDraw.Draw(leaderboard)

    # Fonts for division titles and bot names.
    div_font = ImageFont.truetype('MontserratAlternates-Medium.ttf',120)
    bot_font = ImageFont.truetype('MontserratAlternates-Regular.ttf',80)

    # Bot name colour.
    bot_colour = (0,0,0)

    # For each divion, draw the division name, and each bot in the division.
    for i, div in enumerate(divisions):

        # Calculates position for the division text.
        div_pos = (start_x + div_x_incr * (i // 5), start_y + div_y_incr * (i % 5))
        # Draws the division name.
        draw.text(xy=div_pos, text=div, fill=palette[div][0], font=div_font)

        # Draws the division emblem at an offset.
        try:
            # Opens the division emblem image.
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

    if make_clip:
        # Saves a clip of the image.
        clip = ImageClip('Leaderboard.png').set_duration(duration)
        clip.write_videofile("Leaderboard.mp4",fps=frames_per_second)