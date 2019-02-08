n = int(input())

left = []
right = []
l_zeros = 0
l_ones = 0
r_zeros = 0
r_ones = 0

for i in range(n):
    entry = input()
    left.append(entry[0])
    right.append(entry[2])

for elem in left:
    if elem == '0':
        l_zeros += 1
    else:
        l_ones += 1

for elem in right:
    if elem == '0':
        r_zeros += 1
    else:
        r_ones += 1
        
seconds = 0
if l_zeros != n or l_ones != n:
    if l_zeros < l_ones:
        	seconds += l_zeros
    else:
        	seconds += l_ones

if r_zeros != n or r_ones != n:
    if r_zeros < r_ones:
        	seconds += r_zeros
    else:
        	seconds += r_ones

print(seconds) 
