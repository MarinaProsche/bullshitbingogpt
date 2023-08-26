from concurrent.futures import ThreadPoolExecutor
from chatgpt import generate_buzzwords, generate_buzzwords_for_theme
import re
import json
import os


def example_theme():
    with open('themes.txt', 'r') as f:
        themes = [x.strip() for x in f.readlines() if x.strip()]
        return themes

def parsing_only_buzzwords(text):
    res =[]
    lines = text.split('\n')
    for line in lines:
        m = re.search(r'^\d+\. (.+)$', line)
        if m:
            res.append(m.group(1).replace('"', '').strip())
    return res

def theme_to_file(theme):
    theme_buzzwords = generate_buzzwords_for_theme(theme)
    buzzwords_list = parsing_only_buzzwords(theme_buzzwords)
    with open (f'buzzwords/{theme}', "w") as f:
        json.dump(buzzwords_list, f, indent=4) #make 4 spaces

def get_theme_list():
    theme_list = os.listdir('buzzwords')
    return theme_list

def get_buzzwords_for_theme(theme):
    with open (f'buzzwords/{theme}', "r") as f:
        return json.load(f)

def main():
    futures = []
    themes = example_theme()
    with ThreadPoolExecutor(max_workers=128) as executor:
        for theme in themes:
            future = executor.submit(theme_to_file, theme)
            futures.append(future)
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()