s = input()

s = [int(i) for i in s.split()]

max_sequence = [x for x in range(s[2]+1)]
min_sequence = [x for x in range(s[0]-1, s[1]-1, -1)] 

len_min = len(min_sequence)
len_max = len(max_sequence)

if len_min < len_max:
	print(len_min)
else:
	print(len_max)
                                                                   