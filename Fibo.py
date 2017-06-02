def fibo(number):
	count = 2
	num1 = 0
	num2 = 1
	s = [num1, num2]
	while(count < number):
		add = num1 + num2
		num1 = num2
		num2 += 1
		count += 1
		s.append(add)
	return (s) 
	
print(fibo(10))
