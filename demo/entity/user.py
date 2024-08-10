class User:
    def __init__(self, uid, name, age, gender, location) -> None:
        self.uid = uid
        self.name = name
        self.age = age
        self.gender =gender
        self.location = location

    def setName(self, new_name):
        self.name = new_name

    def setGender(self, new_gender):
        self.gender = new_gender
    
    def setAge(self, new_age):
        self.age = new_age
        

    def setLocation(self, new_location):
        self.location = new_location
        
