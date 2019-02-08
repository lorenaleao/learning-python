import math as m
n = int(input())

spaces = n
numbers = 1
rhombus = []

for row in range(n+1):
	rhombus.append([])
	for i in range(spaces):
		rhombus[row].append(" ")
	spaces -= 1

	first_half_size = m.ceil(numbers/2)
	for i in range(first_half_size):
		rhombus[row].append(str(i))
	
	for i in range(first_half_size-2, -1, -1):
		rhombus[row].append(str(i))
	
	numbers += 2

spaces = 1
numbers -= 4

for row in range(n+1, n+n+1):
	rhombus.append([])
	for i in range(spaces):
		rhombus[row].append(" ")
	spaces += 1

	first_half_size = m.ceil(numbers/2)
	for i in range(first_half_size):
		rhombus[row].append(str(i))
	
	for i in range(first_half_size-2, -1, -1):
		rhombus[row].append(str(i))
	
	numbers -= 2

for row in range(len(rhombus)):
	rhombus[row] = ' '.join(rhombus[row])
	print(rhombus[row])