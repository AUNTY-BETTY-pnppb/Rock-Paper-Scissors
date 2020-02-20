#!/usr/local/bin/python3
from cgitb import enable

enable()

from html import escape

from cgi import FieldStorage
import random

print("Content-Type: text/html")
print()

form_data = FieldStorage()
pick = escape(form_data.getfirst("pick", "").strip())

outcome = ""
link = """Wanna play another one? <a href ="rsp15.html">Then let's go!</a>"""
image = """swell.jpg"""
try:
    rand_pick = random.randint(0, 14)
    rsp_dict = {0: "rock",
                1: "gun",
                2: "lightning",
                3: "devil",
                4: "dragon",
                5: "water",
                6: "air",
                7: "paper",
                8: "sponge",
                9: "wolf",
                10: "tree",
                11: "human",
                12: "snake",
                13: "scissors",
                14: "fire"}

    out_dict = {0: "rock POUNDS OUT",
                1: "gun SHOOTS",
                2: "lightning STRIKES",
                3: "devil DEFEATS",
                4: "dragon DEVASTATES",
                5: "water SPLASHES",
                6: "air BLOWS",
                7: "paper CUTS",
                8: "sponge BOB SQUAREPANTS",
                9: "wolf BITES",
                10: "tree TACKLES",
                11: "human PUNCHES",
                12: "snake SPITES",
                13: "scissors SLICES",
                14: "fire FRIES"}

    pick = int(pick)
    user_pick = rsp_dict[pick]
    comp_pick = rsp_dict[rand_pick]

    user_pick_win = out_dict[pick]
    comp_pick_win = out_dict[rand_pick]

    if pick == rand_pick:
        outcome = "Computer's " + comp_pick + " ties with User's " + user_pick

    elif ((pick - rand_pick) % 15) in range(8, 15):
        outcome = "Computer's " + comp_pick_win + " User's " + user_pick + ". It is very effective!"

    elif ((pick - rand_pick) % 15) in range(1, 8):
        outcome = "User's " + user_pick_win + " Computer's " + comp_pick + ". It is very effective!"
    else:
        raise KeyError
except ValueError:
    outcome = """ERROR - I don't think that was one of the choices..."""
    link = """<a href="rsp15.html">Go back nerd.</a>"""
    image = """tom.jpg"""

except KeyError:
    outcome = """ERROR - I know what you were doing ;)"""
    link = """<a href="rsp15.html">Go back nerd.</a>"""
    image = """tom.jpg"""

print("""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <title>Rock, Paper, Scissors</title>
                <link rel="stylesheet" href="rsp.css"/>
            </head>
            <body>
                <p>%s</p>
                <img src= %s />
                <p>%s</p>
            </body>
        </html>""" % (outcome, image, link))
