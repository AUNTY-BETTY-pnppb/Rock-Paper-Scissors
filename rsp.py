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
link = """Wanna play another one? <a href ="rsp.html">Then let's go!</a>"""
try:
    pick = (int(pick))
    rand_pick = random.randint(0, 2)
    rsp_dict = {0: "rock",
                1: "scissors",
                2: "paper"}

    comp_pick = rsp_dict[rand_pick]
    user_pick = rsp_dict[pick]

    if pick == rand_pick:
        outcome = "Computer's " + comp_pick + " ties with User's " + user_pick

    elif ((pick-rand_pick) % 3) == 1:
        outcome = "Computer's " + comp_pick + " beats User's " + user_pick

    elif ((pick - rand_pick) % 3) == 2:
        outcome = "User's " + user_pick + " beats Computer's " + comp_pick
    else:
        raise ValueError
except ValueError:
    outcome = """ERROR - I don't think that was one of the choices..."""
    link = """<a href="rsp.html">Go back nerd.</a>"""
except KeyError:
    outcome = """ERROR - I know what you were doing ;)"""
    link = """<a href="rsp.html">Go back nerd.</a>"""

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
                <p>%s</p>
            </body>
        </html>""" % (outcome, link))