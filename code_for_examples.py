from chatgpt import generate_buzzwords, find_theme_for_sent_text, match_buzzwords
from generator_for_themes import get_theme_list, get_buzzwords_for_theme


def example_texts():
    with open('.exampletext', 'r') as f:
        example_text = f.read().strip()
        example_text_split = example_text.split('-------------------------------------------')
        return example_text_split

def main():
    texts = example_texts()
    themes = get_theme_list()
    for text in texts:
        theme_of_sent_text = find_theme_for_sent_text(text=text, themes=themes)
        if theme_of_sent_text in themes:
            list_final_buzzwords = get_buzzwords_for_theme(theme_of_sent_text)
            buzzword_match = match_buzzwords(text=text, buzzwords=str(list_final_buzzwords))
            for buzzword in list_final_buzzwords:
                if buzzword in buzzword_match:
                    print (f"X {buzzword}")    
                else:
                    print (f"  {buzzword}") 
            print("THEMES:\n\n" + theme_of_sent_text + "\n\n" + buzzword_match + "\n---------------------\n\n")
        else:
            print(f"sorry, this text with theme {theme_of_sent_text} doesn't match any theme from list \n---------------------\n\n")


if __name__ == "__main__":
    main()