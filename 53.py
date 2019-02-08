s = input()

s = s.lower()
consonant = "aeyiou"
l = []

for char in s:
	if char not in consonant:
		l.append('.' + char)

l = ''.join(l)
print(l)