a=int(input("Enter time in seconds: "))
z=(a//(3600))
print("hours: ",z)
x=(a%(3600))//60
print("minutes: ",x)
y=(a%(3600)%60)
print("seconds: ",y)

