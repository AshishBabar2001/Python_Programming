def Cal(Ename,Sal,Bonus = 3000):
    TotalAmount = Sal + Bonus
    print(Ename," : ",TotalAmount)
Name = input("Enter Employee Name : ")
sal = int(input("Enter Salary : "))
Cal(Name, sal)

