rno = int(input("Enter Roll Number : "))
Name = input("Enter Name : ")
Sci = int(input("Enter Marks of Science : "))
Maths = int(input("Enter Marks Of Maths : "))
Eng = int(input("Enter Marks Of English : "))

Tot = Sci+Maths+Eng
Avg = Tot/3

print("\nRoll_No.  Name \tTotal \tAvarage")
print("\n",rno,"\t",Name,"\t",Tot,"\t",Avg)

if(Sci>=40 and Maths>=40 and Eng>=40):
    if(Avg > 80):
        print("Grade - A")
    if(Avg > 60):
        print("Grade - B")
    if(Avg > 40):
        print("Grade - c")
else:
    print("Fail...")