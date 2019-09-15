from flask import Flask, render_template, jsonify, redirect, request
from inverted_index import InvertedIndex

app = Flask(__name__)
inverted_index = InvertedIndex()

@app.route("/Search", methods=['GET','POST'])
def index():
    search = str(request.args['search'])
    query = inverted_index.search(search)
    links = []
    frames = []
    #print(inverted_index.inverted_index['human'])
    print(query)
    total_frames  = []
    video_titles= []
    video_thumbnails = []
    video_links = []
    for item in query:
        pervideoframe = []
        video_titles.append(query[item]['title'])
        video_thumbnails.append(query[item]['thumbnail_link'])
        video_links.append(query[item]['youtube_link'][:-1])

        for frames in query[item]['frames']:
            pervideoframe.append(frames['frame_no'])
        total_frames.append(pervideoframe)
    return render_template("list.html",video_links=video_links,total_frames=total_frames,video_titles=video_titles,video_thumbnails=video_thumbnails,pervideoframe=pervideoframe)

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
    link= str(request.args['video'])

    return render_template("play.html",link=link)



if __name__ == "__main__":
    app.run(debug=True,port = 8080)
