n = int(input())

goals = []
for i in range(n):
	 s = input()
	 goals.append(s)

team1 = goals[0]
team1_goals = 0
team2_goals = 0

for elem in goals:
	if elem == team1:
		team1_goals += 1
	else:
		team2_goals += 1
		team2 = elem

if team1_goals > team2_goals:
	print(team1)
else:
	print(team2)