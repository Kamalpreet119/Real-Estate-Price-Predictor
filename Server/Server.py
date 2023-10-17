from flask import Flask,request,jsonify
import Util
#Flask is a model that allows us to write a Python Service to handle HTTP requests
app=Flask(__name__)

@app.route("/Hello")#Way of Exposing HTTP Endpoint
def Hello():#A simple Hello routine
    return "Hello"
"""To run the server- Open Command Prompt and write'python Server.py'
Then use the URL provided on the Command Prompt on the Browser
To see Hello Routine- <URL Obtained>/Hello"""

@app.route("/get_location_names")
def get_location_names():#Routine to get Location's names
    response=jsonify({
        "locations":Util.get_location_names()
        #util-A new file to contain all the core routines
        #server.py-Just for routing of requests and response
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    #Returning a response containing all the locations
    return response

@app.route("/predict_house/price",methods=["GET","POST"])
def predict_house_price():#Another endpoint
    #For HTTP call from our HTML Application-We will get all the inputs in request.form
    total_sqft=float(request.form["total_sqft"])
    location=request.form["location"]
    bhk=int(request.form["bhk"])
    bath=int(request.form["bath"])

    response=jsonify({
        "estimated_price":Util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

if __name__=="__main__":
    print("Starting Python Flask Server for House Price Prediction-")
    app.run()#Run application on a specific port
