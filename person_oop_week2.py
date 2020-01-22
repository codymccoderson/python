class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
    def greet(self, other_person):
        return("Hello {}, I am {}!".format(other_person.name,
        self.name))
    
    def contact_info(self):
        return("Email: {} and Phone: {} ".format(self.email, 
        self.phone))

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

print(sonny.greet(jordan))
print(jordan.greet(sonny))
print(sonny.contact_info())
print(jordan.contact_info())