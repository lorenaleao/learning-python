n_m = input()
n_m = [int(i) for i in n_m.split()]

if n_m[0] < n_m[1]:
	min_num = n_m[0]
else:
	min_num = n_m[1]

count = 0
for a in range(min_num+1):
	for b in range(min_num+1):
		exp1 = a**2 + b
		exp2 = a + b**2
		if exp1 == n_m[0] and exp2 == n_m[1]:
			count += 1

print(count)
