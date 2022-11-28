class Form:

    def __init__ (self, name,lastname,address,telephone,birthday,marital_status,weight,age):
        self.name = name
        self.lastname = lastname 
        self.address = address 
        self.telephone = telephone
        self.age = age
        self.marital_status = marital_status
        self.observation = observation
        self.weight = weight
        self.problem_affection = problem_affection
        self.birthday = birthday
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
        return self.age
    def getMarital_status(self):
        return self.marital_status
    def getobservation(self):
        return self.observation
    def getweight(self):
        return self.weight
    def getproblem_affection(self):
        return self.problem_affection
    def getbirthday(self):
        return self.birthday


    def __str__(self):
        print("Name:\n",self.name)
        print("Apellido:\n",self.lastname) 
        print("Direccion:\n", self.address)
        print("Telefono:\n", self.telephone)
        print("Edad:\n", self.age)
        print("Estado Marital:\n",self.marital_status)
        print("Observaciones:\n", self.observation)
        print("Problema/Afeccion:\n",self.problem_affection)
        print("Peso:\n",self.weight)
        print("Nacimiento:\n",self.birthday)

##imprimir#
title = input("Ficha del Paciente:\n")
name = input("Nombre:\n")
lastname = input("Apellido:\n") 
address = input("Dirrecion:\n")
telephone= input("Telefono:\n")
age = input("Edad:\n")
marital_status = input("Estado Marital:\n")
birthday = input("Nacimiento:\n")
observation = input("Observacion:\n")
problem_affection = input("Problema/Afeccion:\n")
weight = input("Peso:\n")

##mostrar##

e = print("Los Datos son: \n",title)
print("Nombre:\n",name)
print("Apellido:\n",lastname)
print("Direcion:\n",address)
print("Telefono:\n",telephone)
print("Edad:\n",age)
print("Estado Civil:\n",marital_status)
print("Observacion:\n",observation)
print("Problema/Afeccion: \n",problem_affection)
print("Nacimiento: \n",birthday)
print("Peso: \n",weight)

showed = print("")

result = str(Form)
print("Name:\n",name)
print("Apellido:\n",lastname) 
print("Direccion:\n",address)
print("Telefono:\n",telephone)
print("Edad:\n",age)
print("Estado Marital:\n",marital_status)
print("Observaciones:\n",observation)
print("Problema/Afeccion:\n",problem_affection)
print("Peso:\n",weight)
print("Nacimiento:\n",birthday)