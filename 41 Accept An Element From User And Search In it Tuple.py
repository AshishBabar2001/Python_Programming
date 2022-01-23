Employee = ("Avinash","Shantanu","Mansi","Mayuri")

print(Employee)

ele = input("Enter Element To Search : ")

if ele in Employee :
    print(ele,"Is Present In Employee Tuple")
else:
    print(ele,"Is NOt Present In Employee Tuple")