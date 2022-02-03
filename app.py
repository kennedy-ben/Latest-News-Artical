from distutils.log import debug
import string
from flask import Flask, render_template
from newsapi import NewsApiClient




app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="30ff088b266c4f0c9fa8b0457185680f")
    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge',
                                          language='en')
    print(top_headlines,'news')                                          
                                         
    return render_template("index.html", articles = top_headlines["articles"])


    # articales = topheadlines['articles']

    # desc = []
    # news = []
    # img = []



    # for i in range(len(articales)):
    #     myarticles = articales[i]


    #     news.append(myarticles['title'])
    #     desc.append(myarticles['description'])
    #     img.append(myarticles['urlToImage'])


        
    #     mylist = zip(news, desc, img)


    #     return render_template('index.html', context=mylist)


if __name__== "_main_":
    app.run(debug=True)

