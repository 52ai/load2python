# ex 41:Gothons From Planet Percal

from sys import exit
from random import randint


def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ... jackass.",
             "Such a luser.",
             "I have a small puppy that's better at this."]
    print quips[randint(0, len(quips) - 1)]
    exit(1)


print death()