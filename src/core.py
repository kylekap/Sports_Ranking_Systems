# Third-party
import numpy as np
import pandas as pd

# First-party/Local
import config
import util


class sports_season:
    def __init__(self, season, sports_class, teams_dict):
        self.season = season
        self.teams = {}
        for team in teams_dict.values():
            self.teams[team] = sports_class(team)
            self.teams.get(team)._team_info_for_year(team_name=team, year=season)

    def all_stats(self, printout=False):
        self.sos(printout=printout)
        self.sos_bcs(printout=printout)
        self.sov(printout=printout)
        self.srs(printout=printout)
        self.pythagorean_expectation(printout=printout)
        self.CPI(printout=printout)
        self.RPI(printout=printout)
        self.square_gear_rating(printout=printout)

    def sos(self, printout=False):
        # combined win % of all teams facing them. This is used in several other calculations below
        for team_name in self.teams:
            dubs = 0
            games = 0
            opp_list = self.teams.get(team_name).opponents
            for opp in opp_list:
                dubs = dubs + self.teams.get(opp).wins
                games = self.teams.get(opp).wins + self.teams.get(opp).losses + self.teams.get(opp).ties
            self.teams.get(team_name).sos = dubs / games
            if printout:
                print(team_name, "sos", self.teams.get(team_name).sos)

    def sos_bcs(self, printout=False):
        if not hasattr(self.teams.get(list(self.teams.keys())[0]), "sos"):
            self.sos()

        for team_name in self.teams:
            li = []
            for opp_name in self.teams.get(team_name).opponents:
                li.append(self.teams.get(opp_name).sos)

            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li)
            self.teams.get(team_name).sos_bcs = ((opp_pct * 2) + (opp_opp_pct * 1)) / 3
            if printout:
                print(team_name, "sos_bcs", self.teams.get(team_name).sos_bcs)

    def sov(self, printout=False):
        # combined win % of all teams facing them they BEAT
        for team_name in self.teams:
            dubs = 0
            games = 0
            opp_list = self.teams.get(team_name).beaten_opponents
            for opp in opp_list:
                dubs = dubs + self.teams.get(opp).wins
                games = games + self.teams.get(opp).wins + self.teams.get(opp).losses + self.teams.get(opp).ties
            self.teams.get(team_name).sov = dubs / games if games else 0
            if printout:
                print(team_name, "sov", self.teams.get(team_name).sov)

    def srs(self, printout=False):
        # own_rating - (1 / games) * (rating + ... + rating) = -spread
        coefficients = []
        spreads = []
        for team_name, team in self.teams.items():
            games = len(team.opponents)
            row = []
            for opp in self.teams:
                if opp == team_name:
                    # own_rating
                    row.append(1)
                elif opp in team.opponents:
                    # 1/games, since opponents rating
                    row.append(-1 / games)
                else:
                    # did not play, do not include
                    row.append(0)

            coefficients.append(row)
            spreads.append(team.spread)

        solutions = np.linalg.solve(np.array(coefficients), np.array(spreads))
        ratings = list(zip(self.teams.keys(), solutions))
        for ea in ratings:
            self.teams[ea[0]].srs = ea[1]
            if printout:
                print(ea[0], ea[1])

    def pythagorean_expectation(self, printout=False):
        for team_name in self.teams:
            team_obj = self.teams.get(team_name)
            expectation = (team_obj.points_for**team_obj.expon) / (
                (team_obj.points_for**team_obj.expon) + (team_obj.points_against**team_obj.expon)
            )
            self.teams.get(team_name).pythagorean_expectation = expectation
            if printout:
                print(team_name, "expectation", expectation)

    def CPI(self, printout=False):
        # (Win% ** 3) * (Opp% ** 2) * (Opp_Opp ** 1)... so SOS ?
        if not hasattr(self.teams.get(list(self.teams.keys())[0]), "sos"):
            self.sos()

        for team_name in self.teams:
            li = []
            for opp_name in self.teams.get(team_name).opponents:
                li.append(self.teams.get(opp_name).sos)

            win_pct = self.teams.get(team_name).wins / sum(
                self.teams.get(team_name).wins, self.teams.get(team_name).losses, self.teams.get(team_name).ties
            )
            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li)
            self.teams.get(team_name).cpi = (win_pct**3) * (opp_pct**2) * (opp_opp_pct**1)
            if printout:
                print(team_name, "cpi", self.teams.get(team_name).cpi)

    def RPI(self, printout=False):
        # (Win% .25) + (Opp% * .5) + (Opp_Opp * .25)
        if not hasattr(self.teams.get(list(self.teams.keys())[0]), "sos"):
            self.sos()

        for team_name in self.teams:
            li = []
            for opp_name in self.teams.get(team_name).opponents:
                li.append(self.teams.get(opp_name).sos)

            win_pct = self.teams.get(team_name).wins / sum(
                self.teams.get(team_name).wins, self.teams.get(team_name).losses, self.teams.get(team_name).ties
            )
            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li)
            self.teams.get(team_name).cpi = (win_pct * 0.25) + (opp_pct * 0.5) + (opp_opp_pct * 0.25)
            if printout:
                print(team_name, "rpi", self.teams.get(team_name).rpi)

    def square_gear_rating(self, printout=False):
        # (Win% + Opp% + Opp_Opp%)/3
        if not hasattr(self.teams.get(list(self.teams.keys())[0]), "sos"):
            self.sos()

        for team_name in self.teams:
            li = []
            for opp_name in self.teams.get(team_name).opponents:
                li.append(self.teams.get(opp_name).sos)

            win_pct = self.teams.get(team_name).wins / sum(
                self.teams.get(team_name).wins, self.teams.get(team_name).losses, self.teams.get(team_name).ties
            )
            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li)
            self.teams.get(team_name).square_gear_rating = (win_pct + opp_pct + opp_opp_pct) / 3
            if printout:
                print(team_name, "square_gear_rating", self.teams.get(team_name).square_gear_rating)


