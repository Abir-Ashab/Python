class StoryBooks : 
    # here __init__  is a default constructor in python, and self is similar as this
    def __init__ (self, name, writer, age) :
        self.name = name
        self.writer = writer
        self.age = age

person_1 = StoryBooks('hamlak', 'shakespare', 90)
person_2 = StoryBooks('kamla','spare', 70 )

# changes er feature o add korse python
person_1.name = 'sufia'

print(person_1.name)
print(person_2.name)