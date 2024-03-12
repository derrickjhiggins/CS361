import os
import sys
import requests
from dotenv import load_dotenv

from openai import OpenAI
from generate import generate

# Load environment variables from .env file
load_dotenv()

# establish openai api client connection and translation api connection
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
api_url = 'http://localhost:5000/translate'

def getFirstInput():
    # get first user input
    filepath = None
    user_input = input('||  ')
    if user_input == '1':
        with open('instruction_files/generate_new_icebreaker.txt', 'r') as instructions:
            for line in instructions.readlines():
                print(line.strip())
    elif user_input == '2':
        with open('instruction_files/filepath_instructions.txt', 'r') as instructions:
            print("||   Enter file path here: ")
            filepath = input('||    ')
            for line in instructions.readlines():
                print(line.strip())
    elif user_input == '3':
        text_to_translate = input('|| Enter text to be translated here: ')
        target_language = input('|| What is your target language? ')
        translate(text_to_translate, target_language)
        sys.exit()
    elif user_input == '4':
        with open('instruction_files/settings.txt', 'r') as settings:
            for line in settings.readlines():
                print(line.strip())
            sys.exit()
    elif user_input == chr(27):
        print("|| Goodbye for now!")
        sys.exit()

    return filepath

def getSecondInput(filepath):
    # get second user input
    user_input = input('||  ')
    if user_input == '1':
        print(f"||  Here's a good icebreaker: \n")
        generate(client, filepath)
    elif user_input == chr(27):
        print("|| Goodbye for now!")
        sys.exit()
    else:
        additionalDirections = input('|| ')
        generate(client, filepath, additionalDirections)

def translate(text, target_language):
    payload = {
    'text': text,
    'target_language': target_language
    }
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        translated_text = response.json()['translated_text']
        print(f'|| Translated Text: {translated_text}')
    else:
        print(f'|| Error: {response.status_code}, {response.text}')

def main():
    # print introduction screen
    with open('instruction_files/startup.txt', 'r') as startup:
        for line in startup.readlines():
            print(line.strip())

    filepath = getFirstInput()
    getSecondInput(filepath)

if __name__ == "__main__":
    main()
