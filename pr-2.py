print("welcome to the pattern generator and number analyzer!")
print("")

while True:
    print("select an option:")
    print("1.Generate a pattern")
    print("2.Analyze a range of numbers")
    print("3.Exit")
    choice = int(input("enter your choice:"))

    if(choice == 1):
        n = int(input("enter the number of rows for the pattern: "))
        for i in range(0,n):
            for j in range(0,i):
                print("* ",end=" ")
            print("")
    elif (choice == 2):
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        sum = 0
        for i in range(start,end):
            if i%2==1:
                print(i, "is Odd")
            else:
                print(i,"is Even")
            sum += i
        print("sum of all num from 10 to 15 is:",sum)
    else:
        print("exiting the program. Goodbye!")
        break
   
'''
OutPut:
welcome to the pattern generator and number analyzer!

select an option:
1.Generate a pattern
2.Analyze a range of numbers
3.Exit
enter your choice:1
enter the number of rows for the pattern: 5

*  
*  *  
*  *  *  
*  *  *  *  
select an option:
1.Generate a pattern
2.Analyze a range of numbers
3.Exit
enter your choice:2
Enter the start of the range: 15
Enter the end of the range: 25
15 is Odd
16 is Even
17 is Odd
18 is Even
19 is Odd
20 is Even
21 is Odd
22 is Even
23 is Odd
24 is Even
sum of all num from 10 to 15 is: 195
select an option:
1.Generate a pattern
2.Analyze a range of numbers
3.Exit
enter your choice:3
exiting the program. Goodbye!



'''
