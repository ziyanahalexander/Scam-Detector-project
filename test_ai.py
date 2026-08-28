import requests

from api_key import API_KEY

response = requests.post(
    "https://router.huggingface.co/v1/chat/completions",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "model": "meta-llama/Llama-3.1-8B-Instruct:novita",
        "messages": [
            {"role": "user", "content": "Say hello in one short sentence."}
        ]
    }
)

print(response.status_code)
print(response.json())
