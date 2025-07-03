print("welcome to the student data organizer!")
my_std_list = []
while True:
    print("select an option:")
    print("1.add student")
    print("2.display all student")
    print("3.update student information")
    print("4.delete student")
    print("5.display subjects offered")
    print("6.exit")
    choice = int(input("enter your choice:"))

    if(choice == 1):
          print("Enter Student Details:")
          sid = input("student id:"),
          sname = input("name:"),
          sage = int(input("age:")),
          '''
          sGrade = input("grade:"),
          sDOB = input("date of birth:"),
          sSub = input("subjects(comma-separated):")
          '''
          a={
              "id": sid,
              "name": sname, 
              "age": sage,
              
            }
          my_std_list.append(a)
          print()
          print("student added successfully!")
          print()

    elif(choice == 2):
        print("---display all students:")
        for i in my_std_list:
            print(f"Name: {i["name"]}| Age: {i["age"]}")

    if(choice == 3):
        id = int(input("Enter Update Id: "))
        '''
        a={input("name:"),
           input("student Id:"),
           c=input("age:"),
           input("grade:"),
           input("date of birth:"),
           input("subjects(comma-separated):")
          }

        print(a.update(c))

              "Grade": sGrade,
              "DOB": sDOB,
              "Subjects": sSub,
        '''

        
                       

        


            
