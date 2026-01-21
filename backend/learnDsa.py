from flask import Flask, render_template

app = Flask(__name__)

#home page 
@app.route("/")
def home():
    return render_template("home.html")

#Stack 
@app.route("/stack")
def stack():
    return render_template("stack.html")

#List 
@app.route("/list")
def list():
    return render_template("list.html")

#Queue
@app.route("/queue")
def queue():
    return render_template("queue.html")

#Map 
@app.route("/map")
def map():  
    return render_template("map.html")

#Deque
@app.route("/deque")
def deque():
    return render_template("deque.html")

#Graph
@app.route("/graph")
def graph():
    return render_template("graph.html")

#Tree
@app.route("/tree")
def tree():
    return render_template("tree.html")

if __name__ == "__main__":
    app.run(debug=True)