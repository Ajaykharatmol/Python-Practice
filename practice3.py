class Employee:
    def AcceptDetails(self):
        self.id = int(input("Enter ID : "))
        self.Name = input("Enter Name : ")
        self.Salary = int(input("Enter Salary : "))
    def ShowDeatails(self):
        print("Employee Details : ")
        print("ID : ",self.id)
        print("Name : ", self.Name)
        print("Salary : ", self.Salary)

#e = Employee()
#e.AcceptDetails()
#e.ShowDeatails()

class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.Name = name
        self.Salary = salary
    def ShowDeatails(self):
        print("Employee Details : ")
        print("ID is : ",self.id)
        print("Name is : ", self.Name)
        print("Salary is : ", self.Salary)

class Adress(Employee):
    def __init__(self,id,name,salary,city,state,country):
        Employee.__init__(self,id,name,salary)
        self.city = city
        self.state = state
        self.country = country
    def showadress(self):
        Employee.ShowDeatails(self)
        print("Employee Details : ")
        print("City : ", self.city)
        print("State : ", self.state)
        print("Country : ", self.country)

e1 = Adress(100,"Ajay",20000,"Panvel","Maharashtra","India")
e1.showadress()


class Family:
    def __init__(self, father, mother):
        self.father = father
        self.mother = mother
    def show(self):
        print(self.father)
        print(self.mother)

class MyFamily(Family):
    def __init__(self,father,mother,wife, son):
        Family.__init__(self, father, mother)
        self.wife = wife
        self.son = son
    def showfamily(self):
        Family.show(self)
        print(self.wife)
        print(self.son)

f = MyFamily("Ankush","Ganga","Poonam","Reyaansh")
f.showfamily()

