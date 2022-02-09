Emp = {"Ename":"Amit","Eage":23,"Esalary":32000,"Ecompany":"Tcs"}

print("Original Data Of Dictionary...")

print(Emp)

Emp["Ename"] = input("Enter Name Of Employee : ")
Emp["Eage"] = int(input("Enter Age Of Employee : "))
Emp["Esalary"] = int(input("Enter Salary Of Employee : "))
Emp["Ecompany"] = input("Enter Company Name : ")

print("Updated Dictionary....")

print(Emp)