n = int(input())

increment = 0
decrement = 0
for i in range(n):
	statement = input()
	if statement[0] == '+' or statement[-1] == '+':
		increment += 1
	else:
		decrement += 1

x = increment - decrement;

print(x)