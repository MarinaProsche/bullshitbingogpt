from openai import OpenAI

TEXT_ABOUT_LANGUAGE = "\n\n\n give the answer in the same language as the text"


def openai_key():
    with open(".openaikey", "r") as f:
        key = f.read().strip()
        return key

client = OpenAI(api_key=openai_key())
# openai.api_key = openai_key()


def generate_buzzwords_for_theme(theme):
    prompt = (
        "create 24 stereotypical buzzwords, cliches or obstacles (using short phrase, max 2 words) that could meet in a text with this theme: \n\n\n"
        + theme
    )
    buzzwords = chat_with_chatgpt(prompt=prompt, model="gpt-4")
    return buzzwords


def find_general_theme_for_sent_text(themes, text):
    themes_str = "\n".join(themes)
    prompt = (
        f"this is the text \n\n{text}.\n\nWhat kind of theme is it? Give a theme in short phrase, that contains a few details and a genre (text about, fiction, non-fiction, article, resume) \n\n{themes_str}"
    )
    print(prompt)
    general_theme = chat_with_chatgpt(prompt=prompt)
    return general_theme


def find_theme_for_sent_text(under_themes, text):
    under_themes_str = "\n".join(under_themes)
    prompt = f"this is the list of themes:\n\n{under_themes_str}\n\n\nfind the one, that describes the following text the best and print only the theme:\n\n{text}"
    theme_of_text = chat_with_chatgpt(prompt=prompt)
    return theme_of_text


def match_buzzwords(text, buzzwords):
    buzzwords_str = str(buzzwords)
    prompt = f"select from this list: \n\n{buzzwords_str}\n\n all items that could describe this text\n\n{text}"
    return chat_with_chatgpt(prompt=prompt)


def get_result_message(theme, score):
    prompt = (
        f"Generate short (up to 45 words) message that congratulates a player who sent text submissions got {score}"
        + f' out of 24 in "Bullshit Bingo GPT" game that automatically matches the buzzwords for theme "{theme}". Use one emoji in the end.'
    )
    return chat_with_chatgpt(prompt=prompt)

def get_text_about():
    prompt = (f'Please write description (up to 150 words) for the website "Bullshit Bingo GPT" where you can provide an input ' +
        f'text and it automatically generates bullshit bingo card for this text by exposing buzzwords and cliches from the text. ' + 
        f'We are using power of modern AI, you should mention it. Use a lot of bullshit in your answer. Use just three emoji in text. ')
    return chat_with_chatgpt(prompt=prompt)

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo-16k"):
    response = client.chat.completions.create(
        # engine=model,
        model=model,
        messages=[{"role": "user", "content": prompt}],
        # max_tokens=100,
        # n=1,
        # stop=None,
        # top_p = 0.1,
        # temperature=0.1,
    )

    message = response.choices[0].message.content.strip()
    return message
