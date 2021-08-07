class Address:
    def __init__(self,street,street2,city,state,zip,country):
        self.street = street
        self.street2 = street2
        self.city = city
        self.zip = zip
        self.country = country

    def get_address(self):
        return f"Street :{self.street}, Street 2: {self.street2}, City: {self.city}, ZIP: {self.zip}, Country: {self.country}"

class Information(Address):

    def __init__(self,phone,mobile,fax,email,language,website):
        self.phone = phone
        self.mobile = mobile
        self.fax = fax
        self.email = email
        self.language = language
        self.website = website
        

    def all_tags(self):
        tags = ["Company Contact", "Components Buyer", "Consultancy Service","Destributor","Employee","Manufacturer","Office Supplies"]
        return tags
    def __iter__(self):
        return iter(self.all_tags())


class Professions:
    def __init__(self):
        self.value1 = "Doctor"
        self.value2 = "Madam"
        self.value3 = "Miss"
        self.value4 = "Mister"
        self.value5 = "Professor"
    def get_professions(self):
        return [self.value1, self.value2,self.value3,self.value4,self.value5]

class Contacts(Professions):
    def __init__(self,name,position,email,phone,mobile,notes):
        self.name = name
        self.position = position
        self.email = email
        self.phone = phone
        self.mobile = mobile
        self.notes = notes
    
    def contacts(self):
        return self.get_professions(),self.name,self.position,self.email,self.phone,self.mobile,self.notes