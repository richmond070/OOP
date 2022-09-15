class Cars:
    def __init__(self, name, year, model):
        self.name = name
        self. year = year
        self.model = model

    def display(self):
        print(self.name)
        print(self.year)
        print(self.model)


toyota = Cars('camry', '2020', '50')
toyota.display()


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def set_name(self):
        print (f'my name is {self.name}')

    def get_grade(self):
        print (f'i am in grade {self.grade}')


s1 = Student("Jude", 12, 3)
s1.set_name()
s1.get_grade()


