# -*- coding: utf-8 -*-
"""
    instabot example
    Workflow:
        read and reply your DM
"""
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

def choice(get_choice):
    if get_choice == "y":
        return True
    elif get_choice == "n":
        return False
    else:
        print("Invalid Input")
        return choice(get_choice)

def main():
    chatbot = ChatBot('Ron Obvious')
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    # Train the chatbot based on the english corpus
    trainer.train("chatterbot.corpus.english")

    try:
        input = raw_input
    except NameError:
        pass

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-u", type=str, help="username")
    parser.add_argument("-p", type=str, help="password")
    parser.add_argument("-proxy", type=str, help="proxy")
    args = parser.parse_args()

    bot = Bot()
    bot.login(username=args.u, password=args.p, proxy=args.proxy)

    while 1:
        # Get a response to an input statement
        response = chatbot.get_response("Hello, how are you today?")
        print(response)
        if bot.api.get_inbox_v2():
            data = bot.last_json["inbox"]["threads"]
            for item in data:
                if item['inviter']['username'] != args.u:
                    bot.console_print(item["inviter"]["username"], "lightgreen")
                    user_id = str(item["inviter"]["pk"])
                    last_item = item["last_permanent_item"]
                    item_type = last_item["item_type"]
                    if item_type == "text":
                        print(last_item["text"])
                        text = chatbot.get_response(last_item["text"])
                        bot.send_message(text, user_id, thread_id=item["thread_id"])
                        continue
                    else:
                        print(item_type)

if __name__ == "__main__":
    main()