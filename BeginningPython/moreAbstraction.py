def length_message(x):

    return "The length of", repr(x), "is", len(x)

print(length_message("Marry"))
print(length_message([1, 2, 3, 4]))


__metaclass__ = type #Make sure we get new style classes


class Person:

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello,world! I'm %s." % self.name

foo = Person()
bar = Person()

foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')

foo.greet()
bar.greet()

print(foo.name)
foo.name = 'Yoda'
print(foo.name)
Person.greet(foo)



