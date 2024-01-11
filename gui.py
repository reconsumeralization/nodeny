import asyncio
from tkinter import Tk, Entry, Button, Text, Scrollbar, END
from api_handler import APIHandler

class GUI:

    def __init__(self):
        self.api_handler = APIHandler(self)
        self.root = Tk()
        self.root.title("Generative Language API GUI")
        self.query_entry = Entry(self.root, width=50)
        self.submit_button = Button(self.root, text="Submit", command=self.handle_user_input)
        self.response_text = Text(self.root, width=50, height=10)
        self.scrollbar = Scrollbar(self.root, command=self.response_text.yview)
        self.response_text['yscrollcommand'] = self.scrollbar.set

    def run(self):
        self.query_entry.pack()
        self.submit_button.pack()
        self.response_text.pack(side="left", fill="y")
        self.scrollbar.pack(side="right", fill="y")
        self.root.mainloop()

    def handle_user_input(self):
        query = self.query_entry.get()
        asyncio.run(self.api_handler.make_async_request(query))

    def display_responses(self, responses):
        self.response_text.delete(1.0, END)
        for response in responses:
            self.response_text.insert(END, response + "\n")