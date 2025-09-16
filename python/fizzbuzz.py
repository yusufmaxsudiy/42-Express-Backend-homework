n = int(input("n sonini kiriting:"))

for son in range(1, n + 1):
	if son%3==0 and son%5==0:
		print("fizbuz")
	elif son%3==0:
		print("fiz")
	elif son%5==0:
        	print("buz")
	else:
        	print(son)
