from flask import Flask, render_template, request
import openai
from chatgpt import generate_buzzwords, find_theme_for_sent_text, match_buzzwords
from generator_for_themes import get_theme_list, get_buzzwords_for_theme

from dataclasses import dataclass

@dataclass
class BuzzwordsMatch:
    # class for keeping buzzword match for input text
    buzzword: str
    match: bool

app = Flask(__name__, template_folder= 'templates')

@app.route("/", methods=['post', 'get'])
def text():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        text = request.form.get('input_text')
        themes = get_theme_list()
        theme_of_sent_text = find_theme_for_sent_text(text=text, themes=themes)
        print(theme_of_sent_text, themes)
        if theme_of_sent_text in themes:
            list_final_buzzwords = get_buzzwords_for_theme(theme_of_sent_text)
            buzzword_match = match_buzzwords(text=text, buzzwords=str(list_final_buzzwords))
            buzz_m_list = [BuzzwordsMatch(buzzword=buzzword, match=buzzword in buzzword_match) for buzzword in list_final_buzzwords]
            buzz_m_list = buzz_m_list[:12] + [BuzzwordsMatch(buzzword='', match=True)] + buzz_m_list[12:]   
            return render_template('bingo.html', buzz_m_list=buzz_m_list, theme_of_sent_text=theme_of_sent_text)
        else:
            return render_template('theme_not_found.html', theme_of_sent_text=theme_of_sent_text)

