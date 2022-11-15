class Form:

    def __init__ (self, name,lastname,address,telephone,birthday,marital_status,weight):
        self.name = name
        self.lastname = lastname 
        self.address = address 
        self.telephone = telephone
        self.Age = Age
        self.marital_status = marital_status
        self.observation = observation
        self.weight = weight
        self.problem_affection = problem_affection

##metodos ##
    def getName(self): ##get para encapsular##
        return self.name 
    def getLastname(self):
        return self.lastname
    def getAddress(self):
        return self.address
    def getTelephone(self):
        return self.telephone
    def getAge(self):
        return self.Age
    def getMarital_status(self):
        return self.marital_status
    def getobservation(self):
        return self.observation
    def getweight(self):
        return self.weight
    def getproblem_affection(self):
        return self.problem_affection



    def showed(self):
        print("Name:\n")
        print("Lastname:\n", self.name) 
        print("Address:\n", self.lastname)
        print("Telephone:\n", self.address)
        print("Age:\n", self.telephone)
        print("Marital Status:\n", self.Age)
        print("Observation:\n", self.marital_status)
        print("problem/affection:\n",self.observation)
        print("weight:\n",self.weight)
        print("weight:\n",self.problem_affection)

##imprimir#
title = input("Pacient Form:\n")
name = input("Name:\n")
lastname = input("Lastname:\n") 
address = input("Address:\n")
telephone= input("Telephone:\n")
Age = input("Age:\n")
marital_status = input("Marital Status:\n")
observation = input("Observation:\n")
problem_affection = input("problem/affection:\n")
weight = input("weight:\n")

##mostrar##
e = Form(name,lastname,address,telephone,Age,marital_status,observation,problem_affection,weight,title)
e.showedPatient_form()