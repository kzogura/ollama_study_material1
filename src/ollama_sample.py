import requests
import json

# Ollama APIエンドポイント
url = "http://192.168.0.102:11434/api/generate"

# リクエストデータ
payload = {
    "model": "llama3:70b",  # 使用するモデル名
    "prompt": "こんにちは、Ollama！"
}

# APIリクエスト
try:
    response = requests.post(url, json=payload, timeout=300)
    response.raise_for_status()
    last_data = None
    for line in response.text.strip().split('\n'):
        data = json.loads(line)
        print(data.get("response", data))
        last_data = data  # 最後のJSONを保存
    # 最後のJSONからtoken/sを計算
    if last_data and "eval_count" in last_data and "eval_duration" in last_data:
        token_per_sec = last_data["eval_count"] / (last_data["eval_duration"] / 1e9)
        print(f"token/s: {token_per_sec:.2f}")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)

