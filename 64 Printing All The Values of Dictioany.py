Emp = {"Name":"Vaishali","Age":25,"Company":"Accenture","Salary":40000}
Emp["Name"] = input("Enter Name  : ")
Emp["Age"] = int(input("ENter Age : "))
Emp["Company"] = input("Enter Company : ")
Emp["Salary"] = int(input("ENter Salary : "))
for x in Emp:
    print(Emp[x])