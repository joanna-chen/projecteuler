def square(num):
	return num**2
	
sum1 = 0
sum2 = 0
	
for i in range(1,101):
	sum1 = sum1 + square(i)
	sum2 = sum2 + i
	
difference = 0
difference = square(sum2) - sum1
print(difference)