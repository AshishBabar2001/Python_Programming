Data = ("Ashish",34,"Prakash",67,"Bhavesh",4)

print(Data)

Ans = input("\n Wheather To Search Number or String : ")

if(Ans == "Number"):
    n = int(input("Enter A No To Search : "))
else:
    n = int(input("Enter a String to Search : "))
if n in Data:
    print(n,"Present In Tuple")
else:
    print(n,"Not Present In Tuple")
