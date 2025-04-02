from webscout import PhindSearch

def Main_Brain(text):
    ai = PhindSearch(
        quiet=True,
        intro="you are Jarvis ai assistant"
    )
    res = ai.ask(text)
    return res['choices'][0]['delta']['content']

if __name__ == "__main__":
    print("Brain script started.")
    while True:
        x = input("Enter your query: ")
        if x.lower() == "exit":
            break
        print(Main_Brain(x))
