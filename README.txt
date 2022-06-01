Summary
=======

Whenever we visit a digital platform, we no longer need to worry about what to watch next as we are served with a bunch of recommendations to choose from. But how exactly the platform decides what to recommend to a specific user, and if the user is going to like that.
In this project, we attempt to build a specific kind of recommendation system which suggest movies with similar content to the user. The Content-Based Movie Recommender System built using the cosine similarity scores.

The chosen dataset was obtained from Kaggle and is based on publicly accessible Netflix data from 2021, which contains information on 8800+ streaming movies and TV shows at the time. This detailed data includes information such as the movie title, genre, director, cast, release year, country of origin, and content description.
Our model would allow a user to enter a Netflix title or input some description about the movie, and obtain recommendations for comparable titles or with similar descriptions.
The data are contained in the files 'netflix_titles.csv', `links.csv`, `movies.csv`, `ratings.csv` and `tags.csv`. 

DEPENDENCIES:
~ Python 3
~ Scikit-Learn
~ Pandas/Numpy
~ Seaborn/Matplotlib
~ Current Web Browser
~ Jupyter Notebook
~ MLflow
~ Tensorflow
~ Pickle
~ MS Azure Portal
~ Flask, Flasgger APIs
~ Docker
~ Kubernetes

INSTALLATION GUIDE:
~ Install relevant Python packages with Anaconda including Flask and Flasgger
~ www.anaconda.com/products/individual (Python 3, Scikit-Learn & Jupyter Notebook)
~ pandas.pydata.org/pandas-docs/stable/getting_started/install.html
~ Install MLFlow package
~ www.mlflow.org/docs/latest/quickstart.html#installing-mlflow

EXECUTING PROGRAM 
To Start MLflow, go to anaconda prompt and execute:
1) Start MLflow server: 
>> mlflow server --backend-store-uri 'C:/temp/mlflow/localserver'
2) Open browser and go to http://localhost:5000 for MLflow UI
Once MLflow is running, open a new anaconda prompt and execute:
Jupyter Notebook

Run the first experiment, and then go to http://localhost:5000 and view the results in MLFlow. 
The MLFlow portal will list any model runs (successful or not).

Once a model is successfully tracked and saved via MLFlow, it should be tested locally by creating a Flask python file (.py) 
and exposed on a local port (such as 5000) using the Swagger API, entering the proper input to test the expected output


Content and Use of Files
========================

Formatting and Encoding
-----------------------

The dataset files are written as [comma-separated values](http://en.wikipedia.org/wiki/Comma-separated_values) files with a single header row. Columns that contain commas (`,`) are escaped using double-quotes (`"`). These files are encoded as UTF-8. If accented characters in movie titles or tag values (e.g. Misérables, Les (1995)) display incorrectly, make sure that any program reading the data, such as a text editor, terminal, or script, is configured for UTF-8.



Netflix_titles.csv
~---------
The dataset consist of 12 columns, which consists of show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description.

Content Based Recommender
We build an engine that computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine, this also known as Content Based Filtering.

The recommender system was based on:
Movie Description and Taglines
Moreover, we also use Movie Cast, Crew, Keywords and Genre for the recommender system.

Cosine Similarity
We will be using the Cosine Similarity to calculate a numeric quantity that denotes the similarity between two movies. Mathematically, it is defined as follows:

cosine(x,y)=x.y⊺||x||.||y|| 
Since we have used the TF-IDF Vectorizer, calculating the Dot Product will directly give us the Cosine Similarity Score. Therefore, we will use sklearn's linear_kernel since it is much faster.



Movie Ids
~---------

Only movies with at least one rating or tag are included in the dataset. Movie ids are consistent between `ratings.csv`, `tags.csv`, `movies.csv`, and `links.csv` (i.e., the same id refers to the same movie across these four data files).


Ratings Data File Structure (ratings.csv)
-----------------------------------------

All ratings are contained in the file `ratings.csv`. Each line of this file after the header row represents one rating of one movie by one user, and has the following format:

    userId,movieId,rating,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.

Ratings are made on a 5-star scale, with half-star increments (0.5 stars - 5.0 stars).

Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Tags Data File Structure (tags.csv)
-----------------------------------

All tags are contained in the file `tags.csv`. Each line of this file after the header row represents one tag applied to one movie by one user, and has the following format:

    userId,movieId,tag,timestamp

The lines within this file are ordered first by userId, then, within user, by movieId.

Tags are user-generated metadata about movies. Each tag is typically a single word or short phrase. The meaning, value, and purpose of a particular tag is determined by each user.

Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970.


Movies Data File Structure (movies.csv)
---------------------------------------

Movie information is contained in the file `movies.csv`. Each line of this file after the header row represents one movie, and has the following format:

    movieId,title,genres

Movie titles are entered manually or imported from <https://www.themoviedb.org/>, and include the year of release in parentheses. Errors and inconsistencies may exist in these titles.

Genres are a pipe-separated list, and are selected from the following:

* Action
* Adventure
* Animation
* Children's
* Comedy
* Crime
* Documentary
* Drama
* Fantasy
* Film-Noir
* Horror
* Musical
* Mystery
* Romance
* Sci-Fi
* Thriller
* War
* Western
* (no genres listed)
------------------------------------------------------
GIT PUSH & SOURCE CONTROL

echo "# MovieRecommenderSystem" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/CIS325-Group2/MovieRecommenderSystem.git
git push -u origin main

-------------------------------------------------------

Credits
--------
Dataset:
Kaggle source: https://www.kaggle.com/datasets/shivamb/netflix-shows
