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
        prompt = "extract a main theme from text, using not more than 100 words and only generic terms: " + text
        message = chat_with_chatgpt(prompt=prompt)
        return render_template('bingo.html', text=message)

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