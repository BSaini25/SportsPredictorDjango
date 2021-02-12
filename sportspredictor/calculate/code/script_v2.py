from datetime import datetime
import math

# def main():
#     lg = input("Which league? ")

#     if lg.lower() == "nfl":
#         from sportsipy.nfl.teams import Teams
#     elif lg.lower() == "mlb":
#         from sportsipy.mlb.teams import Teams
#     elif lg.lower() == "nhl":
#         from sportsipy.nhl.teams import Teams
#     elif lg.lower() == "nba":
#         from sportsipy.nba.teams import Teams
#     else:
#         print("Error!")
#         return

#     teams = Teams()
#     calculate(lg.lower(), teams)

def calculate(lg, teams, away=None, home=None):
    """
    Calculates game score and probability of win
    :type lg: string
    :type teams: Teams
    :rtype: None
    """
    lg_pf = get_league_average(lg, teams)

    # Getting points per game tuples for away and home teams
    if (away is None) and (home is None):
        away_input = input("Away team? ")
        home_input = input("Home team? ")
    else:
        away_input = away
        home_input = home

    away_team = get_team(teams, away_input)
    away_ppg = get_ppg_tuple(lg.lower(), away_team)

    home_team = get_team(teams, home_input)
    home_ppg = get_ppg_tuple(lg.lower(), home_team)

    away_score = (away_ppg[0] / lg_pf) * (home_ppg[1] / lg_pf) * lg_pf
    home_score = (home_ppg[0] / lg_pf) * (away_ppg[1] / lg_pf) * lg_pf
    spread = math.fabs(away_score - home_score)
    total = away_score + home_score

    return(f"{away_team.name}: {away_score:.1f} - {home_team.name}: {home_score:.1f}\nSpread: {spread:.1f}, Total: {total:.1f}\n\n")


def get_league_average(lg, teams):
    """
    Get league average points per game
    :type lg: string
    :type teams: Teams
    :rtype: float
    """
    lg_gp = 0
    lg_pf = 0.0
    lg_pa = 0.0

    if lg.lower() == "nfl":
        for team in teams:
            lg_gp = lg_gp + team.games_played
            lg_pf = lg_pf + team.points_for
        lg_gpa = lg_gp / 32
        lg_pfa = lg_pf / 32
    elif lg.lower() == "mlb":
        for team in teams:
            lg_gp = lg_gp + team.games_played
            lg_pf = lg_pf + team.runs
        lg_gpa = lg_gp / 30
        lg_pfa = lg_pf / 30
    elif lg.lower() == "nhl":
        for team in teams:
            lg_gp = lg_gp + team.games_played
            lg_pf = lg_pf + team.goals_for
        lg_gpa = lg_gp / 31
        lg_pfa = lg_pf / 31
    elif lg.lower() == "nba":
        for team in teams:
            lg_gp = lg_gp + team.games_played
            lg_pf = lg_pf + team.points
        lg_gpa = lg_gp / 30
        lg_pfa = lg_pf / 30

    return lg_pfa / lg_gpa


def get_team(teams, team_input):
    """
    Returns desired Team from Teams
    :type teams: Teams
    :type team_input: string
    :rtype: Team
    """
    for team in teams:
        if team_input.lower() in team.name.lower():
            return team


def get_ppg_tuple(lg, team):
    """
    Returns a tuple of team's ppg for and ppg against.
    :type lg: string
    :type team: string
    :rtype: float tuple
    """
    if lg.lower() == "nfl":
        gp = team.games_played
        pf = team.points_for
        pf = pf / gp
        pa = team.points_against
        pa = pa / gp
        tup = (pf, pa)
    elif lg.lower() == "mlb":
        rf = team.runs_for
        ra = team.runs_against
        tup = (rf, ra)
    elif lg.lower() == "nhl":
        gp = team.games_played
        gf = team.goals_for
        gf = gf / gp
        ga = team.goals_against
        ga = ga / gp
        tup = (gf, ga)
    elif lg.lower() == "nba":
        gp = team.games_played
        pf = team.points
        pf = pf / gp
        pa = team.opp_points
        pa = pa / gp
        tup = (pf, pa)
    
    return tup


# main()
