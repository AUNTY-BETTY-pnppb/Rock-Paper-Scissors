#!/usr/local/bin/python3

from cgitb import enable

enable()

from cgi import FieldStorage
from html import escape

print("Content-Type: text/html")
print()

form_data = FieldStorage()
length = escape(form_data.getfirst("length", "").strip())
units = escape(form_data.getfirst("units", "").strip())

outcome = ''

try:
    if units == "inches":
        inches = float(length)
        feet = inches / 12
        yards = inches / 36

    elif units == "feet":
        feet = float(length)
        inches = feet * 12
        yards = feet / 3

    elif units == "yards":
        yards = float(length)
        feet = yards * 3
        inches = yards * 36

    outcome = """<table>
                        <caption>Measurements</caption>
                        <tr>
                            <th scope="col">Inches</th>
                            <td>%.2f</td>
                        </tr>
                        <tr>
                            <th scope="col">Feet</th>
                            <td>%.2f</td>
                        </tr>
                        <tr>
                            <th scope="col">Yard</th>
                            <td>%.2f</td>
                        </tr>
                    </table>""" % (inches, feet, yards)

except:
    outcome = """<p>ERROR - <a href="lengths.html">Go back nerd</a>.</p>"""


print("""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <title>Lengths</title>
                <link rel="stylesheet" href="lengths.css" />
            </head>
            <body>
                %s
            </body>
        </html>""" % outcome)




