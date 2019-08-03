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
    'Transistor':   ((250,242,168),(218,207, 55),(158,150, 27)),
    'Abacus':       ((183,132,255),(123, 76,183),( 69, 43,134)),
    'Babbage':      ((224,130,145),(173, 65, 79),(134, 19, 36)),
    'Colossus':     ((114,181,234),( 70,121,174),( 41, 88,128)),
    'Dragon':       ((129,211,129),( 54,149, 60),( 37,102, 37)),
    'ENIAC':        ((255,227,135),(201,162, 69),(143,121, 45)),
    'Ferranti':     ((200,200,200),( 98, 98, 98),( 56, 56, 56)) 
}


def generate_symbols():
    """Creates symbols"""
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

def generate_legend():
    """Creates legend."""
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

