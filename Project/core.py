#https://realpython.com/python-pep8/

import requests

import pandas as pd

import config

def import_team_year(team,year):
    url = f'https://www.pro-football-reference.com/teams/{team}/{year}.htm'
    df = pd.read_html(url,header=[0,1])[1]
    df.columns = config.pro_football_headers
    df['SeasonWeek'] = pd.to_numeric(df['SeasonWeek'], errors='coerce')
    df = df[df['Result'].isin(['W','L','T']) & df['SeasonWeek'].isin(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])]
    df['Opponent'] = df['Opponent'].replace(config.nfl_names)
    df['Team'] = team
    return df


def import_nfl(year):
    df_list = []
    for team in config.nfl_franchises:
        df_list.append(import_team_year(team,year))
    return pd.concat(df_list)


def wl_calculator(full_df):
    wl_table = full_df.pivot_table(index='Team', columns='Result', aggfunc='size', fill_value=0)
    wl_table['PCT'] = wl_table['W']/(wl_table['W']+wl_table['L'])
    wl_df = pd.merge(full_df, wl_table, left_on='Team',right_index=True, how='inner')
    wl_df = pd.merge(wl_df, wl_table, left_on='Opponent',suffixes=['_Team','_Opponent'],right_index=True, how='inner')
    return wl_df


def main():
    # main function that you use to run the program
    df = import_nfl(2020)
    df = wl_calculator(df)
    df = df.pivot_table(values=['PCT_Team','PCT_Opponent'], index='Team',aggfunc=['mean','sum'],fill_value=0,sort=True)
    df.columns = ['_'.join(col).strip() for col in df.columns.values]
    df.to_csv('Test.CSV')


if __name__ == '__main__':
    main()
