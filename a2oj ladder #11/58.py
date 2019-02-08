s = input()

hello = 'hello'
unique_letters = ""

i = 0
for char in s:
	if i > 4:
		break
	elif char == hello[i]:
		unique_letters += char
		i += 1

if hello in unique_letters:
	print("YES")
else:
	print("NO")

