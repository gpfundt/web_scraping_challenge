import pymongo
from flask import Flask, render_template
from scrape_mars import scrape

client = pymongo.MongoClient()
db = client.mars_db
col = db.scraped_mars

app = Flask(__name__)
@app.route("/")
def homepagething():
    render_template("mars_info.html", scraped = scraped)

@app.route("/scrape")
def getmarsinfo():

    scraped = scrape()
    mars_info=db.posts
    posts_id = mars_info.insert_one(scraped).inserted_id

if __name__ == '__main__':
    app.run(debug = True)