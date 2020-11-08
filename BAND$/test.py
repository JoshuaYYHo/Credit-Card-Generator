from random import randint
import datetime

credit_card_number_text = ""

#the credit card number
for i in range(0, 4):
    credit_card_number = str(randint(1000, 9999))
    credit_card_number_text += credit_card_number
    credit_card_number_text += " "

#security code
security_code = str(randint(100, 999))


print(credit_card_number_text)
print(security_code)

'''
rand_color = ["crimson", "dodgerblue", "gold", "palegreen"]
for i in range(0, len(rand_color)):
    rand_num = randint(0, len(rand_color))
    print(rand_color[rand_num])
'''

#use date time for expiration date
date_now = datetime.datetime.now()
date_now_month = int(date_now.strftime("%m"))
date_now_year = int(date_now.strftime("%y")) + 3


print(type(date_now_month))

#list of names


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

print(first + " " + last)