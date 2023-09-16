from flask import Flask, render_template, request
import openai
from chatgpt import (
    find_theme_for_sent_text,
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


@app.route("/", methods=["get"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def text_about():
    text_about = get_text_about()
    return render_template("about.html", text_about=text_about)


@app.route("/extract_theme", methods=["post", "get"])
def extract_theme():
    if request.method == "GET":
        return render_template("extract_theme.html")
    if request.method == "POST":
        text = request.form.get("input_text")
        themes = get_theme_architecture()
        general_theme = find_general_theme_for_sent_text(themes=list(themes), text=text)
        for theme in themes:
            if theme.lower() in general_theme.lower():
                list_of_under_themes = themes[theme]
                theme_of_sent_text = find_theme_for_sent_text(
                    text=text, under_themes=list_of_under_themes
                )
                return render_template(
                    "extract_theme.html", chat_response=theme_of_sent_text
                )
        else:
            return render_template("extract_theme.html", chat_response=general_theme)
        


@app.route("/bingo", methods=["post", "get"])
def bingo():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        theme = request.form.get("input_theme")
        list_final_buzzwords = parsing_only_buzzwords(generate_buzzwords_for_theme(theme))
        # buzzword_match = match_buzzwords(
        #     text=text, buzzwords=list_final_buzzwords
        # )
        buzz_m_list = [
            BuzzwordsMatch(
                buzzword=buzzword,
                match=False
                # buzzword.lower() in buzzword_match.lower(),
            )
            for buzzword in list_final_buzzwords
        ]
        buzz_m_list = (
            buzz_m_list[:12]
            + [BuzzwordsMatch(buzzword="", match=False)]
            + buzz_m_list[12:]
        )
        # result_message = get_result_message(
        #     theme=theme,
            # score=len([x for x in buzz_m_list if x.match]) - 1,
        # )
        return render_template(
            "bingo.html", buzz_m_list=buzz_m_list, result_message=''
        )
