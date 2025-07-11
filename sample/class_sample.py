class PersonalDetails:
    year = 2020

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def add_age(self):
        self.age = self.age + 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Year: " + str(PersonalDetails.year))
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        print("Place: " + self.place)

    @classmethod
    def add_year(cls):
        cls.year = cls.year + 1

    @staticmethod
    def display_welcome():
        print("welcome")


PersonalDetails.display_welcome()
x = PersonalDetails("febs", 3, "kott")
y = PersonalDetails("name", 4, "er")

x.display()
y.display()

print("--------------------------------------------")
PersonalDetails.year = PersonalDetails.year + 1

x.add_age()
y.add_age()

x.display()
y.display()

print("--------------------------------------------")
PersonalDetails.add_year()

x.add_age()
y.add_age()

x.relocate("Th")
y.relocate("Del")

x.display()
y.display()
