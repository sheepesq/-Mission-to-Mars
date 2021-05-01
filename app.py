#10.5.1
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#First, let's define the route for the HTML page. 
#In our script, type the following:
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#Our next function will set up our scraping route
#This route will be the "button" of the web application, 
#the one that will scrape updated data when we tell it to from the homepage of our web app
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()  ########HERE############
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


if __name__ == "__main__":
   app.run()
