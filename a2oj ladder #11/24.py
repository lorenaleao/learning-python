guest = input()
host = input()
pile = input()

pile_list = list(pile)

for char in guest:
	if char in pile_list:
		pile_list.remove(char)
	else:
		break

for char in host:
	if char in pile_list:
		pile_list.remove(char)
	else:
		break

if len(pile_list) == 0 and len(pile) == len(guest)+len(host):
	print("YES")
else:
	print("NO")