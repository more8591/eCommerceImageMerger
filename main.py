# Automating Tasks for Propago
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
import os
import time
import pyautogui
from login_screen import login_screen

#######################
# CLIENT WEBSITES

wbAbr = {
    "allied": "AAG",
    "carrier": "CE",
    "cc holdings": "CCH",
    "cooling": "LP",
    "envigo": "ENV",
    "Equita": "EFES",
    "FHLBI": "FHLBI",
    "flaherty": "FCP",
    "get involved": "GI",
    "gw berkheimer": "GWB",
    "herff jones": "HJ",
    "inbound": "IBO",
    "lennox awards": "LNXA",
    "lennox stores": "LS",
    "lifeomic": "LOG",
    "online transport": "OLTR",
    "pac van": "PV",
    "randazzo": "RAND",
    "sigma": "STTI",
    "trueblood": "TRE",
    "worrell gear": "WORG",
    "york gear": "YG"
}

fullName = {
    "AAG": "Allied Air Gear",
    "CE": "Carrier Enterprise",
    "CCH": "CC Holdings",
    "LP": "Lennox Promos",
    "ENV": "Envigo",
    "EFES": "Equita",
    "FHLBI": "FHLBI",
    "FCP": "flaherty",
    "GI": "Get Involved",
    "GWB": "GW Berkheimer",
    "HJ": "Herff Jones",
    "IBO": "Inbound Back Office",
    "LNXA": "Lennox Awards",
    "LS": "Lennox Stores",
    "LOG": "LifeOmic",
    "OLTR": "Online Transport",
    "PV": "PacVan",
    "RAND": "Randazzo",
    "STTI": "Sigma",
    "TRE": "Trueblood",
    "WORG": "Worrell Gear",
    "YG": "York Gear"
}

strLoc = {
    "allied air gear": (120, 325),
    "carrier enterprise": (120, 355),
    "cc holdings": (120, 385),
    "lennox promos": (120, 415),
    "envigo": (120, 440),
    "equita": (120, 470),
    "FHLBI": (120, 495),
    "flaherty": (120, 520),
    "get involved": (120, 540),
    "gw berkheimer": (120, 575),
    "herff jones": (120, 625),
    "inbound back office": (120, 655),
    "lennox awards": (120, 685),
    "lennox stores": (120, 705),
    "online transport": (120, 735),
    "pacvan": (120, 765),
    "lifeomic": (120, 715),
    "randazzo": (120, 785),
    "sigma": (120, 815),
    "trueblood": (120, 840),
    "worrell gear": (120, 920),
    "york gear": (120, 950)
}

#######################


mDo = ["1) Login", "2) Make Images", "3) TEST"]
propDo = ["1) Create Product", "2) Bulk Upload Images", "3) Add Master Image"]

print("WELCOME")
print(*mDo, sep="\n")
mResp = input()


def terminal_menu():
    if "1" in mResp:
        login_screen()
    elif "2" in mResp:
        make_images()
    elif "3" in mResp:
        print("NOW TESTING")

        # INSERT TEST CODE
        pyautogui.moveTo(1000, 160)

        print("TEST SUCCESS!")

        # IMAGE REGCONITION
        # imlogin = Image.open("images/test2.JPG")
        # imtest = pyautogui.locateOnScreen(imlogin, confidence=.8)
        # print(imtest)
        # pyautogui.click(imtest)


def inner_menu():
    print("TERMINAL OPTIONS")
    print(*propDo, sep="\n")

    myResp = input()

    if "1" in myResp:
        print("OPTION IN DEVELOPMENT")
        time.sleep(2)
        print("CLOSING PROGRAM.")
    elif "2" in myResp:
        bulk_upload_img()
    elif "3" in myResp:
        mstr_imupload()


def make_images():
    Tk().withdraw()
    imFile = askopenfilename()

    print("What shade is the shirt? Dark or Light?")
    respShade = input()
    print("What's the logo location? Right or Left?:")
    respLocation = input()
    print("Color abriv. name?")
    respName = input()

    shirtsizex = 1400
    shirtsizey = 1800

    lsizex = 760
    lsizey = 680
    rsizex = 410
    rsizey = 660

    logosizex = 150
    logosizey = 80

    shirt = Image.open(imFile)
    shirt_01 = shirt.resize((shirtsizex, shirtsizey))
    shirt_02 = shirt.resize((shirtsizex, shirtsizey))
    shirt_03 = shirt.resize((shirtsizex, shirtsizey))

    if "ark" in respShade:
        logo_hfwl = Image.open("images/logos/randazzo/hfox-wht.png")
        logo_hfwl = logo_hfwl.resize((logosizex, logosizey))
        logo_hrtw = Image.open("images/logos/randazzo/htld-wht.png")
        logo_hrtw = logo_hrtw.resize((logosizex, logosizey))
        logo3_rzwl = Image.open("images/logos/randazzo/rand-wht.png")
        logo3_rzwl = logo3_rzwl.resize((logosizex, logosizey))

        if "lef" in respLocation:
            shirt_01.paste(logo_hfwl, (lsizex, lsizey), logo_hfwl)
            shirt_02.paste(logo_hrtw, (lsizex, lsizey), logo_hrtw)
            shirt_03.paste(logo3_rzwl, (lsizex, lsizey), logo3_rzwl)

        elif "rig" in respLocation:
            shirt_01.paste(logo_hfwl, (rsizex, rsizey), logo_hfwl)
            shirt_02.paste(logo_hrtw, (rsizex, rsizey), logo_hrtw)
            shirt_03.paste(logo3_rzwl, (rsizex, rsizey), logo3_rzwl)

        shirt_01.save('images/final/' + respName + '-hfwl.jpg')
        shirt_02.save('images/final/' + respName + '-hrtw.jpg')
        shirt_03.save('images/final/' + respName + '-rwl.jpg')

    if "ght" in respShade:
        logo_hfwl = Image.open("images/logos/randazzo/hfox.png")
        logo_hfwl = logo_hfwl.resize((logosizex, logosizey))
        logo_hrtw = Image.open("images/logos/randazzo/htld.png")
        logo_hrtw = logo_hrtw.resize((logosizex, logosizey))
        logo3_rzwl = Image.open("images/logos/randazzo/rand.png")
        logo3_rzwl = logo3_rzwl.resize((logosizex, logosizey))

        if "lef" in respLocation:
            shirt_01.paste(logo_hfwl, (lsizex, lsizey), logo_hfwl)
            shirt_02.paste(logo_hrtw, (lsizex, lsizey), logo_hrtw)
            shirt_03.paste(logo3_rzwl, (lsizex, lsizey), logo3_rzwl)

        elif "rig" in respLocation:
            shirt_01.paste(logo_hfwl, (rsizex, rsizey), logo_hfwl)
            shirt_02.paste(logo_hrtw, (rsizex, rsizey), logo_hrtw)
            shirt_03.paste(logo3_rzwl, (rsizex, rsizey), logo3_rzwl)

        shirt_01.save('images/final/' + respName + '-hfcl.jpg')
        shirt_02.save('images/final/' + respName + '-hrtc.jpg')
        shirt_03.save('images/final/' + respName + '-rcl.jpg')

    path = "images/final/"
    path = os.path.realpath(path)
    os.startfile(path)


