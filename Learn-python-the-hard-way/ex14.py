# Exercise 14: Prompting And Passing

from sys import argv

scripts, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s scripts." % (user_name, scripts)
print "I'd like to ask you a few questions."
print "Do you lile me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
