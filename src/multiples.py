import openai
import requests
import requests
import shutil
import json

from dotenv import dotenv_values
from datetime import datetime

CONFIG = dotenv_values('.env')

openai.api_key = CONFIG["KEY"]
openai.organization = CONFIG["ORG"]

def download(data: dict = {}) -> None:
    for img in data:
        print(img)
        print(f'Downloading from {img["url"]}...')
        response = requests.get(img["url"], stream = True)
        if response.status_code == 200:
            with open(f"img/{datetime.now().timestamp()}.png", "wb") as fh:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, fh)

def generate_prompt(**kwargs) -> str:
    response = openai.Image.create(
        prompt = kwargs["prompt"],
        n = 2,
        size = "1024x1024",
        response_format="url"
    )
    return response['data']

def main():
    prompt = input("Prompt: ")
    try:
        result = generate_prompt(prompt = prompt)
        download(data = result)
    except:
        print("[ERROR] Something went wrong...")

if __name__ == "__main__":
    main()
