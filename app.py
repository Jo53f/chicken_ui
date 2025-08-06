from chicken import Chicken
from chickens import Chickens
from flask import Flask, render_template
app = Flask(__name__)

menu_options = ["Create New Record", "Update Existing Record", "Delete Record"]

# A function to add placeholder chickens to the chickens list
def add_placeholder_chickens(chickens):
    chicken_names = ["Peter", "Romly", "Tommy", "Jonathan"]

    for name in chicken_names:
        chickens.add_chicken(Chicken(name))


chickens = Chickens()
add_placeholder_chickens(chickens)

@app.route("/")
def main_menu():
    return render_template("index.html", menu_options=menu_options)

@app.route("/records")
def records():
    return render_template("secondPage.html", chickens=chickens.return_chickens())