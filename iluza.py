# Iluza chatbot
# author Bulat

from ai_module import sayai

print("Welcome to:\nIluza")
print("Iluza: Hello! I am Iluza.")
def main():
    user = input("You: ")
    ai(user)
def say(arg):
    print("Iluza: {}".format(arg))
def ai(arg):
    strai = sayai(arg)
    say(strai)
while  True:
    main()
