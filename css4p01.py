
import pandas as pd

# Load the dataset
df = pd.read_csv('movie_dataset.csv')

# Cleaning the data (example steps, assuming these were performed)
# df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].mean(), inplace=True)
# df.dropna(inplace=True)

# Analysis for Question 4: How many movies were released in 2016?
movies_2016_count = df[df['Year'] == 2016].shape[0]

# Analysis for Question 5: How many movies were directed by Christopher Nolan?
nolan_movies_count = df[df['Director'] == 'Christopher Nolan'].shape[0]

# Analysis for Question 6: How many movies have a rating of at least 8.0?
highly_rated_movies_count = df[df['Rating'] >= 8.0].shape[0]

# Analysis for Question 7: What is the median rating of movies directed by Christopher Nolan?
nolan_median_rating = df[df['Director'] == 'Christopher Nolan']['Rating'].median()

# Analysis for Question 8: Find the year with the highest average rating.
year_highest_avg_rating = df.groupby('Year')['Rating'].mean().idxmax()

# Analysis for Question 9: What is the percentage increase in number of movies made between 2006 and 2016?
movies_2006 = df[df['Year'] == 2006].shape[0]
percentage_increase = ((movies_2016_count - movies_2006) / movies_2006) * 100

# Analysis for Question 10: Find the most common actor in all the movies.
all_actors = df['Actors'].str.split(',').explode()
most_common_actor = all_actors.value_counts().idxmax()

# Analysis for Question 11: How many unique genres are there in the dataset?
unique_genres = df['Genre'].str.split(',').explode().nunique()

# Correlation analysis for Question 12
correlation_matrix = df.corr()

# Insights from correlation
# Strong positive correlation between 'Votes' and 'Revenue (Millions)'
# Strong positive correlation between 'Metascore' and 'Rating'
# Positive correlation between 'Votes' and 'Rating'
# Moderate positive correlation between 'Votes' and 'Runtime (Minutes)'
# Moderate positive correlation between 'Rating' and 'Runtime (Minutes)'

# Advice to directors based on analysis (to be added)

# Save the script as a .py file
script_file = 'css4p01.py'
with open(script_file, 'w') as file:
    file.write(python_script)
