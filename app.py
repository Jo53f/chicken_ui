from chicken import Chicken
from chickens import Chickens
from flask import Flask, render_template, request, redirect
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
    return render_template("secondPage.html", chickens=enumerate(chickens.return_chickens()))

@app.post("/add")
def addChicken():
    name = request.form["chicken-name"].strip()
    if name:
        chickens.add_chicken(Chicken(name))
    return redirect("/records")

@app.post("/delete")
def deleteChicken():
    chicken_id = request.form["chicken_id"].strip()
    chicken_id = int(chicken_id)
    chickens.remove_chicken(chicken_id)
    return redirect("/records")

@app.post("/update")
def updateChicken():
    chicken_id = request.form["chicken_id"].strip()
    chicken_id = int(chicken_id)
    new_name = request.form["new_name"].strip()

    if new_name:
        chickens.change_name(chicken_id, new_name)

    return redirect("/records")