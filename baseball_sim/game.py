position_dict = {1: "P", 2: "C", 3: "1B", 4: "2B", 5: "3B", 6: "SS", 7: "LF", 8: "CF", 9: "RF", "DH": "DH"}

team_home_name = input("Input home team: ")
team_away_name = input("Input away team: ")

print("Simulating {} v. {}...".format(team_away_name, team_home_name))

print("Confirming starting lineup for {}...".format(team_away_name))
game_teams = [team_away_name, team_home_name]


def define_lineup(team_name):
    # confirm starting lineup, position, and roster
    print("Input roster by batting order for {}!".format(team_name))
    is_dh = input("Is there a DH (Y/N): ")
    lineup = {}
    for i in range(1, 10):
        player = input("Player name: ")
        pos = input("Player pos (number): ")

        if pos.upper() != "DH":
            lineup[int(pos)] = player
        else:
            lineup[pos] = player

    if is_dh.lower() == "y":
        pitcher = input("Starting pitcher: ")
        lineup[1] = pitcher

    print("Confirm lineup for {}".format(team_name))
    for player in lineup:
        print(position_dict[player] + " : " + lineup[player])

    return lineup


for team in game_teams:
    team_home = define_lineup(team)








