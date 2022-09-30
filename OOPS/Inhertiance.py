class Person:
    def __init__(self, fname, lname,age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    
    def printname(self):
        print(self.firstname, self.lastname)
    
    def printage(self):
  	    # print("{} is {} year old".format(self.firstname).format(self.age))
        print('{} is {} year old'.format(self.firstname , self.age))
#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe", '45')
x.printname()

# Creating Child class by the name of student and using features of parent class(Person)
class student(Person):
	pass
    
x = student('Sagar','Saini', '21')
x.printname()
x.printage()