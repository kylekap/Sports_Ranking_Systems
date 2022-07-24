# First-party/Local
import config
import sports_classes


def main():
    for key, val in config.config_info.items():
        print(key)
        Season2020 = sports_classes.sports_season(2020, key, sports_classes.sports_team)
        Season2020.sos(printout=True)
    # for key, val in Season2020.teams.get("MEM").__dict__.items():
    #     print(key, val)


if __name__ == "__main__":
    """[summary]"""
    main()