class nfl_team:
    def __init__(team, name):
        # team here replaces "self"
        team.team_name = name
        team.expon = 2.37  # for the Pythagorean Expectation calculation. Depends on sport

    def _team_info_for_year(team, team_name, year):
        # team here replaces "self"
        url = f"https://www.pro-football-reference.com/teams/{team_name}/{year}.htm"
        df = pd.read_html(url, header=[0, 1])[1]
        # Configure dataframe
        df.columns = config.nfl_football_headers
        df["SeasonWeek"] = pd.to_numeric(df["SeasonWeek"], errors="coerce")
        df = df[df["Result"].isin(["W", "L", "T"]) & df["SeasonWeek"].isin(range(1, 19))]
        df["Opponent"] = df["Opponent"].map(config.nfl_teams)

        # Set up team specific information
        team.wins = sum(df["Result"] == "W")
        team.losses = sum(df["Result"] == "L")
        team.ties = sum(df["Result"] == "T")
        team.opponents = df["Opponent"].tolist()
        team.points_for = sum(df["PointsFor"])
        team.points_against = sum(df["PointsAgainst"])
        team.spread = (team.points_for - team.points_against) / len(team.opponents)
        team.beaten_opponents = df["Opponent"].loc[df["Result"] == "W"].tolist()


class ncaa_team:
    def __init__(team, name):
        # team here replaces "self"
        team.team_name = name
        team.expon = 2.37  # for the Pythagorean Expectation calculation. Depends on sport

    def _team_info_for_year(team, team_name, year):
        # team here replaces "self"
        url = f"https://www.sports-reference.com/cfb/schools/{team_name}/{year}-schedule.html"
        df = pd.read_html(url, header=[0])[-1]
        # Configure dataframe
        df.columns = config.ncaa_football_headers
        df["SeasonWeek"] = pd.to_numeric(df["SeasonWeek"], errors="coerce")
        df = df[df["Result"].isin(["W", "L", "T"]) & df["SeasonWeek"].isin(range(1, 19))]
        df["Opponent"] = util.loop_replace_li(list(df["Opponent"]), config.ncaa_ranks)
        df["Opponent"] = [
            x if x not in config.ncaa_teams else config.ncaa_teams[x] for x in [str(x) for x in df["Opponent"]]
        ]
        df["Opponent"] = [x for x in df["Opponent"] if x != "nan"]

        # Set up team specific information
        team.wins = sum(df["Result"] == "W")
        team.losses = sum(df["Result"] == "L")
        team.ties = sum(df["Result"] == "T")
        team.opponents = list(df.loc[~df["Conference"].str.contains("Major"), "Opponent"])
        team.points_for = sum(df["PointsFor"])
        team.points_against = sum(df["PointsAgainst"])
        team.spread = (team.points_for - team.points_against) / len(team.opponents)
        team.beaten_opponents = [x for x in team.opponents if x in df["Opponent"].loc[df["Result"] == "W"].tolist()]


def main():
    NFL2020 = sports_season(2020, nfl_team, config.nfl_teams)
    NFL2020.sos_bcs(printout=True)

    # NCAA2019 = sports_season(2019, ncaa_team, config.ncaa_teams)
    # NCAA2019.all_stats()


if __name__ == "__main__":
    """[summary]"""
    main()
