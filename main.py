from PIL import Image, ImageDraw, ImageFont

# TODO Add this to README.md
# Bot names in the txts should be seperated by newline characters.
# This should make it easy to just copy and paste from the sheet.

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

new_bots = []
moved_up = []
moved_down = []

# Loops through each bot in current standings.
for bot in current:
    # Finds if the bot is newly added.
    if bot not in previous:
        new_bots.append(bot)

    else:
        # Finds whether the bot moved and whether up or down.
        if current.index(bot) < previous.index(bot):
            moved_up.append(bot)
        elif current.index(bot) > previous.index(bot):
            moved_down.append(bot)

# Divisions
divisions = ('Quantum', 'Overclocked', 'Processor', 'Circuit', 'Transistor', 'Abacus', 'Babbage', 'Colossus', 'Dragon', 'ENIAC')

# Start positions for drawing.
start_x = 450
start_y = 90

# Bot name offsets from the division name position.
x_offset = -220
y_offset = 210

# Incremenets for x and y.
div_x_i = 1850
div_y_i = 790
bot_y_i = 140

# Opening image for drawing.
image = Image.open('Leaderboard_empty.png')
draw = ImageDraw.Draw(image)

# Fonts.
div_font = ImageFont.truetype('MontserratAlternates-Regular.ttf',120)
bot_font = ImageFont.truetype('MontserratAlternates-Regular.ttf',80)

# Colours.
div_colour = (255,255,255)
bot_colour = (0,0,0)

# For each divion, draw the division name, and each bot in the division.
for i, div in enumerate(divisions):
    # Calculates position for the division text.
    div_pos = (start_x + div_x_i * (i // 5), start_y + div_y_i * (i % 5))
    # Draws the division name.
    draw.text(xy=div_pos, text=div, fill=div_colour, font=div_font)

    # Loops through the four bots in the division and draws each.
    bot_i = i * 4
    for ii, bot in enumerate(current[bot_i : bot_i+4]):
        # Calculates position for the bot.
        bot_pos = (div_pos[0] + x_offset, div_pos[1] + y_offset + ii * bot_y_i)
        # Draws the bot name.
        draw.text(xy= bot_pos, text=bot, fill=bot_colour, font=bot_font)

        # TODO Add symbols for new bot, moving up, moving down.

# Shows and saves the image.
image.show()
image.save('Leaderboard.png')
