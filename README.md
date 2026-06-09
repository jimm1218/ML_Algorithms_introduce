# 機器學習演算法介紹 (ML Algorithms Introduce)
**連結請點此：https://ml-algorithms-introduce-gaw2.vercel.app/**

## 📝 產品介紹

這是一個專注於介紹與實作各種基礎到進階**機器學習演算法 (Machine Learning Algorithms)** 的專案。
本專案旨在提供清晰、易懂的程式碼範例與原理解釋，幫助開發者與學習者快速掌握機器學習的核心概念。

本專案的特色包含：
- **演算法實作**：包含線性迴歸、決策樹、KNN 等經典演算法的 Python 實作與範例。
- **AI 輔助學習**：整合了 **Gemini API**，可用於輔助生成資料、解釋演算法結果或進行互動式的觀念問答。
- **開箱即用**：提供結構化的資料夾設計與測試資料，讓學習者能快速上手。

## 📂 資料夾架構圖

```text
ML_Algorithms_introduce-main/
├── .env                # 環境變數設定檔 (存放 Gemini API Key 等機密資訊，不應上傳)
├── .gitignore          # Git 忽略清單
├── README.md           # 專案說明文件
├── prompt.md           # AI 協作開發過程之 Prompt 紀錄
├── requirements.txt    # Python 依賴套件清單
├── data/               # 存放訓練與測試用的資料集 (Datasets)
├── notebooks/          # Jupyter Notebooks (適合互動式教學與資料探索)
└── src/                # 原始碼目錄
    ├── algorithms/     # 各類 ML 演算法實作 (如: LinearRegression, DecisionTree)
    ├── utils/          # 共用工具函式 (如: 資料前處理、視覺化)
    └── main.py         # 程式執行主入口
```

## 🚀 快速開始

### 1. 安裝環境與套件
請確認您已安裝 Python，建議使用虛擬環境 (Virtual Environment)。然後執行以下指令安裝所需套件：
```bash
pip install -r requirements.txt
```

### 2. 環境變數設定 (Gemini API)
本專案需要使用 Gemini API。請在專案根目錄下建立 `.env` 檔案，並加入您的金鑰：
```env
GEMINI_API_KEY=您的_API_KEY_填寫在這裡
```
> **安全提醒**：請確保 `.env` 檔案已加入 `.gitignore` 中，以避免將機密金鑰推送到 GitHub。

### 3. 執行專案
準備就緒後，您可以執行主程式來觀看演算法的範例與結果：
```bash
python src/main.py
```
