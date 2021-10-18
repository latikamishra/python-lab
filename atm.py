p="1234"
n=int(input("enter your atm password:"))
if n==p:
	print("login successful")
	break
elif n!=p:
	print("wrong password try again!")
	if n==p:
		print("login successful")
		break
	else:
		print("wrong password try again!")
else:
	print("RUN TO BANK")
