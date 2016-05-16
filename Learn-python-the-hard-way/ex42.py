# ex 42: Gothons Are Getting Classy

from sys import exit
from random import randint


class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Nice job, you died ... jackass.",
            "Such a luser.",
            "I have a small puppy that's better at this."]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n-----------------------"
            room = getattr(self, next)
            next = room()

    def death(self):
        print self.quips[randint(0, len(self.quips) - 1)]
        exit(1)
