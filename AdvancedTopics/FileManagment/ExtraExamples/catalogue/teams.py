from io import open
file = open("soccer.txt", "r", encoding = "utf8")
lines = file.readlines()
file.close

teamL = []

for line in lines:
    sep = line.strip("\n").split(";")
    team = {"ID":sep[0], "Team":sep[1], "Location":sep[2], "Foundation":sep[3]}
    teamL.append(team)

for team in teamL:
    print("ID {}: The {} is located in {} and was founded in the year {}".format
    (team["ID"], team["Team"], team["Location"], team["Foundation"]))