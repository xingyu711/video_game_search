from flask import Flask, render_template, request
import searchGame

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/search', methods = ['GET', 'POST'])
def search_game():
    if request.method == 'POST':
        query = request.form['query']
        records = searchGame.search_game(query)
        return render_template('results.html', records = records, query = query)