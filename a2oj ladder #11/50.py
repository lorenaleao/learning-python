k = int(input())

s = input()

letters = {} 

for char in s:
	if char not in letters:
		letters[char] = 1
	else: 
		letters[char] += 1

is_there_solution = True
for elem in letters:
	if letters[elem]%k != 0:
		is_there_solution = False

if not is_there_solution:
	print(-1)
else:
	ans = ""
	for elem in letters.keys():
		num = int(letters[elem]/k)
		ans += elem*num
	ans *= k
	print(ans)