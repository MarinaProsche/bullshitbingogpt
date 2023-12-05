import json

from flask import Flask, render_template, request
import openai
from chatgpt import (
    # find_theme_for_sent_text,
    find_general_theme_for_sent_text,
    match_buzzwords,
    get_result_message,
    get_text_about,
    generate_buzzwords_for_theme,
)
from generator_for_themes import get_theme_architecture, parsing_only_buzzwords

from dataclasses import dataclass


@dataclass
class BuzzwordsMatch:
    # class for keeping buzzword match for input text
    buzzword: str
    match: bool


app = Flask(__name__, template_folder="templates")
app.static_folder = 'static'

@app.route("/", methods=["get"])
def index():
    gif_file = "robot.gif"
    bingo = 'bingo.gif'
    return render_template("index.html", gif_file=gif_file, bingo=bingo)

@app.route("/about", methods=["POST", "GET"])
def text_about():
    bullshit = 'bullshit.gif'
    code_file = "code.png"
    if request.method == "GET":
        return render_template("about.html", code_file=code_file, bullshit=bullshit)
    if request.method == "POST":
        text_about = get_text_about()
        return render_template("about.html", text_about=text_about, code_file=code_file, bullshit=bullshit)


@app.route("/extract_theme", methods=["post", "get"])
def extract_theme():
    bullshit = 'bullshit.gif'
    gif_file = "robot.gif"
    if request.method == "GET":
        return render_template("extract_theme.html", gif_file=gif_file, show_form = True)
    if request.method == "POST":
        text = request.form.get("input_text")
        themes = get_theme_architecture()
        general_theme = find_general_theme_for_sent_text(themes=list(themes), text=text)
        
        # In case of solid themes:
        # for theme in themes:
        #     if theme.lower() in general_theme.lower():
        #         list_of_under_themes = themes[theme]
        #         theme_of_sent_text = find_theme_for_sent_text(
        #             text=text, under_themes=list_of_under_themes
        #         )
        #         return render_template(
        #             "extract_theme.html", chat_response=theme_of_sent_text
        #         )
        # else:
        
        return render_template("extract_theme.html", chat_response=general_theme, bullshit=bullshit, gif_file=gif_file, show_form = False)
        


@app.route("/bingo", methods=["post", "get"])
def bingo():
    theme_for_message = ''
    wow = 'wow.gif'
    hand = 'hand.gif'
    bingo = 'bingo.gif'
    gif_file = "robot.gif"
    if request.method == "GET":
        return render_template("index.html", bingo=bingo, gif_file=gif_file)
    if request.method == "POST":
        theme = request.form.get("input_theme")
        user_text = request.form.get("input_user_text")
        if theme is not None:
            list_final_buzzwords = parsing_only_buzzwords(generate_buzzwords_for_theme(theme))
            buzzword_serial = json.dumps(list_final_buzzwords) #string of buzzwords
            buzzword_match = ''
            remember_theme = json.dumps(theme) #remember theme for use it in the message text
        else:
            remember_theme = request.form.get('remember_theme')
            theme_for_message = json.loads(remember_theme)
            buzzword_serial = request.form.get('buzzword_serial') # we came from 'bingo.html' if not theme
            list_final_buzzwords = json.loads(buzzword_serial)
            buzzword_match = match_buzzwords(
                text=user_text, buzzwords=list_final_buzzwords
            )

        buzz_m_list = [
            BuzzwordsMatch(
                buzzword=buzzword,
                match=buzzword.lower() in buzzword_match.lower(),
            )
            for buzzword in list_final_buzzwords
        ]
        buzz_m_list = (
            buzz_m_list[:12]
            + [BuzzwordsMatch(buzzword="", match=False)]
            + buzz_m_list[12:]
        )
        if buzzword_match:
            result_message = get_result_message(
                theme=theme_for_message,
                score=len([x for x in buzz_m_list if x.match]),
            ) + f'\n\nTry another one text with "{theme_for_message.strip()}" or '
        else:
            result_message = (f'GREAT! We have the most common cliches for theme "{theme.strip()}"\n'
            + f'Now you can insert your text (up to 240000 symbols), and see, if you win the bingo! 🚀🚀')

        return render_template(
            "bingo.html", buzz_m_list=buzz_m_list, buzzword_serial=buzzword_serial,
            result_message=result_message, remember_theme=remember_theme, theme=theme, wow=wow, hand=hand
        )
