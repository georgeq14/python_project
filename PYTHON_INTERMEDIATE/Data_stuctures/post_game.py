
goats = [
    {"name": "Lebron James", "Position": "Power Forward", "PPG": 27.5, "APG": 7.4, "RPG": 7.5, "SPG": 1.5},
    {"name": "Michael Jordan", "Position": "Shooting Guard", "PPG": 30.1, "APG": 5.3, "RPG": 6.2, "SPG": 2.3}
]
#getting the names
names = [player["name"] for player in goats]
print("The names of the players are:", names)

#Getting the positions
postions = [player["Position"] for player in goats]
print("The positions of the players are:", postions)

#update game statistics of a player
goats[0]["PPG"] += 10

#calculate average points per games
avgPPG = sum([player["PPG"] for player in goats]) / len(goats)
print("The average points per game is:", avgPPG)

