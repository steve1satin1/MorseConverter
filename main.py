import tkinter
from MorseWidget import MorseWidget

window = tkinter.Tk()

# input widget
input = tkinter.Text(window)
input.grid(row=0, column=0)
slider1 = tkinter.Scrollbar(window, orient="vertical", command=input.yview)
slider1.grid(column=1, row=0, sticky="ns")
input['yscrollcommand'] = slider1.set

# result widget
morse_text = MorseWidget(window)
morse_text.grid(row=1, column=0)
slider2 = tkinter.Scrollbar(window, orient="vertical", command=morse_text.yview)
slider2.grid(column=1, row=1, sticky="ns")
morse_text['yscrollcommand'] = slider2.set

translate_btn = tkinter.Button(window, text="Translate",
                               command=lambda: morse_text.translate(input.get(1.0, tkinter.END)))
translate_btn.grid(row=2, column=0)
window.mainloop()
