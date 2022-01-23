Nos = (12,23,4,45,67,78)

print(Nos)

n = int(input("Enter NO to Search Element : "))

if n in Nos:
    print(n,"Number Is Present In Tuple")
else:
    print(n,"Number Is Not Present In Tuple")