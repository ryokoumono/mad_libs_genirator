import os
import random
import re

def generator(text:str) -> str:
    '''find needed words in text and ask user enter them, then return result'''
    parts_of_speech: list = re.findall('_+\s?\([^\)]+\)', text)
    words: dict = {}
    for part in parts_of_speech:
        text_to_user = part.replace('_', '').replace('(', '').replace(')', '').replace('\n', ' ')
        words[part] = input(f'Please input a(n) {text_to_user}\n')
        os.system('cls' if os.name == 'nt' else 'clear')
    
    for regex, replacable_world in words.items():
        regex = regex.replace(')', '\)').replace('(', '\(')
        text = re.sub(regex, replacable_world, text, 1)
    return text
    
def get_template(witch: str = None) -> str:
    '''just get a template from text file'''  
    if witch:
        return open(f'./templates/{witch}.txt', 'r').read()
    template: str = random.choice(os.listdir('./templates'))
    return open(f'./templates/{template}', 'r').read() 

def main() -> None:
    text = generator(get_template())
    print(text)

if __name__ == '__main__':
    main()