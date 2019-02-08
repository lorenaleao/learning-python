tv_sets = input()
tv_sets = [int(i) for i in tv_sets.split()]

prices = input()
prices = [int(i) for i in prices.split()]

prices.sort()

money = 0
for i in range(tv_sets[1]):
	if prices[i] <= 0:
		money += prices[i]*(-1)
	else:
		break 

print(money)