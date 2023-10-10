class StoryBooks : 

    discount = 0.5

    def __init__ (self, name, writer, age, price) :
        self.name = name
        self.writer = writer
        self.age = age
        self.price = price

    def print_info(self) :
        print(f'name : {self.name}, writer : {self.writer}, age : {self.age}, price : {self.price}')
    
    def get_discount_by_instance_var_method(self) :
        self.price = self.price * self.discount

    def get_discount_by_class_var_method(self) :
       self.price = self.price * StoryBooks.discount

person_1 = StoryBooks('hamlak', 'shakespare', 90, 500)
person_2 = StoryBooks('kamla','spare', 70, 400)

# call by instance variable, so if I make changes it wont effect on the result
person_1.get_discount_by_instance_var_method()
print(f'price is {person_1.price}')
discount = 0.3 
print(f'price is {person_1.price}')

# call by class variable, so if I make changes it(discount = 0.3) will effect on the result
person_1.get_discount_by_class_var_method()
print(f'price is {person_1.price}')
