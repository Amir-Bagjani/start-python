import json
from functools import lru_cache

import requests


@lru_cache(maxsize=128)
def ask_ai(prompt: str):
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
