a = input()
a = [int(i) for i in a.split()]

b = input()
b = [int(i) for i in b.split()]

b.sort()

if a[0] == a[1]:
	min_dif = b[-1] - b[0]

elif a[0] == 2:
	equal = False
	for i in range(len(b)-1):
		if b[i] == b[i+1]:
			equal = True
			break
	if equal:
		min_dif = 0
	else:
		min_dif = b[a[0]-1] - b[0]

else:
	min_dif = 1000
	for i in range(a[1]-(a[0]-1)):
		dif = b[i+a[0]-1]-b[i]
		if dif < min_dif:
			min_dif = dif

print(min_dif)