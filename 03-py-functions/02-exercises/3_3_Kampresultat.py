def show_match_result(home_team, away_team, home_score, away_score):
    if home_score > away_score:
        print(f"{home_team} won over {away_team}, with the score {home_score} vs {away_score}")
    elif home_score < away_score:
        print(f"{away_team} won over {home_team}, with the score {away_score} vs {home_score}")
    else:
        print(f"{home_team} and {away_team} was equally good, and scored {home_score} point each")


show_match_result("Norway", "Spain", 3, 2)
show_match_result("Spain", "England", 0, 2)
show_match_result("Island", "Sweden", 1, 1)

