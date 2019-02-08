a = input()
a = [int(i) for i in a.split()]
num_passengers = a[0]
num_planes = a[1]

planes = input()
planes = [int(i) for i in planes.split()]

planes.sort()

remaining = num_passengers
max_cost = min_cost = 0 
planes_copy = planes.copy()

while remaining > 0:
	for i in range(num_planes-1, -1, -1): 
		if remaining < 1:
			break 
		if planes_copy[i] != planes_copy[i-1]:
			max_cost += planes_copy[i]
			planes_copy[i] -= 1
			remaining -= 1
			break
		else:
			max_cost += planes_copy[i]
			planes_copy[i] -= 1
			remaining -= 1

remaining = num_passengers
planes_copy = planes.copy()

for i in range(num_planes):
	for j in range(planes[i]): 
		if remaining < 1:
			break 
		min_cost += planes_copy[i]
		planes_copy[i] -= 1
		remaining -= 1
			
print(max_cost, min_cost)