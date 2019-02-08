s = input()
t = input()

s_lower = s.lower()
t_lower = t.lower()

if s_lower == t_lower:
	print("0")
elif s_lower < t_lower:
	print("-1")
else: 
	print("1")