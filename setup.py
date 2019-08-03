'''Creates the images used to construct the leaderboard.'''

from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Getting symbol shapes.
symbols = {
    # Symbol: (Image, description)
    'new':      (Image.open('templates/new.png'), 'New bot'),
    'up':       (Image.open('templates/up.png'), 'Rank up'),
    'down':     (Image.open('templates/down.png'), 'Rank down'),
    'played':   (Image.open('templates/played.png'), 'Played, but not moved'),
}


# Colour scheme for each division.
palette = {
    # Division: ((light), (normal), (dark)) -> RGB values
    'Quantum':      ((218,139,249),(168, 85,200),( 99, 32,135)),
    'Overclocked':  ((246,138,156),(206, 69, 90),(150, 11, 11)),
    'Processor':    (( 82,220,234),( 55,151,194),( 20, 98,117)),
    'Circuit':      ((134,247,131),( 59,186, 57),( 26,104, 24)),
    'Transistor':   ((255,245,135),(218,207, 55),(158,150, 27)),
    'Abacus':       ((183,132,255),(123, 76,183),( 69, 43,134)),
    'Babbage':      ((224,130,145),(173, 65, 79),(134, 19, 36)),
    'Colossus':     ((114,181,234),( 70,121,174),( 41, 88,128)),
    'Dragon':       ((129,211,129),( 54,149, 60),( 37,102, 37)),
    'ENIAC':        ((255,227,135),(201,162, 69),(143,121, 45)) 
}


'''
# I tried to use the value shifting but it didn't give good resutls.
from colorsys import hsv_to_rgb

# Base colour for each division. Light and dark are made by shifting V.
base_colours = {
    # Division: (H, S, V)
    'Quantum':      (283, 45, 83),
    'Overclocked':  (350, 54, 83),
    'Processor':    (187, 80, 76),
    'Circuit':      (119, 59, 81),
    'Transistor':   ( 55, 72, 87),
    'Abacus':       (266, 53, 71),
    'Babbage':      (352, 53, 69),
    'Colossus':     (210, 52, 68),
    'Dragon':       (123, 48, 64),
    'ENIAC':        ( 42, 57, 85)     
}

val_shift = 0.30

for div in base_colours:
    # Looks at base colour for the division.
    colour = base_colours[div]
    colour = (colour[0]/360, colour[1]/100, colour[2]/100)

    # Converts HSV to RGB.
    normal = hsv_to_rgb(colour[0], colour[1], colour[2])
    normal = (normal[0]*255, normal[1]*255, normal[2]*255)
    normal = tuple([int(value) for value in normal])

    # Makes light version and does fancy conversion.
    light = hsv_to_rgb(colour[0], colour[1] , colour[2] + val_shift)
    light = (light[0]*255, light[1]*255, light[2]*255)
    light = tuple([int(value) for value in light])

    # Makes dark version and does fancy conversion.
    dark = hsv_to_rgb(colour[0], colour[1] , colour[2] - val_shift)
    dark = (dark[0]*255, dark[1]*255, dark[2]*255)
    dark = tuple([int(value) for value in dark])

    # Saves the colours to palette.
    palette[div] = (light,normal,dark)
'''

# Creates symbols.
for div in palette:
    # TODO Do this with numpy to preserve alpha

    # Makes new images which are all one colour.
    light   = palette[div][0]
    normal  = palette[div][1]
    dark    = palette[div][2]

    for symbol in symbols:
        # Changes symbol to numpy array containing RGBA for every pixel.
        data = np.array( symbols[symbol][0].convert('RGBA') )

        # Seperating RGBA for clarity.
        red, green, blue, alpha = data.T

        # Creates array of True or False for which pixels are white.
        white = (red == 255) & (green == 255) & (blue == 255)

        # Choses appropriate colour depending on symbol.
        if symbol == 'down':
            colour = dark
        else:
            colour = light

        # Assigns white pixels to colour
        data[..., :-1][white.T] = colour

        # Reconstructs image from array of pixel values.
        image = Image.fromarray(data)

        # Saves symbol to file.
        image.save(f'symbols/{div}_{symbol}.png', 'PNG')


# Creating legend.
legend = Image.new('RGB', (500, 400), (0,0,0))
draw = ImageDraw.Draw(legend)
font_type = ImageFont.truetype('MontserratAlternates-Regular.ttf',32)

# Pastes symbol template and draws help text.
for i, symbol in enumerate(symbols):
    pos = (10, 100*i + 10)
    legend.paste(symbols[symbol][0], pos, symbols[symbol][0])
    draw.text(xy=(110,100*i+30), text=symbols[symbol][1], fill=(255,255,255), font=font_type)

# Saves legend to file.
legend.save('Legend.png', 'PNG')

