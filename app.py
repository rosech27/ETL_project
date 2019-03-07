from flask import Flask, render_template
from flask_pymongo import PyMongo
# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
#import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# # Create connection variable
# conn = 'mongodb://localhost:27017'

# # Pass connection to the pymongo instance.
# client = pymongo.MongoClient(conn)

# # Connect to a database. Will create one if not already available.
# db = client.demoelection
# collection = db.combData
app.config["MONGO_URI"] = "mongodb://localhost:27017/demoelection"
mongo = PyMongo(app)

# Set route
@app.route('/')
def index():

    #data = collection.find_one()
    data = mongo.db.combData.find_one()
    # Return the template with the data passed in
    return render_template('index.html', data=data)

# @app.route('/tech')
# def tech():
#     return render_template('techstack.html')


# @app.route('/report')
# def report():
#     return render_template('reports.html')


if __name__ == "__main__":
    app.run(debug=True)