import pandas as pd


def highest_scoring_team():
    file_name = ['FIFA - 1930.csv', 'FIFA - 1934.csv', 'FIFA - 1938.csv', 'FIFA - 1950.csv', 'FIFA - 1954.csv', 'FIFA - 1958.csv','FIFA - 1962.csv', 'FIFA - 1966.csv','FIFA - 1970.csv','FIFA - 1974.csv','FIFA - 1978.csv','FIFA - 1982.csv','FIFA - 1986.csv','FIFA - 1990.csv','FIFA - 1994.csv','FIFA - 1998.csv','FIFA - 2002.csv','FIFA - 2006.csv','FIFA - 2010.csv','FIFA - 2014.csv','FIFA - 2018.csv','FIFA - 2022.csv']
    a = 0
    for name in file_name:
        df = pd.read_csv(name)
        year = name.lstrip('FIFA - ')
        year = year.rstrip('.csv')
        df['year'] = year
        if a == 0:
            df_full = df
        else:
            df_full = pd.concat([df_full, df], ignore_index=True)
        a = 1
    df_grouped = df_full.groupby('Team')['Goals For'].sum().sort_values(ascending=False)
    print(df_grouped.head(1))

if __name__ == '__main__':
    highest_scoring_team()