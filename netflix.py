# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def get_recommendations(title):
    data=pd.read_csv('netflix_full.csv')
    df=data.drop(['id','country','creator'],axis=1)
    df['genres']=df['genres'].fillna('x')
    count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
    count_matrix = count_vectorizer.fit_transform(df['genres'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    # Getting the index of the movie that matches the title
    idx = df[df['name'].str.lower()== title.lower().strip()].index[0]

    # Now the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sorting the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # We now get the scores of the 5 most similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    display=df['name'].iloc[movie_indices]
    pattern='([^\d]*)Name:name'
    temp=""
    for recommendation in display:
        temp+=re.sub(pattern, '', recommendation)
        temp+=" / "
    temp.strip()
    return(temp)
        
       
