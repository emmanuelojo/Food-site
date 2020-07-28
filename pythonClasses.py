import random

responses = ["Nice question", "Wow, amazing", "Fantabulous", "Next question", "Maybe next time", "Thats interesting", "Try again"
            "I expected a better question", "Niver give up", "I dont have to prove im a genuis"]


def login():
    user_login = input(""""Welcome to Jekon game. Nice having you here.
    You can login to play or exit at the game at your own time. Enter
        1 ==> To login
        2 ==> To exit : """)
    if user_login == "1":
        username = input("Welcome again. Enter your preferred name: ")
        print("Hello ", username)
    elif user_login == "2":
        print("Thanks for checking out. See you another time")
    else:
        print("Invalid command")
        login()
login()

def magic_ball():
    user_question = input("Please enter your question: ")
    answer = random.choice(responses)
    print("Thinking ................................................")
    print("_"*100)
    print("Thanks for waiting, your answer is: ", answer)
    next_question = input("Do you want to ask another question? Enter Yes or No: ")
    if next_question == "Yes" or "yes":
        magic_ball()
    elif next_question == "No" or "no":
        login()
    else:
        print("Invalid command")
        login()
magic_ball()


