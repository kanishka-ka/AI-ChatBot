from tkinter import *
import nltk

# Download required NLTK data
nltk.download('punkt')

def send_message():
    user_message = entry_box.get().lower()

    greetings = ["hello", "hi", "hey"]
    asking = ["how are you"]
    goodbye = ["bye", "goodbye"]

    if user_message in greetings:
        bot_reply = "Hello! How can I help you?"

    elif user_message in asking:
        bot_reply = "I am doing great!"

    elif user_message in goodbye:
        bot_reply = "Goodbye!"

    elif user_message == "what is your name":
        bot_reply = "My name is AI Bot."

    elif user_message == "who made you":
        bot_reply = "Kanishka created me."

    elif user_message == "what can you do":
        bot_reply = "I can chat with you."

    else:
        bot_reply = "Sorry, I don't understand."

    chat_box.insert(END, "You: " + user_message + "\n")
    chat_box.insert(END, "Bot: " + bot_reply + "\n\n")

    entry_box.delete(0, END)

# Main Window
root = Tk()
root.title("AI ChatBot")
root.geometry("500x500")
root.config(bg="lightblue")

# Heading
heading = Label(
    root,
    text="AI ChatBot",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
heading.pack(pady=10)

# Chat Area
chat_box = Text(root, height=20, width=50)
chat_box.pack(pady=10)

# Scrollbar
scrollbar = Scrollbar(root, command=chat_box.yview)
chat_box.config(yscrollcommand=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)

# Input Box
entry_box = Entry(root, width=40, font=("Arial", 12))
entry_box.pack(pady=10)

# Send Button
send_button = Button(
    root,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=send_message
)
send_button.pack()

# Enter key sends message
root.bind('<Return>', lambda event: send_message())

root.mainloop()