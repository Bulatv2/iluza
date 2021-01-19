# Iluza AI
# author Bulat

import ai_module

print("Welcome to:\nIluza")
words = ""
hello = "Hello, I am Iluza."
def sayai(words):
    name = "Iluza"
    if words == "":
        print("{}: {}".format(name, hello))
    else:
        print("{}: {}".format(name, words))
    request()
def request():
    user = input("You: ")
    ai(user)
def ai(file):
    words = ai_module.say(file)
    sayai(words)
sayai(words)
