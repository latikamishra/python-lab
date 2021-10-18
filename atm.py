p="1234"
n=3
while n>=0:
	x=input("enter password: ")
	if x==p:
		print("login successful")
		break
	else:
		n-=1
		print("wrong password")
		print(f"{n} attempts left")
