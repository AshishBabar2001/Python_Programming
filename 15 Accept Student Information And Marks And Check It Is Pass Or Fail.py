Roll_No = int(input("Enter Roll Number : "))
Name  = input("Enter Name Of Student : ")
Sci = int(input("Enter Marks Of Science Subject : "))
Maths = int(input("Enter Marks Of Maths : "))
Eng = int(input("Enter Marks Of English : "))

Tot = Sci+Maths+Eng
Avg = Tot/3

print("Total is : ",Tot)
print("Avg is :",Avg)

if(Avg > 40):
    print("You Are Pass")
else:
    print("You Are Fail")