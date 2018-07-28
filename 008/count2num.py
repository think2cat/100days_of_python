arr = (1,3,5,7,9,11,13,16,17,18,20,64,156)
total =  84

def countNum(nums, count):
	for i, num1 in enumerate(nums):
		for j, num2 in enumerate(nums):
			if i != j and (num1 + num2) == count :
				print(str(i) + ":" + str(j))
				return (i, j)
	print("no found")
	return
		
countNum(arr, total)