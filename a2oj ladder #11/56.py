import collections as c
from collections import defaultdict
		
line0 = input()
line0 = [int(i) for i in line0.split()]

kirito_strength = line0[0]

dragons = defaultdict(list)

for i in range(line0[1]):
	line = input()
	line = [int(i) for i in line.split()]
	dragons[line[0]].append(line[1]) #line[0] -> dragon's strength
				 	 #line[1] -> the bonus for defeating it

dragons = c.OrderedDict(sorted(dragons.items()))
#for k, v in dragons.items(): print(k, v)

kirito_dies = False
for strength in dragons:
	for elem in dragons[strength]:
		if strength < kirito_strength:
			kirito_strength += elem
		else:
			kirito_dies = True 
			break

if kirito_dies:
	print("NO")
else:
	print("YES")
