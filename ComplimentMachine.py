""" This is a Compliment Machine """
import random
import time
# Check if you enter a interger and a number smaller the 60
while True:
    time_between = input("How many compliments per minute do you want?\n")

    if not time_between.isdigit():
        print("Please enter a whole number")
        continue

    time_between = int(time_between)

    if time_between > 60:
        print("Please enter a smaller number")
        continue

    break

time_between = time_between / 60
# The list of Compliments
list_of_compliments = ["You have a very thoughtful way of looking at things.",
        "Your ideas are always interesting and insightful.",
        "You explain complex things clearly and effectively.",
        "You have a great sense of curiosity and willingness to learn.",
        "Your work shows real dedication and effort."    ]


# The machine
while True:
        new_list = list_of_compliments.copy()
        print("")
        while len(new_list) >= 1:
                i = random.randint(0, (len(new_list)-1))
                print(new_list[i])
                del new_list[i]
                time.sleep(time_between)
