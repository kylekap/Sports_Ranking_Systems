# Third-party
import numpy as np
import pandas as pd

# First-party/Local
import config
import util


class sports_team:
    def __init__(team, team_name, configuration):
        # team here replaces "self"
        team.team_name = team_name
        team._expon = configuration.get("expon", 1)
        team._sports_headers = configuration.get("headers", 1)
        team._sports_teams = configuration.get("teams", 1)
        team._html_header = configuration.get("header_rows", 1)
        team._html_table = configuration.get("html_table", 1)
        team._url_base = configuration.get("url_base", 1)

    def _team_info_for_year(team, year):
        # team here replaces "self"
        url = team._url_base.format(team_name=team.team_name, year=year)
        try:
            df = pd.read_html(url, header=team._html_header)[team._html_table]
        except Exception as E:
            print(E, url, "\n", type(E).__name__, __file__, E.__traceback__.tb_lineno)
            team.wins = 0
            team.losses = 0
            team.ties = 0
            team.opponents = []
            team.points_for = 0
            team.points_against = 0
            team.spread = 0
            team.beaten_opponents = []
            team.lost_opponents = []
            team.tied_opponents = []
            return None

        # Configure dataframe
        if len(df.columns) < len(team._sports_headers):
            for ea in range(len(team._sports_headers) - len(df.columns)):
                df[ea] = ""
        df.columns = team._sports_headers
        # df["Game#"] = pd.to_numeric(df["Game#"], errors="coerce")
        df[["Game#", "PointsFor", "PointsAgainst"]] = df[["Game#", "PointsFor", "PointsAgainst"]].apply(
            pd.to_numeric, errors="coerce"
        )
        df["Result"] = df["Result"].replace(["L-wo"], "L")  # remove walkoff wins/losses (baseball relevant)
        df = df[df["Result"].isin(["W", "L", "T"]) & df["Game#"].isin(range(1, 200))]  # Ensures regular season
        df["Opponent"] = util.loop_replace_li(list(df["Opponent"]), config.ncaa_ranks)  # Remove NCAA rankings
        df["Opponent"] = [
            (
                "nan"
                if x not in team._sports_teams and x not in team._sports_teams.values()
                else team._sports_teams.get(x, x)
            )
            for x in [str(x) for x in df["Opponent"]]
        ]  # Ensure opponent is in the league
        df = df.loc[df["Opponent"] != "nan"]  # Remove invalid opponents or bye weeks
        # Set up team specific information
        team.wins = sum(df["Result"] == "W")
        team.losses = sum(df["Result"] == "L")
        team.ties = sum(df["Result"] == "T")

        team.opponents = df["Opponent"]
        team.points_for = sum(df["PointsFor"])
        team.points_against = sum(df["PointsAgainst"])
        team.spread = (team.points_for - team.points_against) / len(team.opponents) if len(team.opponents) else 0

        team.beaten_opponents = [x for x in team.opponents if x in df["Opponent"].loc[df["Result"] == "W"].tolist()]
        team.lost_opponents = [x for x in team.opponents if x in df["Opponent"].loc[df["Result"] == "L"].tolist()]
        team.tied_opponents = [x for x in team.opponents if x in df["Opponent"].loc[df["Result"] == "T"].tolist()]


class sports_season:
    def __init__(self, season, league, sports_class):
        self.season = season
        self.league = league.lower()
        self.teams = {}
        for team in config.config_info.get(self.league).get("teams").values():
            self.teams[team] = sports_class(team, config.config_info.get(self.league))
            self.teams.get(team)._team_info_for_year(year=season)

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
                games = games + self.teams.get(opp).wins + self.teams.get(opp).losses + self.teams.get(opp).ties
            self.teams.get(team_name).sos = dubs / games if games else 0
            if printout:
                print(
                    team_name,
                    "",
                    self.teams.get(team_name).sos,
                    f"\nOpp played {games} games",
                    "",
                    f"Opponents won {dubs}",
                )

    def sos_bcs(self, printout=False):
        if not hasattr(self.teams.get(list(self.teams.keys())[0]), "sos"):
            self.sos()

        for team_name in self.teams:
            li = []
            for opp_name in self.teams.get(team_name).opponents:
                li.append(self.teams.get(opp_name).sos)

            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li) if len(li) else 0
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
            games = max(len(team.opponents), 1)
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
            top = team_obj.points_for**team_obj._expon
            bottom = (team_obj.points_for**team_obj._expon) + (team_obj.points_against**team_obj._expon)
            expectation = top / bottom if bottom else 0
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
            games = self.teams.get(team_name).wins + self.teams.get(team_name).losses + self.teams.get(team_name).ties
            win_pct = self.teams.get(team_name).wins / games if games else 0
            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li) if len(li) else 0
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
            games = self.teams.get(team_name).wins + self.teams.get(team_name).losses + self.teams.get(team_name).ties
            win_pct = self.teams.get(team_name).wins / games if games else 0
            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li) if len(li) else 0
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
            games = self.teams.get(team_name).wins + self.teams.get(team_name).losses + self.teams.get(team_name).ties
            win_pct = self.teams.get(team_name).wins / games if games else 0
            opp_pct = self.teams.get(team_name).sos
            opp_opp_pct = sum(li) / len(li) if len(li) else 0
            self.teams.get(team_name).square_gear_rating = (win_pct + opp_pct + opp_opp_pct) / 3
            if printout:
                print(team_name, "square_gear_rating", self.teams.get(team_name).square_gear_rating)
