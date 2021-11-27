Name = input("Enter Name Of Student : ")
Rno = int(input("Enter Roll Number : "))
Sci = int(input("Enter Marks Of Science : "))
Maths = int(input("Enter Marks Of Maths : "))
Eng = int(input("Enter Marks Of English : "))

Tot = Sci+Maths+Eng
Avg = Tot/3

print("Roll Number Of Student is : ",Rno)
print("Name Of Student Is :",Name)
print("Total Marks Of Student : ",Tot)
print("Avarage Of Student : ",Avg)
