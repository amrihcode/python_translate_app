from tkinter import *
from tkinter import ttk, messagebox
# pip install googletrans
import googletrans
import requests

root = Tk()
root.title("TRANSL")
root.geometry("1080x500")

Lang = googletrans.LANGUAGES
LangV = list(Lang.values())
Lang1 = list(Lang.keys())
LangV_to_Lang1 = {v: k for k , v in Lang.items()}

combo1 = ttk.Combobox(root, values=LangV , font="Roboto 14" , state="readonly")
combo1.place(x=100 , y=20)
combo1.set("english")  

f = Frame(root , bg="black", bd=5)
f.place(x=10 , y=118 , width=400 , height=210)

text1 = Text(f , font="Roboto 20" , bg="white" , relief=GROOVE , wrap=WORD)
text1.place(x=0 , y=0 , width=390 , height=200)

scbar1 = Scrollbar(f)
scbar1.pack(side="right" , fill="y")
scbar1.config(command=text1.yview)
text1.config(yscrollcommand=scbar1.set)

combo2 = ttk.Combobox(root , values=LangV , font="Roboto 14" , state="readonly")
combo2.place(x=730 , y=20)
combo2.set("persian")

f2 = Frame(root , bg="black", bd=5)
f2.place(x=620 , y=118 , width=400 , height=210)

text2 = Text(f2 , font="Roboto 20" , bg="white" , relief=GROOVE , wrap=WORD)
text2.place(x=0 , y=0 , width=390 , height=200)

scbar2 = Scrollbar(f2)
scbar2.pack(side="right" , fill="y")
scbar2.config(command=text2.yview)
text2.config(yscrollcommand=scbar2.set)

def check_internet_connection():
    try:
        requests.get("https://www.google.com" , timeout=5)
        return True
    except requests.ConnectionError:
        return False

def transltnow():
    if not check_internet_connection():
        messagebox.showerror("Translator" , "No internet connection. Please check your connection and try again.")
        return
    try:
        text_ = text1.get(1.0 , END).strip()
        src_lang = LangV_to_Lang1[combo1.get().lower()]
        dest_lang = LangV_to_Lang1[combo2.get().lower()]
        if text_ and src_lang and dest_lang:
            translator = googletrans.Translator()
            translation = translator.translate(text_ , src=src_lang , dest=dest_lang)
            text2.delete(1.0 , END)
            text2.insert(END , translation.text)
        else:
            messagebox.showwarning("Translator" , "Please select both languages and enter text to translate.")
    except Exception as e:
        messagebox.showerror("Translator" , f"Error: {str(e)}.\nPlease check your internet connection and try again.")

trans_btn = Button(root, text="Translate" , font="Roboto 15 bold italic" , activebackground="yellow" , cursor="hand2", bd=5, bg="blue", fg="white", command=transltnow)
trans_btn.place(x=470 , y=20)

root.configure(bg="white")
root.mainloop()