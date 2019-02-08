k = int(input())
g = input()

g = [int(i) for i in g.split()]

g.sort(reverse = True)

total_growth = 0
count = 0
for elem in g:
	if total_growth < k:
		total_growth += elem
		count += 1
	else:
		break

if total_growth < k:
	print(-1)
else: 
	print(count)
