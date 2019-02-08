n = int(input()) #number of students
t = int(input()) #time passed
s = input() #string representing boys and girls in the queue

index_list = [] 
for i in range(1, n):
	if s[i-1] == 'B' and s[i] == 'G':
		index_list.append(i)

for elem in index_list:
	s = s[elem] + s[elem-1] + s[elem+1::] 
