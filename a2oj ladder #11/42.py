n = input()

magic = True

if n[0] == '4':
	magic = False
else:
	for char in n:
		if char != '1' and char != '4':
			magic = False
			break
		else:
			if char == '4':
				fours += 1
			else:
				fours = 0
			if fours > 2:
				magic = False
				break

if magic:
	print("YES")
else:
	print("NO")