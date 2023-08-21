from flask import Flask, render_template, request
import openai

def openai_key():
    with open('.openaikey', 'r') as string:
        key = string.read().strip()
        return key

openai.api_key = openai_key()

app = Flask(__name__, template_folder= 'templates')

@app.route("/", methods=['post', 'get'])
def text():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        text = request.form.get('text')
        prompt = ("find a purpose of this text: \n\n\n"
        + text + "\n\n\n give the answer in the language of the text (example: Russian should result in Russian)")
        message_100 = chat_with_chatgpt(prompt=prompt)
        prompt = ("create a short theme from previous theme, using not more than 20 words, exclude all specific terms: \n\n\n"
        + message_100 + "\n\n\n give the answer in the language of the theme (example: Russian should result in Russian)")
        # theme ready for making a buzzwords:
        message_20 = chat_with_chatgpt(prompt=prompt)

        prompt = ("write down funny buzzwords, that could be used for bullshit bingo for this theme: \n\n\n"
        + message_20 + "\n\n\n give the answer in the language of the theme (example: Russian should result in Russian)")
        buzzwords = chat_with_chatgpt(prompt=prompt)

        return render_template('bingo.html', text=buzzwords, message_100=message_100, message_20 = message_20)

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        # engine=model,
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        # max_tokens=100,
        # n=1,
        # stop=None,
        # temperature=0.5,
    )

    message = response.choices[0].message.content.strip()
    return message