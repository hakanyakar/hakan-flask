import numpy as np
import pandas as pd
import re

ratings_data = pd.read_csv("ml/ratings.csv")#reading ratings csv
#print(ratings_data.head())

movie_names = pd.read_csv("ml/movies.csv")#reading movies csv
movie_names['title'] = movie_names['title'].str.split('(', 1).str[0].str.strip()
print(movie_names.head())


# movie_data = pd.merge(ratings_data, movie_names, on='movieId')#merge two frames.
# #print(movie_data.head())

# #print(movie_data.groupby('title')['rating'].mean().head())#First 5 movies and their average ratings.

# #print(movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head())#sort the ratings in the descending order of their average ratings.

# #print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())#total number of ratings for a movie.

# ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())#add the average rating of each movie
# ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())#add the number of ratings for a movie to the ratings_mean_count dataframe.
# #print(ratings_mean_count.head())#movie title, along with the average rating and number of ratings for the movie.

# user_movie_rating = movie_data.pivot_table(index='userId', columns='title', values='rating')#To create the matrix of movie titles and corresponding user ratings.
# #print(user_movie_rating.head())

# film_ratings = user_movie_rating['Forrest Gump (1994)']
# #print(film_ratings.to_frame().head())

# movies_like_film_name = user_movie_rating.corrwith(film_ratings)

# corr_film_name = pd.DataFrame(movies_like_film_name, columns=['Correlation'])
# corr_film_name.dropna(inplace=True)
# #print(corr_film_name.head())
