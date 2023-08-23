from flask import Flask, render_template, request
import openai

from chatgpt import generate_buzzwords

app = Flask(__name__, template_folder= 'templates')

@app.route("/", methods=['post', 'get'])
def text():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        text = request.form.get('input_text')
        buzzwords, message_30 = generate_buzzwords(text)
        return render_template('bingo.html', buzzwords=buzzwords, message_30=message_30)

