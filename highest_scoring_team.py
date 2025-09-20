import pandas as pd


def highest_scoring_team():
    file_name = ['data/FIFA - 1930.csv', 'data/FIFA - 1934.csv', 'data/FIFA - 1938.csv', 'data/FIFA - 1950.csv', 'data/FIFA - 1954.csv', 'data/FIFA - 1958.csv','data/FIFA - 1962.csv', 'data/FIFA - 1966.csv','data/FIFA - 1970.csv','data/FIFA - 1974.csv','data/FIFA - 1978.csv','data/FIFA - 1982.csv','data/FIFA - 1986.csv','data/FIFA - 1990.csv','data/FIFA - 1994.csv','data/FIFA - 1998.csv','data/FIFA - 2002.csv','data/FIFA - 2006.csv','data/FIFA - 2010.csv','data/FIFA - 2014.csv','data/FIFA - 2018.csv','data/FIFA - 2022.csv']
    a = 0
    for name in file_name:
        df = pd.read_csv(name)
        year = name.lstrip('data/FIFA - ')
        year = year.rstrip('.csv')
        df['year'] = year
        if a == 0:
            df_full = df
        else:
            df_full = pd.concat([df_full, df], ignore_index=True)
        a = 1
    df_grouped = df_full.groupby('Team')['Goals For'].sum().sort_values(ascending=False)
    df_grouped.name = 'Total Goals'
    df_grouped.to_csv('highest_scoring_teams.csv')

if __name__ == '__main__':
    highest_scoring_team()