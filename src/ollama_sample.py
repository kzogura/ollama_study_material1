import requests
import json

# Ollama APIエンドポイント
url = "http://192.168.0.102:11434/api/generate"

# リクエストデータ
payload = {
    "model": "llama3",  # 使用するモデル名
    "prompt": "こんにちは、Ollama！"
}

# APIリクエスト
try:
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()
    # 1行ずつJSONとして処理
    for line in response.text.strip().split('\n'):
        data = json.loads(line)
        print(data.get("response", data))
except requests.exceptions.RequestException as e:
    print("Request failed:", e)

