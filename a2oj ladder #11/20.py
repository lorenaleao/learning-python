s = input()

s_list = list(s)

for i in range(len(s)//2):
	s_list.remove('+')

s_list.sort()

s = '+'.join(s_list)

print(s) 