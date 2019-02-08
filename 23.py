s = input()
unique_letters = []

for char in s:
	if char not in unique_letters:
		unique_letters.append(char)

if len(unique_letters) % 2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")