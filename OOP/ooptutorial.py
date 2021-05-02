class Person:
    def __init__(self,person_name,dob,ht):
        self.name = person_name
        self.dob = dob
        self.height = ht

    
    def get_name(self):
        return self.name

    def new_name(self,new_name):
        if self.__has_any_number(new_name):
            print("LOL")
            return "LOL"
        else:
            self.name = new_name

    def __has_any_number(self,string):
        return "0" in string

    def get_summary(self):
        return f"Name :{self.name}, DOB: {self.dob}, Height: {self.height}"

a_person = Person("Shojib Hasan","23",'5.6')


print(a_person.get_summary())

a_person.new_name("Mahfujul Hasan")
print(a_person.get_summary())
print(a_person.dob)
a_person.new_name("0Shojib")
print(a_person.name)