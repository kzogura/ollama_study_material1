import requests
import json

# これでは取得できなかった
# Ollama APIエンドポイント
# url = "http://192.168.0.102:11434/api/show"
# payload = {"name": "llama3:70b"}

# response = requests.post(url, json=payload)
# if response.ok:
#     data = response.json()
#     print("Model size (bytes):", data.get("size"))
# else:
#     print("Error:", response.text)

# print("-------------------------------")

# リクエストデータ
url = "http://192.168.0.102:11434/api/generate"
payload = {
    "model": "llama3",  # 使用するモデル名
    "prompt": "こんにちは、Ollama！"
}

# APIリクエスト
try:
    response = requests.post(url, json=payload, timeout=300)
    response.raise_for_status()
    last_data = None
    full_response = ""  # ここで全トークンを連結
    for line in response.text.strip().split('\n'):
        data = json.loads(line)
        full_response += data.get("response", "")
        last_data = data  # 最後のJSONを保存
    print(full_response)  # まとめて出力
    # 最後のJSONからtoken/sを計算
    if last_data and "eval_count" in last_data and "eval_duration" in last_data:
        token_per_sec = last_data["eval_count"] / (last_data["eval_duration"] / 1e9)
        print(f"token/s: {token_per_sec:.2f}")
except requests.exceptions.RequestException as e:
    print("Request failed:", e)

