from flask import Flask, render_template, jsonify, redirect, request
import inverted_index   

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    
    return render_template("index.html") 

@app.route('/get-user-data', methods=['POST'])
def show_stuff():
    #setup elastic search
    #setup schema for ES
    #push data onto the ES
    #get search query
    #process search query 
    #pass to front end
    #pass tags,timeframes, freq of terms
    return render_template("index.html") 


if __name__ == "__main__":
    app.run()
