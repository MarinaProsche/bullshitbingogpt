from chatgpt import generate_buzzwords


def example_texts():
    with open('.exampletext', 'r') as f:
        example_text = f.read().strip()
        example_text_split = example_text.split('-------------------------------------------')
        return example_text_split

def main():
    texts = example_texts()
    for n in texts:
        text_info = generate_buzzwords(n)
        print("BUZZWORDS:\n\n" + text_info[0] + "\n\n" + "SYNOPSYS: \n\n" + text_info[1] + "\n---------------------\n\n")

if __name__ == "__main__":
    main()