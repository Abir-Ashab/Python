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

    # type-1
    # it changes class variables for the whole program
    @classmethod
    def set_discount(cls, new_discount) :
        cls.discount = new_discount


    # type-2
    @classmethod
    def split_string(cls, data) :
        name, writer, age, price = data.split(',')
        return cls(name, writer, age, price)

person_1 = StoryBooks('hamlak', 'shakespare', 90, 500)
person_2 = StoryBooks('kamla','spare', 70, 400)

StoryBooks.set_discount(0.6)
print(person_2.discount)

data = 'hamlak, shakespare, 90, 500'
store_data = StoryBooks.split_string(data)

print(store_data.name)