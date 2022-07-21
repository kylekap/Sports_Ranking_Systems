# Third-party
import pandas as pd

# First-party/Local
import config


class sports_season:
    def __init__(self, season, sports_class, teams_dict):
        self.season = season
        self.teams = {}
        for team in teams_dict.values():
            self.teams[team] = sports_class(team)
            self.teams.get(team)._team_info_for_year(team_name=team, year=season)

    def sos(self, printout=False):
        # combined win % of all teams facing them
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

    def sov(self, printout=False):
        # combined win % of all teams facing them they BEAT
        for team_name in self.teams:
            dubs = 0
            games = 0
            opp_list = self.teams.get(team_name).beaten_opponents
            for opp in opp_list:
                dubs = dubs + self.teams.get(opp).wins
                games = self.teams.get(opp).wins + self.teams.get(opp).losses + self.teams.get(opp).ties
            self.teams.get(team_name).sov = dubs / games
            if printout:
                print(team_name, "sov", self.teams.get(team_name).sov)

    def srs(self):
        return None

    def pythagorean_expectation(self, printout=False):
        expon = 2.37
        for team_name in self.teams:
            expectation = self.teams.get(team_name).points_for ** expon / (
                (self.teams.get(team_name).points_for ** expon) + (self.teams.get(team_name).points_against ** expon)
            )
            self.teams.get(team_name).pythagorean_expectation = expectation
            if printout:
                print(team_name, "expectation", expectation)


class nfl_team:
    def __init__(team, name):
        # team here replaces "self"
        team.team_name = name
        team.sos = 0
        team.sov = 0
        team.srs = 0
        team.pythagorean_expectation = 0

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
        team.spread = team.points_for - team.points_against
        team.beaten_opponents = df["Opponent"].loc[df["Result"] == "W"].tolist()


class ncaa_team:
    def __init__(team, name):
        # team here replaces "self"
        team.team_name = name
        team.sos = 0
        team.sov = 0
        team.srs = 0
        team.pythagorean_expectation = 0

    def _team_info_for_year(team, team_name, year):
        # team here replaces "self"
        url = f"https://www.sports-reference.com/cfb/schools/{team_name}/{year}-schedule.html"
        df = pd.read_html(url, header=[0])[1]
        # Configure dataframe
        df.columns = config.ncaa_football_headers
        df["SeasonWeek"] = pd.to_numeric(df["SeasonWeek"], errors="coerce")
        df = df[df["Result"].isin(["W", "L", "T"]) & df["SeasonWeek"].isin(range(1, 19))]
        df["Opponent"] = df["Opponent"].map(config.ncaa_teams)

        # Set up team specific information
        team.wins = sum(df["Result"] == "W")
        team.losses = sum(df["Result"] == "L")
        team.ties = sum(df["Result"] == "T")
        team.opponents = df["Opponent"].tolist()
        team.points_for = sum(df["PointsFor"])
        team.points_against = sum(df["PointsAgainst"])
        team.spread = team.points_for - team.points_against
        team.beaten_opponents = df["Opponent"].loc[df["Result"] == "W"].tolist()


def main():
    NFL2020 = sports_season(2020, nfl_team, config.nfl_teams)
    NFL2020.sos()
    NFL2020.sov()
    NFL2020.pythagorean_expectation()


if __name__ == "__main__":
    """[summary]"""
    main()
