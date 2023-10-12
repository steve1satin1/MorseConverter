import tkinter
from tkinter import messagebox

morse_data = {
    "a": ".- ",
    "b": "-... ",
    "g": "--. ",
    "d": "-.. ",
    "e": ". ",
    "z": "--.. ",
    "h": ".... ",
    "c": "-.-. ",
    "i": ".. ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": ".. ",
    "n": "-. ",
    "x": "-..- ",
    "o": "--- ",
    "p": ".--. ",
    "r": ".-. ",
    "s": "... ",
    "t": "- ",
    "y": "-.-- ",
    "f": "..-. ",
    "q": "--.- ",
    "w": ".-- ",
    "v": "...- ",
    "j": ".--- ",
    "u": "..- ",
    "1": "·−−−− ",
    "2": "··−−− ",
    "3": "···−− ",
    "4": "····−	",
    "5": "·····	",
    "6": "−····	",
    "7": "−−···	",
    "8": "−−−··	",
    "9": "−−−−·	",
    "0": "−−−−−	",
    ";": "..--.. ",
    ".": ".-.-.- ",
    ",": "--..-- ",
    ":": "---... ",
    "(": "-.--. ",
    ")": "-.--.- ",
    "/": "-..-. ",
    "\"": ".-..-. ",
    " ": " / "
}


def _translate(text: str):
    text = text.lower().strip()
    try:
        alist = [morse_data[char] for char in text if char != "\n"]
    except KeyError:
        messagebox.showwarning("Invalid text", message="An error occured, maybe you provided a character that can not "
                                                       "be translated to morse code")
    else:
        return "".join(alist)
    return


class MorseWidget(tkinter.Text):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(state="disabled")

    def translate(self, text):
        # enable widget
        self.config(state="normal")

        # delete previous text
        self.delete("1.0", "end")

        # translate
        result_text = _translate(text)

        # show translatted text
        self.insert("1.0", result_text)

        self.config(state="disabled")

