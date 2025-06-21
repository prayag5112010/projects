print("welcome to the interactive personal data collector")

name=str(input("please enter youe name:"))

age=int(input("please enter youe age:"))

hight=float(input("please enter youe hight:"))      

favourite_Number=int(input("please enter youe favourite number:"))
      
print("\n")      
      
print("Thank you! here is the information we collected:")

print("Name:",name,"(Type:",type(name),"Memory adderss:",id(name))

print("age:",age,"(Type:",type(age),"Memory adderss:",id(age))

print("hight:",hight,"(Type:",type(hight),"Memory adderss:",id(hight))

print("favourite_Numbe:",favourite_Number,"(Type:",type(favourite_Number),"Memory adderss:",id(favourite_Number))

current_year=2025
print("your birth is approximetely:",current_year-age)

print("thank you for using the personal data collector.goodbye")
