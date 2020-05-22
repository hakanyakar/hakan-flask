from flask import Flask, redirect, url_for, render_template, request, flash
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    return render_template("games.html")

@app.route("/mrs", methods=['GET', 'POST'])
def mrs():
    if request.method == "POST":
        film_name = request.form['filmname']
        
        ratings_data = pd.read_csv("ml/ratings.csv")#reading ratings csv
        #print(ratings_data.head())

        movie_names = pd.read_csv("ml/movies.csv")#reading movies csv
        movie_names['title'] = movie_names['title'].str.split('(', 1).str[0].str.strip()#Splitting years from movie title
        #print(movie_names.head())

        movie_data = pd.merge(ratings_data, movie_names, on='movieId')#merge two frames.
        #print(movie_data.head())

        #print(movie_data.groupby('title')['rating'].mean().head())#First 5 movies and their average ratings.

        #print(movie_data.groupby('title')['rating'].mean().sort_values(ascending=False).head())#sort the ratings in the descending order of their average ratings.

        #print(movie_data.groupby('title')['rating'].count().sort_values(ascending=False).head())#total number of ratings for a movie.

        ratings_mean_count = pd.DataFrame(movie_data.groupby('title')['rating'].mean())#add the average rating of each movie
        ratings_mean_count['rating_counts'] = pd.DataFrame(movie_data.groupby('title')['rating'].count())#add the number of ratings for a movie to the ratings_mean_count dataframe.
        #print(ratings_mean_count.head())#movie title, along with the average rating and number of ratings for the movie.

        user_movie_rating = movie_data.pivot_table(index='userId', columns=['title'], values='rating')#To create the matrix of movie titles and corresponding user ratings.
        #print(user_movie_rating.head())
    
        film_ratings = user_movie_rating[film_name] #This returns a Pandas series
        #print(forrest_gump_ratings.head())

        movies_like_film_name = user_movie_rating.corrwith(film_ratings)

        corr_film_name = pd.DataFrame(movies_like_film_name, columns=['Correlation'])
        corr_film_name.dropna(inplace=True)
        corr_film_name.sort_values('Correlation', ascending=False).head(10)

        corr_film_name = corr_film_name.join(ratings_mean_count['rating_counts'])
        

        return render_template('mrs.html', film_ratings=corr_film_name[corr_film_name ['rating_counts']>50].sort_values('Correlation', ascending=False).head(10).to_html(classes="table"))
    else:
        return render_template("mrs.html")


    


if __name__ == "__main__":
    app.run(debug=True)