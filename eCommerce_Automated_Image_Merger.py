# python imports
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image

Tk().withdraw()
imFile = askopenfilename()

print("What shade is the shirt? Dark or Light?")
respShade = input()
print("What's the logo location? Right or Left?:")
respLocation = input()
print("Color abriv. name?")
respName = input()

shirt = Image.open(imFile)
shirt_01 = shirt.resize((1200, 1800))
shirt_02 = shirt.resize((1200, 1800))
shirt_03 = shirt.resize((1200, 1800))

if "ark" in respShade:
    logo_hfwl = Image.open("images/logos/randazzo/hfox-wht.png")
    logo_hfwl = logo_hfwl.resize((150, 80))
    logo_hrtw = Image.open("images/logos/randazzo/htld-wht.png")
    logo_hrtw = logo_hrtw.resize((150, 80))
    logo3_rzwl = Image.open("images/logos/randazzo/rand-wht.png")
    logo3_rzwl = logo3_rzwl.resize((150, 80))

    if "lef" in respLocation:
        shirt_01.paste(logo_hfwl, (660, 660), logo_hfwl)
        shirt_02.paste(logo_hrtw, (660, 660), logo_hrtw)
        shirt_03.paste(logo3_rzwl, (660, 660), logo3_rzwl)

    elif "rig" in respLocation:
        shirt_01.paste(logo_hfwl, (410, 660), logo_hfwl)
        shirt_02.paste(logo_hrtw, (410, 660), logo_hrtw)
        shirt_03.paste(logo3_rzwl, (410, 660), logo3_rzwl)

    shirt_01.save('images/final/' + respName + '-hfwl.jpg')
    shirt_02.save('images/final/' + respName + '-hrtw.jpg')
    shirt_03.save('images/final/' + respName + '-rwl.jpg')


if "ght" in respShade:
    logo_hfwl = Image.open("images/logos/randazzo/hfox.png")
    logo_hfwl = logo_hfwl.resize((150, 80))
    logo_hrtw = Image.open("images/logos/randazzo/htld.png")
    logo_hrtw = logo_hrtw.resize((150, 80))
    logo3_rzwl = Image.open("images/logos/randazzo/rand.png")
    logo3_rzwl = logo3_rzwl.resize((150, 80))

    if "lef" in respLocation:
        shirt_01.paste(logo_hfwl, (660, 660), logo_hfwl)
        shirt_02.paste(logo_hrtw, (660, 660), logo_hrtw)
        shirt_03.paste(logo3_rzwl, (660, 660), logo3_rzwl)

    elif "rig" in respLocation:
        shirt_01.paste(logo_hfwl, (410, 660), logo_hfwl)
        shirt_02.paste(logo_hrtw, (410, 660), logo_hrtw)
        shirt_03.paste(logo3_rzwl, (410, 660), logo3_rzwl)

    shirt_01.save('images/final/' + respName + '-hfcl.jpg')
    shirt_02.save('images/final/' + respName + '-hrtc.jpg')
    shirt_03.save('images/final/' + respName + '-rcl.jpg')

path = "images/final/"
path = os.path.realpath(path)
os.startfile(path)
