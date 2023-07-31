class Person:
    def __init__(self, id, name, age, gender, phoneNo, email, address):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.phoneNo = phoneNo
        self.email = email
        self.address = address

    def print_person_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone No: {self.phoneNo}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print("---------------------------")

person1 = Person(1, "John", 30, "male","123-456-7890", "john@example.com", "123 Main Street")
person2 = Person(2, "Jane", 25, "female","987-654-3210", "jane@example.com", "456 Elm Avenue")

persons = [person1, person2]

for person in persons:
    person.print_person_details()
        