def bulk_upload_img():
    print("Webstore?")
    srchstr = input()
    srchstr.lower()
    wbstrAbr = wbAbr[srchstr]

    wbName = wbstrAbr
    wbPthName = fullName[wbName]

    prtOpt = wbPthName.lower()
    prtStrLoc = strLoc[prtOpt]

    print("what item ID?")
    srchitm = input()
    print("Color abriv?")
    srchclr = input()
    print("logo?")
    srchlgo = input()

    srch = wbstrAbr + srchitm + " " + srchclr + " " + srchlgo

    pthfldr = "C:\\Users\\victor.moreno\\Desktop\\PROPARGO WEBSTORES\\" + wbPthName + "\\Product Assets"

    print("PRESS ANY KEY TO CONTINUE")
    cont = input()
    # click PART menu element
    pyautogui.moveTo(1000, 125)
    prtPg = pyautogui.moveTo(1000, 160)
    pyautogui.click(prtPg)

    time.sleep(8)

    pyautogui.click(300, 225)
    pyautogui.write(srch)
    pyautogui.press('enter')

    time.sleep(12)
    # bulk edit - upload
    print("OPENING FILE PATH TO UPLOAD PICTURE ITEM: " + wbstrAbr + srchitm)
    pyautogui.click(60, 470)
    pyautogui.click(230, 400)
    pyautogui.click(750, 200, duration=1)
    pyautogui.click(515, 850)
    pyautogui.click(700, 850)
    pyautogui.click(900, 580)
    pyautogui.click()

    pyautogui.moveTo(500, 50)

    pyautogui.write(pthfldr + "\\" + srchitm + "\\final")
    pyautogui.press('enter')

    # USER PICKS PICTURE - WILL AUTOMATE LATER

    print("PRESS ANY KEY TO CONTINUE")
    cont = input()

    time.sleep(3)

    pyautogui.click(840, 860)
    time.sleep(3)
    # DOUBLE SAVE SEQUENCE
    pyautogui.click(1020, 1060)
    pyautogui.press('enter')
    time.sleep(4)
    pyautogui.click(1020, 1060)
    pyautogui.press('enter')
    time.sleep(4)

    # part tab
    pyautogui.moveTo(1010, 120)
    pyautogui.click(1010, 160)

    time.sleep(5)
    # clear serch
    pyautogui.click(90, 260)


def mstr_imupload():
    print("Webstore?")
    srchstr = input()
    srchstr.lower()
    wbstrAbr = wbAbr[srchstr]

    wbName = wbstrAbr
    wbPthName = fullName[wbName]

    prtOpt = wbPthName.lower()
    prtStrLoc = strLoc[prtOpt]

    print("what item ID?")
    srchitm = input()
    print("Color abriv?")
    srchclr = input()
    print("logo?")
    srchlgo = input()

    srch = wbstrAbr + srchitm + "mstr"

    pthfldr = "C:\\Users\\victor.moreno\\Desktop\\PROPARGO WEBSTORES\\" + wbPthName + "\\Product Assets"

    print("PRESS ANY KEY TO CONTINUE")
    cont = input()

    time.sleep(4)

    pyautogui.click(300, 225)
    pyautogui.write(srch)
    pyautogui.press('enter')

    time.sleep(12)
    # bulk edit - upload
    print("OPENING FILE PATH TO UPLOAD PICTURE ITEM: " + wbstrAbr + srchitm)
    pyautogui.click(120, 515)
    time.sleep(8)
    pyautogui.click(1200, 300)

    pyautogui.moveTo(500, 50)

    pyautogui.write(pthfldr + "\\" + srchitm + "\\final")
    pyautogui.press('enter')

    pyautogui.doubleClick(500, 120)
    pyautogui.click(1200, 675, duration=1)
    # repeat starts
    pyautogui.click(1200, 300)

    pyautogui.moveTo(500, 50)

    pyautogui.write(pthfldr + "\\" + srchitm + "\\final")
    pyautogui.press('enter')
    pyautogui.doubleClick(500, 120)
    # indexing part
    pyautogui.click(1420, 225)


terminal_menu()
