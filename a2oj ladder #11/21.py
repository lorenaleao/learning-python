s = input()

l = s.split()

l.sort()

unique_colors = []

for elem in l:
	if elem not in unique_colors:
		unique_colors.append(elem)

print(4-len(unique_colors))