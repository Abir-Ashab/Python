class StoryBooks : 

    def __init__ (self, name, writer, age, price) :
        self.name = name
        self.writer = writer
        self.age = age
        self.price = price

    def sort_priority(self) :
        return self.price


def print_info(person) :
    for obj in person :
        print(f'name : {obj.name}, writer : {obj.writer}, age : {obj.age}, price : {obj.price}')
    

person_1 = StoryBooks('hamlak', 'shakespare', 90, 500)
person_2 = StoryBooks('kamla','spare', 70, 670)
person_3 = StoryBooks('Ruoa','humu', 65, 250)

person = [person_1, person_2, person_3]

# using sorted function which mainly return person type thing
store = sorted(person, key=StoryBooks.sort_priority)
print_info(store)
print('\n')

# using sort function
person.sort(key = StoryBooks.sort_priority)
print_info(person)
print('\n')

# using lambda function
writers = [person_1, person_2, person_3]
writers.sort(key=lambda x : x.price)
print_info(writers)