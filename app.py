import os
import json
from flask import Flask, jsonify, request, send_from_directory
import requests
from dotenv import load_dotenv

# 讀取 .env 檔案中的敏感環境變數
load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    """首頁路由：直接返回 index.html 靜態網頁"""
    return send_from_directory('.', 'index.html')

@app.route('/data.json')
def get_data():
    """API 路由：返回前後端分離的演算法與測驗主資料庫"""
    return send_from_directory('.', 'data.json')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    安全 AI 對話中繼站 (Chat Proxy)
    前端發送提問後，由後端補上伺服器環境變數中的 API Key 轉發，100% 避免金鑰流失，並解決 CORS 限制。
    """
    data = request.json or {}
    provider = data.get('provider', 'gemini')
    user_query = data.get('query', '')
    model = data.get('model')
    client_key = data.get('apiKey', '')

    # 金鑰優先權：1. 伺服器端環境變數 (高優先級/安全)  2. 客戶端設定值 (動態覆寫)
    api_key = ""
    if provider == 'gemini':
        api_key = os.getenv('GEMINI_API_KEY') or client_key
    elif provider == 'openai':
        api_key = os.getenv('OPENAI_API_KEY') or client_key
    elif provider == 'anthropic':
        api_key = os.getenv('ANTHROPIC_API_KEY') or client_key

    if not api_key:
        return jsonify({
            "error": f"尚未配置伺服器環境變數或客戶端輸入金鑰。請在後端添加 {provider.toUpperCase()}_API_KEY，或點擊右上角設定面板提供。"
        }), 400

    system_prompt = (
        "你是一個極度專業的機器學習智慧學習助理。\n"
        "現在請根據這份「機器學習十大演算法研讀報告」知識庫，來回答使用者的問題。\n\n"
        "【規則指引】：\n"
        "1. 請一律使用繁體中文 (Traditional Chinese) 回答，口吻要友善、專業且充滿教育熱誠。\n"
        "2. 盡量有結構地回答，善用 Markdown (如粗體、條列點)、以及程式碼區塊。\n"
        "3. 對於所有數學公式，一律使用 LaTeX 格式，且一律使用 $ 表示行內公式，$$ 表示獨立區塊公式。例如：$y = wx + b$。\n"
        "4. 資訊要客觀、紮實，並深入解析其核心邏輯與工程實踐技巧。"
    )

    try:
        if provider == 'gemini':
            model_name = model or "gemini-2.5-flash-preview-09-2025"
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
            payload = {
                "contents": [{"role": "user", "parts": [{"text": user_query}]}],
                "systemInstruction": {"parts": [{"text": system_prompt}]}
            }
            response = requests.post(url, json=payload, timeout=30)
            response_data = response.json()
            
            if response.status_code == 200:
                text = response_data['candidates'][0]['content']['parts'][0]['text']
                return jsonify({"text": text})
            else:
                return jsonify({"error": response_data.get('error', {}).get('message', 'Gemini 後端通訊錯誤')}), response.status_code

        elif provider == 'openai':
            model_name = model or "gpt-4o-mini"
            url = "https://api.openai.com/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": model_name,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query}
                ],
                "temperature": 0.7
            }
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response_data = response.json()

            if response.status_code == 200:
                text = response_data['choices'][0]['message']['content']
                return jsonify({"text": text})
            else:
                return jsonify({"error": response_data.get('error', {}).get('message', 'OpenAI 後端通訊錯誤')}), response.status_code

        elif provider == 'anthropic':
            model_name = model or "claude-3-5-haiku-latest"
            url = "https://api.anthropic.com/v1/messages"
            headers = {
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            }
            payload = {
                "model": model_name,
                "max_tokens": 2048,
                "system": system_prompt,
                "messages": [{"role": "user", "content": user_query}]
            }
            response = requests.post(url, headers=headers, json=payload, timeout=30)
            response_data = response.json()

            if response.status_code == 200:
                text = response_data['content'][0]['text']
                return jsonify({"text": text})
            else:
                return jsonify({"error": response_data.get('error', {}).get('message', 'Anthropic 後端通訊錯誤')}), response.status_code

        else:
            return jsonify({"error": "不支援的 AI 服務商"}), 400

    except Exception as e:
        return jsonify({"error": f"後端代理失敗：{str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)