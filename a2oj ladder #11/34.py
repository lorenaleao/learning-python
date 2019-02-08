n = int(input())

pages = input()

pages_week = pages.split()

sum1 = 0
for elem in pages_week:
	sum1 += int(elem)
	
weeks_number = n//sum1

to_be_read = n - weeks_number*sum1;

if(to_be_read == 0):
	to_be_read = sum1

sum2 = 0
day = 0

for elem in pages_week:
	if sum2 < to_be_read:
		sum2 += int(elem)
		day += 1 

print(day)
