s = input()
s_len = len(s)

substring = "WUB"
start = 0
subs_ind = []

while start < s_len:
	index = s.find(substring, start)

	if index != -1:
		subs_ind.append(index)
		start = index+3
	else:
		break

if len(subs_ind) == 0:
	print(s)
else:
	song = []

	if subs_ind[0] > 0:
		for i in range(subs_ind[0]):
			song.append(s[i])
		song.append(" ")

	for i in range(len(subs_ind)-1):
		dif = subs_ind[i+1] - subs_ind[i] 
		if dif > 3:
			for j in range(subs_ind[i]+3, subs_ind[i+1]):
				song.append(s[j])
			song.append(" ")

	if subs_ind[-1] < s_len-3:
		for i in range(subs_ind[-1]+3, s_len):
			song.append(s[i])

	song = ''.join(song)
	print(song)



"""
song = []

i = 0
space = False
while i < len(s):
	if i == len(s)-1:
		if space:
			song.append(" ")
		song.append(s[i])
		i += 1
		space = False
	elif i == len(s)-2:
		if space:
			song.append(" ")
		song.append(s[i])
		i += 1
		if s[i:i+1] != "W":
			song.append(s[i])
			i += 1
		space = False
	elif s[i:i+3] != "WUB":
		if space:
			song.append(" ")
		song.append(s[i])
		i += 1
		if s[i:i+1] != "W":
			song.append(s[i])
			i += 1
		if s[i:i+1] != "W":
			song.append(s[i])
			i += 1
		
		space = False
		
	else:
		i += 3
		space = True 

if song[0] == " ":
	del song[0]
song = ''.join(song)
print(song)
"""
