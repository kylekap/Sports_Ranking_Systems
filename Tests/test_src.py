# Standard library
import unittest

# First-party/Local
import config
import core


class test_core(unittest.TestCase):
    NFL2020 = core.sports_season(2020, core.nfl_team, config.nfl_teams)
    NFL2020.all_stats()

    """
    def test_nfl_wins(self):
        self.assertEqual(self.NFL2020.teams.get("clt").wins, 11)

    def test_nfl_opponents(self):
        self.assertEqual(
            self.NFL2020.teams.get("clt").opponents,
            [
                "jax",
                "min",
                "nyj",
                "chi",
                "cle",
                "cin",
                "det",
                "rav",
                "oti",
                "gnb",
                "oti",
                "htx",
                "rai",
                "htx",
                "pit",
                "jax",
            ],
        )

    def test_nfl_beaten_opponents(self):
        self.assertEqual(
            self.NFL2020.teams.get("clt").beaten_opponents,
            ["min", "nyj", "chi", "cin", "det", "oti", "gnb", "htx", "rai", "htx", "jax"],
        )

    def test_nfl_sos(self):
        self.assertEqual(self.NFL2020.teams.get("clt").sos, 7.0625)

    def test_nfl_srs(self):
        self.assertEqual(round(self.NFL2020.teams.get("clt").srs, 4), 3.9596)

    def test_nfl_sov(self):
        self.assertEqual(self.NFL2020.teams.get("clt").sov, 4.1875)

    def test_nfl_pythagorean_expectation(self):
        self.assertEqual(round(self.NFL2020.teams.get("clt").pythagorean_expectation, 6), 0.627377)

    # NCAA2019 = core.sports_season(2019, core.ncaa_team, config.ncaa_teams)
    # NCAA2019.all_stats()
    """


if __name__ == "__main__":
    unittest.main()
