from datetime import datetime
import praw
import pandas as pd
import nltk
from nltk.corpus import stopwords
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os
from flask import Flask, render_template, request, url_for, jsonify
import flask
# replace # with details of your reddit API
reddit = praw.Reddit(client_id='#',client_secret='#', user_agent='#', username='#',password='#')
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    

@app.route('/predict',methods=['POST'])
def predict():
    data = request.files['filename']
    links=data.readlines()
    value=dict()
    for i in range(0,len(links)):
        a=links[i].decode("utf-8")
        val=prediction(a)
        value[a] = val
    return jsonify(value)

def preprocess_text(text):
    text=str(text)
    text=text.lower()# make the text lowercase
    interval_char=re.compile('[/(){}\[\]\|@,;]')
    special_char= re.compile('[^0-9a-z #+_]')
    text=interval_char.sub(' ',text)
    text=special_char.sub('', text)
    words=text.split()
    text = ' '.join(i for i in words if i not in set(stopwords.words('english')))
    return text

def calculate_feature(URL):
    sub=reddit.submission(url=URL)
    df = {"title":[], "score":[],'upvote_ratio':[],
      "locked":[], "orig_content":[], "text":[],"comms_num": [],'comments':[]}
    df["title"].append(sub.title)
    df["score"].append(sub.score)
    df["upvote_ratio"].append(sub.upvote_ratio)
    df["comms_num"].append(sub.num_comments)
    df["text"].append(sub.selftext)
    df["locked"].append(sub.locked)
    df["orig_content"].append(sub.is_original_content)
    sub.comments.replace_more(limit=None)
    comment = ''
    for k in sub.comments:
        comment = comment + ' ' + k.body
    df["comments"].append(comment)    
    df=pd.DataFrame(df)
    return df


def feature_array(url):
    df=calculate_feature(url)
    df['title'] = df['title'].apply(preprocess_text)
    df['text'] = df['text'].apply(preprocess_text)
    df['comments'] = df['comments'].apply(preprocess_text)
    title=df["title"]
    comments=df["comments"]
    text=df['text']
    count_vect_title=pickle.load(open('CountVectorizer_title.p', 'rb'))
    count_vect_text=pickle.load( open('CountVectorizer_text.p', 'rb'))
    count_vect_comments=pickle.load( open('CountVectorizer_comments.p', 'rb'))
    tfidf_transformer_title=pickle.load(open('TFIDF_title.p', 'rb'))
    tfidf_transformer_text=pickle.load(open('TFIDF_text.p', 'rb'))
    tfidf_transformer_comments=pickle.load(open('TFIDF_comments.p', 'rb'))
    TEXT=tfidf_transformer_text.transform(count_vect_text.transform(text))
    TITLE=tfidf_transformer_title.transform(count_vect_title.transform(title))
    COMMENTS=tfidf_transformer_comments.transform(count_vect_comments.transform(comments))
    TITLE=pd.DataFrame(TITLE.toarray())
    TEXT=pd.DataFrame(TEXT.toarray())
    COMMENTS=pd.DataFrame(COMMENTS.toarray())
    fea=pd.concat([TITLE,TEXT,COMMENTS,df['score'],df['upvote_ratio'],
             df['locked'],df['orig_content'],df['comms_num']],axis=1)
    return fea

def prediction(url):
    feature=feature_array(url)
    model=pickle.load(open('random_forest.p', 'rb'))
    predicted=model.predict(feature)
    return predicted[0]



if __name__ == "__main__":
    app.run(debug=True)

