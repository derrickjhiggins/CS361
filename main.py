from generate import generate
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# establish openai api client connection
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    # print introduction screen
    with open('startup.txt', 'r') as startup:
        for line in startup.readlines():
            print(line.strip())

    # get first user input
    user_input = input('||  ')
    if user_input == '1':
        # print instructions
        with open('instruction_files/generate_new_icebreaker.txt', 'r') as instructions:
            for line in instructions.readlines():
                print(line.strip())
    elif user_input == '2':
        with open('instruction_files/filepath_instructions.txt', 'r') as instructions:
            print("||   Enter file path here: ")
            filepath = input('||    ')
            for line in instructions.readlines():
                print(line.strip())

    # get second user input
    user_input = input('||  ')
    if user_input == '1':
        print(f"||  Here's a good icebreaker: \n")
        generate(client)

if __name__ == "__main__":
    main()
