from flask import Flask, render_template, request
import openai
from chatgpt import (
    find_theme_for_sent_text,
    find_general_theme_for_sent_text,
    match_buzzwords,
    get_result_message,
    get_text_about,
)
from generator_for_themes import get_theme_architecture, get_buzzwords_for_theme

from dataclasses import dataclass


@dataclass
class BuzzwordsMatch:
    # class for keeping buzzword match for input text
    buzzword: str
    match: bool


app = Flask(__name__, template_folder="templates")


@app.route("/", methods=["post", "get"])
def text():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get("input_text")
        themes = get_theme_architecture()
        general_theme = find_general_theme_for_sent_text(themes=list(themes), text=text)
        if general_theme in themes:
            list_of_under_themes = themes[general_theme]
            theme_of_sent_text = find_theme_for_sent_text(
                text=text, under_themes=list_of_under_themes
            )
            if theme_of_sent_text in themes[general_theme]:
                list_final_buzzwords = get_buzzwords_for_theme(theme_of_sent_text)
                buzzword_match = match_buzzwords(
                    text=text, buzzwords=list_final_buzzwords
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
                    + [BuzzwordsMatch(buzzword="", match=True)]
                    + buzz_m_list[12:]
                )
                result_message = get_result_message(
                    theme=theme_of_sent_text,
                    score=len([x for x in buzz_m_list if x.match]),
                )
                return render_template(
                    "bingo.html", buzz_m_list=buzz_m_list, result_message=result_message
                )
            else:
                return render_template("index.html", chat_response=theme_of_sent_text)
        else:
            return render_template("index.html", chat_response=general_theme)


@app.route("/about", methods=["GET"])
def text_about():
    text_about = get_text_about()
    return render_template("about.html", text_about=text_about)
