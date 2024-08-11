import requests
from dotenv import load_dotenv
import base64
import os

# loading in required keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_KEY")


def query_openai_chat(message: str, model: str = 'gpt-4o-mini', temperature: float = 0.7):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": message}],
        "temperature": temperature
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        response.raise_for_status()




def query_openai_image(message: str, image_path: str, model: str = 'gpt-4o-mini'):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
    }
    payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": message
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    if response.status_code == 200:
        response_data = response.json()
        return response_data['choices'][0]['message']['content']
    else:
        response.raise_for_status()


if __name__=='__main__':
    q = query_openai_image('please tell me what image I am looking at right now', 'testimg.png')
    print(q)
