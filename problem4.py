product = 0
palindrome = 0
n = 99
m = 99

while n < 1000:
	while m < 1000:
		product = n * m
		string = str(product)

		#checks whether it is the same from both sides
		if string[:len(string)] == string[len(string)-1::-1]:
			# checks whether the new value is higher than the previous highest
			if product > palindrome:
				palindrome = product
		m += 1
	m = 99
	n += 1
print(palindrome)
