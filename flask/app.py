from flask import Flask, render_template, jsonify, redirect, request
from inverted_index import InvertedIndex

app = Flask(__name__)
inverted_index = InvertedIndex()

@app.route("/Search", methods=['GET','POST'])
def index():
    search = str(request.args['search'])
    print(search)
    query = inverted_index.search(search)
    print(query)
    return render_template("index.html")

@app.route('/')
def show_stuff():
    #setup elastic search
    #setup schema for ES
    #push data onto the ES
    #get search query
    #process search query
    #pass to front end
    #pass tags,timeframes, freq of terms
    return render_template("index.html")

@app.route('/play')
def show_stuff2():
    return render_template("play.html")



if __name__ == "__main__":
    app.run(debug=True,port = 8080)
