p = input()

HQ9mais = ['H', 'Q', '9']

count = 0
for elem in p:
	if elem in HQ9mais:
		count += 1

if count > 0:
	print("YES")
else:
	print("NO")
