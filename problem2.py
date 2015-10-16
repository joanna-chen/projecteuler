sum = 0
fib = [1, 2]
i = 2

while fib[i-1] + fib[i-2] < 4000000:
	fib.append( fib[i-1] + fib[i-2] )
	i += 1
		
for n in fib:
	if n % 2 == 0: 
		sum += n
		
print(sum)
		

	