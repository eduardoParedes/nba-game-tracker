from nba_api.stats.static import teams

# Find teams by full name.
data = teams.get_teams()

i = 0
for team in data:
    i += 1
    print(team)
print(i)
