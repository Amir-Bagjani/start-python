import json
import requests


def chat(prompt: str):
    try:
        res = requests.post(
            url="http://localhost:11434/api/chat",
            headers={"Content-Type": "application/json"},
            data=json.dumps(
                {
                    "model": "minimax-m3:cloud",
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                }
            ),
        )
        if res.status_code == 200:
            return res.json()["message"]["content"]
    except Exception as e:
        return e
