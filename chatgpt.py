
import openai

TEXT_ABOUT_LANGUAGE = "\n\n\n give the answer in the same language as the text"

def openai_key():
    with open('.openaikey', 'r') as f:
        key = f.read().strip()
        return key

openai.api_key = openai_key()
                

def generate_buzzwords(text):
    prompt = ("find a purpose and genre and synopsys in 30 words of this text: \n\n\n"
        + text + TEXT_ABOUT_LANGUAGE)
    message_30 = chat_with_chatgpt(prompt=prompt)
    prompt = ("create short stereotypic buzzwords, that could be used for bullshit bingo for this theme: \n\n\n"
    + message_30 + TEXT_ABOUT_LANGUAGE)
    buzzwords = chat_with_chatgpt(prompt=prompt)
    return (buzzwords, message_30)

def generate_buzzwords_for_theme(theme):
    prompt = ("create 25 short stereotypic cliches (pair of words), that could be used for bullshit bingo for this theme: \n\n\n"
    + theme)
    buzzwords = chat_with_chatgpt(prompt=prompt)
    return buzzwords


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