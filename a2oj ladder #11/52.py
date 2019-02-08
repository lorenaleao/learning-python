s = input()

substring0 = "0000000"
substring1 = "1111111"

ans0 = s.find(substring0)
ans1 = s.find(substring1)

if ans0 != -1 or ans1 != -1:
	print("YES")
else:
	print("NO")
"""
zeros = 0
ones = 0
dangerous = False

for elem in s:
	if elem == "0":
		ones = 0
		zeros += 1
		if zeros >= 7:
			dangerous = True
			break
	else:
		zeros = 0
		ones += 1
		if ones >= 7:
			dangerous = True
			break

if dangerous:
	print("YES")
else:
	print("NO")
"""