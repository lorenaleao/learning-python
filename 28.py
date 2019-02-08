n = int(input())

count = 0

for i in range(n):
	p = input()
	s = p.split()
	suM = 0
	for elem in s:
		if elem == '1':
			suM += 1
	if suM > 1:
		count += 1

print(count)
