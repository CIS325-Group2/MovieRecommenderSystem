import string
import pandas as pd
import numpy as np
import pickle
import requests
from flask import Flask, request
from sklearn.neighbors import NearestNeighbors
from flasgger import Swagger
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

swagger = Swagger(app)

@app.route('/netflix_recommendations', methods=["POST"])

def predict_sign():
    """Endpoint giving Netflix recommendations based on an input description
    ---
    parameters:
        -   name: description
            in: formData
            type: string
            required: True

        -   name: number_recommendations
            in: formData
            type: string
            required: True


    """

    recommender_model_filename = "./Netflix_models/nearest_neighbors_model.pkl/model.pkl"
    vectorizer_filename = "./Netflix_models/tfidf_vectorizer.pkl/model.pkl"

    with open(recommender_model_filename, "rb") as file:
        neighbors = pickle.load(file)

    with open(vectorizer_filename, "rb") as file2:
        tfidf = pickle.load(file2)
    
    df = pd.read_csv("netflix_titles.csv")

    input_row = request.form["description"]
    number_recommendations = int(request.form["number_recommendations"])

    input_data = tfidf.transform(input_row.split())

    top_recommendations = neighbors.kneighbors(input_data, n_neighbors=number_recommendations)
    title_indices = top_recommendations[1][0]
    titles = [df.iloc[row]['title'] for row in title_indices]
    
    title_dict = {}

    for key, value in enumerate(titles):
        title_dict[key] = value

    return(title_dict)


if __name__ == '__main__':
    app.run(debug=True)
