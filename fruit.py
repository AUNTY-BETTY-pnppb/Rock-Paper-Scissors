#!/usr/local/bin/python3

from cgitb import enable

enable()


from cgi import FieldStorage

print("Content-Type: text/html")
print()

form_data = FieldStorage()
buy = form_data.getlist("buy")

try:
    food = {"apples", "bananas", "jujubes", "rambutans"}
    buy = set(buy)

    if not buy <= food:
        outcome = """ERROR - <a href="fruit.html">Go back nerd</a>."""

    market_dict = {"apples": 1.59, "bananas": 1.25, "jujubes": 27.81, "rambutans": 20.84}

    food_list = []
    for i in buy:
        food_list.append(market_dict[i])

    price = sum(food_list)

    outcome = "The price is %.2f" % price

except:
    outcome = """ERROR - <a href="fruit.html">Go back nerd</a>."""

print("""
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="utf-8"/>
                <title>Fruit Stall</title>
            </head>
            <body>
                <p>%s</p>
            </body>
        </html>""" % outcome)