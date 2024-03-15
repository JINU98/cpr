from __future__ import annotations
from flask import Flask, render_template, request
import requests
import datetime
import gensim.downloader as gensim_api
# from gensim.matutils import softcossim
from gensim import corpora
from flask import Flask
from flask_cors import CORS
from PKiL import ProKnow
import json
import regex as re

app = Flask(__name__)
cors = CORS(app)
pk1 = ProKnow()
pk1.process_knowledge('cssrs.txt','cssrs_annotate.txt')

word2vec_model300 = gensim_api.load('word2vec-google-news-300')

convos = []



@app.route("/")
def home(): return "HEllo"

# time = lambda: datetime.datetime.now().strftime("%H:%M")




@app.route("/get")
def get():
    annotations=[]
    test = request.args.get('posts')
    # print("test",test)
    posts = re.sub(r'\.+', ".", request.args.get('posts')).split("||")
    # posts=[re.sub('nn', '', post) for post in posts]
    print("posts",posts)
    print("length of post",len(posts))

    # posts = posts[1:10]

    # pool=Pool()
    
    # def getLabel(post):
    #     label = pk1.evaluate_pk(post,explanation=True)
    #     annotations.append(label)
    #     return label
    
    # pool.map(getLabel,posts)

    for post in posts:
        label = pk1.evaluate_pk(post,explanation=True)
        print("label",label)
        annotations.append(label)
    return annotations

    # return annotations

if __name__ == "__main__":
    app.run(debug=True)