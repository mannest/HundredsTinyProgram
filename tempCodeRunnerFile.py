""" This is a Compliment Machine """
import random
import time

list = ["You have a very thoughtful way of looking at things.",
        "Your ideas are always interesting and insightful.",
        "You explain complex things clearly and effectively.",
        "You have a great sense of curiosity and willingness to learn.",
        "Your work shows real dedication and effort."    ]

while True:
        new_list = list
        while len(new_list) >= 1:
                i = random.randint(0, (len(new_list)-1))
                print(new_list[i])
                del new_list[i]
                time.sleep(5)
