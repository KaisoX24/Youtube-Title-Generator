import time
from groq import Groq
import os
import tkinter as tk
from tkinter import filedialog

# Load API key from .env
Api_key = os.getenv('GROQ_API_KEY')

client = Groq(api_key=Api_key)

# Function for getting the response from the API
def chat(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": 'user', "content": template.format(user_input=user_input)}],
            model="llama-3.1-8b-instant",
            max_tokens=800,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print('Api Error: ', e)
        return None

# Function to stream the text response
def streamtext(response):
    for i in response:
        print(i, end='', flush=True)
        time.sleep(0.02)

# Prompt template for generating video titles
template = '''
Generate 5 catchy, attractive YouTube video titles
for the topic: {user_input}. Titles should be optimized for maximum clicks.
'''

# Function to get the file save path from the user
def get_save_path():
    root = tk.Tk()
    root.withdraw()
    root.lift() 
    root.attributes("-topmost", True)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    root.attributes("-topmost", False)
    return file_path

# Main loop
while True:
    user_input = input("Enter a topic for YouTube video titles: ")
    if user_input.lower() == "exit":
        print('Bye!')
        break
    try:
        response = chat(user_input)
        print('🤖: ', end='')
        streamtext(response)
        while True:
            ask = input("\n\nDo you want to save the titles in a text file (y/n): ")
            if ask.lower() == 'y':
                save_path = get_save_path() 
                if save_path: 
                    with open(save_path, 'a') as f:
                        f.write(f"Topic: {user_input}\n{response}\n\n")
                    print(f'Titles saved in {save_path}')
                else:
                    print("Save operation canceled.")
                break
            elif ask.lower() == 'n':
                break
            else:
                print('Invalid input. Please enter y or n.')
    except Exception as e:
        print('Error: ', e)
    
        