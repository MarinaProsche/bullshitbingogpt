from flask import Flask, render_template, request

app = Flask(__name__, template_folder= 'templates')

@app.route("/", methods=['post', 'get'])
def text():
    if request.method == "GET":
        text = request.form.get('text')
        return render_template('text.html', text=text)
    if request.method == "POST":
        text = 'дождитесь генерации'
        return render_template('after_text.html', text=text)

# @app.route('/text/', methods=['post', 'get'])
# def false():
#     message = ''
#     if request.method == 'POST':
#         text = request.form.get('text')
#     if text:
#         message = 'Please wait'
#     return render_template('text.html', message=message)