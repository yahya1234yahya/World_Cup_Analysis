FIFA World Cup Data Analysis




Step 1: Identify the Highest Scoring Teams

    The first step in this project was to analyze all FIFA World Cup tournaments and determine which teams scored the most goals in history.

    Process:

        Load the dataset:

            Combined all CSV files from 1930 to 2022 into a single DataFrame df_full.

            Added a year column to indicate the tournament year.

        Group by team:

            Used groupby('Team') on the Goals For column to calculate total goals scored per team across all tournaments.

        Sort and rename:

            Sorted teams in descending order to find the highest scoring teams.

            Renamed the aggregated column to Total Goals for clarity.
            
        Save the result:

            Exported the results to a CSV file called highest_scoring_teams.csv.