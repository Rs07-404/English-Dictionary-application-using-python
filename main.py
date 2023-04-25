# RS7
# English Dictionary using python
from tkinter import *
from tkinter.ttk import *
import requests

FONT = ("Segoe UI", 8, "bold")
URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


# Logic
def find():
    word = (input_word.get()).title()
    response = requests.get(url=URL+word)
    data = response.json()[0]
    phonetic_text = ""
    meanings = ""
    for i in range(0, len(data["meanings"])):
        meanings += f'''\n◙ PartOfSpeech: {data["meanings"][i]["partOfSpeech"]}\n'''
        for j in range(0, len(data["meanings"][i]["definitions"])):
            definition_dict = data["meanings"][i]["definitions"][j]
            meanings += f'''    definition {j+1}: {definition_dict["definition"]}\n'''

    for i in range(0, len(data["phonetics"])):
        phonetic_dict = data["phonetics"][i]
        try:
            phonetic_text = phonetic_dict["text"]
            break
        except:
            pass

    meaning = f'''word: {data["word"]}\nphonetic: {phonetic_text}\n\ndefinitions: {meanings}'''
    meaning_text.delete("1.0", END)
    meaning_text.insert("1.0", meaning)


# Window
window = Tk()
window.title("English Dictionary")
window.minsize(width=800, height=500)
window.attributes("-alpha", 0.9)

# heading
label_0 = Label(text="English Dictionary", font=("Segoe UI", 20, "bold"))
label_1 = Label(text="Enter a word to search for", font=("Segoe UI", 10, "bold"))
label_2 = Label(text="Meaning: ", font=("Segoe UI", 15, "bold"))
meaning_text = Text(width=111, height=12, font=("Segoe UI", 10, "normal"))
# input_box
input_word = Entry(width=30)

# search_button
search_button = Button(text="Search", command=find)

# layout
label_0.place(x=270, y=0)
label_1.place(x=305, y=50)
input_word.place(x=295, y=70)
search_button.place(x=350, y=110)
label_2.place(x=2, y=150)
meaning_text.place(x=10, y=190)
window.mainloop()
