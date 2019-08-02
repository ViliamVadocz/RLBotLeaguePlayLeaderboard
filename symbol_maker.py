'''Creates the symbol images and legend automatically.'''

from PIL import Image, ImageDraw, ImageFont

# Getting symbol shapes.
symbols = {
    # Symbol: (Image, description)
    'new':      (Image.open('template/new.png'), 'New bot'),
    'up':       (Image.open('template/up.png'), 'Rank up'),
    'down':     (Image.open('template/down.png'), 'Rank down'),
    'played':   (Image.open('template/played.png'), 'Played, but not moved'),
}


colour_scheme = {
    # Division: ((light_theme), (dark_theme))
    'Abacus':       ((139,108,216),( 85, 61,143)),
    'Babbage':      ((204,118,131),(137, 37, 52)),
    'Circuit':      ((134,247,131),( 61,150, 58)),
    'Colossus':     ((107,161,206),( 49,102,146)),
    'Dragon':       ((129,211,129),( 48,116, 48)),
    'ENIAC':        ((255,227,135),(183,159, 78)),
    'Overclocked':  ((204,100,105),(183, 51, 62)),
    'Processor':    (( 99,188,198),( 28,129,142)),
    'Quantum':      ((218,139,249),(134, 69,160)),
    'Transistor':   ((249,240,102),(193,183, 42))
}

# Creates symbols.
for div in colour_scheme:
    # Assigns light and dark themes for the division.
    light = Image.new('RGB', (80,80), colour_scheme[div][0])
    dark = Image.new('RGB', (80,80), colour_scheme[div][1])

    for symbol in symbols:
        # Creates blank image.
        image = Image.new('RGBA', (80, 80), (0, 0, 0, 0))

        # If the symbol is 'new' or 'up', use light theme.
        if symbol == 'new' or symbol == 'up':
            image.paste(light, (0,0), symbols[symbol][0])

        # Else use dark theme.        
        else:
            image.paste(dark, (0,0), symbols[symbol][0])

        # Saves symbol.
        image.save(f'symbols/{div}_{symbol}.png', 'PNG')

# Creating legend.
legend = Image.new('RGB', (500, 400), (0,0,0))
draw = ImageDraw.Draw(legend)
font_type = ImageFont.truetype('MontserratAlternates-Regular.ttf',32)

for i, symbol in enumerate(symbols):
    pos = (10, 100*i + 10)
    legend.paste(symbols[symbol][0], pos, symbols[symbol][0])
    draw.text(xy=(110,100*i+30), text=symbols[symbol][1], fill=(255,255,255), font=font_type)

legend.save('Legend.png', 'PNG')

