from flask import Flask, render_template
#from test import credit_card_number_text, security_code
from random import randint
import datetime
app = Flask(__name__)

#the credit card number
#want it to generate a new number
def generate_new_card():
    credit_card_number_text = ""
    for i in range(0, 4):
        credit_card_number = str(randint(1000, 9999))
        credit_card_number_text += credit_card_number
        credit_card_number_text += " "

    #security code
    security_code = str(randint(100, 999))
    return [credit_card_number_text, security_code]

rand_color_list = ["crimson", "dodgerblue", "gold", "palegreen"]
rand_num = randint(0, len(rand_color_list))

#for expiration date
date_now = datetime.datetime.now()
date_now_month = int(date_now.strftime("%m"))
date_now_year = int(date_now.strftime("%y")) + 3

#list of names
def name():
    first_names = []
    last_names = []

    for i in open("first_names.txt", "r"):
        bruh = i.capitalize()
        foo = bruh.replace("\n", "")
        first_names.append(foo)

    for i in open("last_names.txt", "r"):
        foo = i.replace("\n", "")
        last_names.append(foo)

    first = first_names[randint(0, len(first_names)-1)]
    last = last_names[randint(0, len(last_names)-1)]

    return first + " " + last

@app.route('/')
def home():
    skrt = generate_new_card()
    rand_color = rand_color_list[rand_num]
    return render_template('index.html', card_number = skrt[0], sec_code = skrt[1], rand_color = rand_color, dm = date_now_month, dy = date_now_year, n = name())

@app.route('/', methods = ["POST"])
def new_card():
    new_card = generate_new_card()
    rand_color_new = rand_color_list[rand_num]
    return render_template('newcard.html', card_number = new_card[0], sec_code = new_card[1], rand_color = rand_color_new, dm = date_now_month, dy = date_now_year, n = name())


if __name__ == "__main__":
    app.run(debug=True)