# Iluza chatbot
# author Bulat

import ai_module

answer = ""
print("Welcome to:\nIluza")
def say(var):
    name = "Iluza"
    if var == "":
        hello = "Hello! I am Iluza."
        print("{}: {}".format(name, hello))
    else:
        print("{}: {}".format(name, var))
    request()
def request():
    user = input("You: ")
    ai(user)
def ai(var):
    strai = ai_module.sayai(var)
    say(strai)
while  True:
    say(answer)
