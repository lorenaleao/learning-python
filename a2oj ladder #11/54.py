def swap(a, b):
	temp = a
	a = b
	b = temp
	return a, b

def main():
	n = int(input())

	if n == 1:
		print(n)
	else:
		sequence = [str(x) for x in range(1, n+1)]

		i = n-1 
		while i > 0:
			sequence[i], sequence[i-1] = swap(sequence[i], sequence[i-1])
			i -= 1

		sequence = ' '.join(sequence)
		print(sequence)


if __name__ == "__main__":
	main()
"""
n = int(input())

sequence = [str(n)]
for i in range(1, n):
	sequence.append(str(i))

sequence = ' '.join(sequence)
print(sequence)
"""