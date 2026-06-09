# 開發過程 Prompt 紀錄 (Prompt Log)

這份文件記錄了在開發 `ML_Algorithms_introduce` 專案時，與 AI 助理（如 Gemini）互動所使用的提示詞 (Prompts)。
這有助於追蹤程式碼的生成邏輯，並方便未來進行重現、修改或分享。

---

## 階段一：專案初始化與架構設計

**Prompt 1: 建立專案結構**
> 你現在是一位資深的 AI/ML 軟體工程師。我想要建立一個名為 "ML_Algorithms_introduce" 的 Python 專案，用來介紹常見的機器學習演算法。請幫我設計一個符合最佳實踐的專案資料夾架構，並說明每個資料夾的用途。

**Prompt 2: Git 安全性設定**
> 請幫我撰寫一份 `.gitignore` 檔案，適用於 Python 開發環境，並確保 `.env` 檔案（用來放 API Key）以及虛擬環境不會被上傳到 GitHub。

## 階段二：核心演算法實作 (範例)

**Prompt 3: 演算法生成**
> 請用 Python 實作一個基礎的「線性迴歸 (Linear Regression)」模型。請包含訓練 (fit) 和預測 (predict) 方法，並在程式碼中加上詳細的中文註解解釋數學原理。

**Prompt 4: 資料視覺化**
> 請幫我寫一段程式碼，使用剛建立的模型進行訓練，並使用 matplotlib 畫出預測值與實際值的散佈圖。

## 階段三：整合 Gemini API

**Prompt 5: API 呼叫與環境變數讀取**
> 我想在專案中整合 Gemini API，讓系統可以自動呼叫 Gemini 產生一段演算法的白話文解釋。請教我如何使用 Python 套件 `python-dotenv` 讀取 `.env` 內的 `GEMINI_API_KEY` 並發送 API 請求。
> 