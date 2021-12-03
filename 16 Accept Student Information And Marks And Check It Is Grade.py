Roll_No = int(input("Enter Roll Number : "))
Name = input("ENter Name : ")
Sci = int(input("Enter Sci Marks : "))
Maths = int(input("Enter Maths Marks : "))
Eng = int(input("Enter Eng Marks : "))

Tot = Sci + Maths + Eng
Avg = Tot/3

print("\n Roll No. \tName \tTot \tAvg")
print("\n",Roll_No,"\t      ",Name,"\t",Tot,"\t",Avg)

print("\n\nTotal Marks Are : ",Tot)
print("\nAvrage Is : ",Avg)

if(Avg>80):
    print("\nGrade - A")
elif(Avg>60):
    print("\nGrade - B")
elif(Avg>40):
    print("\nGrade - C")
else:
    print("\nFail")
