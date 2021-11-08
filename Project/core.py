#https://realpython.com/python-pep8/

import requests

import pandas as pd

import config

def import_team_year(team,year):
    url = f'https://www.pro-football-reference.com/teams/{team}/{year}.htm'
    df = pd.read_html(url,header=[0,1])[1]
    df.columns = config.pro_football_headers
    df['SeasonWeek'] = pd.to_numeric(df['SeasonWeek'], errors='coerce')
    df = df[df['SeasonWeek'].isin([range(1,17,1)]) & df['Result'].isin(['W','L','T','w','l','t'])]
    df['Opponent'] = df['Opponent'].replace(config.nfl_names)
    df['Team'] = team
    return df


def import_nfl():
    df_list = []
    for team in config.nfl_franchises:
        df_list.append(import_team_year(team,2020))
    return pd.concat(df_list)


def main():
    # main function that you use to run the program
    df = import_nfl()
    print(df.dtypes)
    df.to_csv('Test.CSV')

if __name__ == '__main__':
    main()
