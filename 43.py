s = input()
t = input()
"""
s_size = len(s)
t_size = len(t)

if s_size == t_size:
	count = 0
	for i in range(s_size):
		if s[i] == t[s_size-i-1]:
			count += 1
		else:
			break

	if count == s_size:
		print("YES")
	else: 
		print("NO")
else:
	print("NO")
"""
s_size = len(s)
t_size = len(t)

if s_size == t_size:
	reverse_string = s[::-1]
	if reverse_string == t:
		print("YES")
	else:
		print("NO")
else:
	print("NO")