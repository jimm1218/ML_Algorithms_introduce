AI 智慧數據工作區：10 大機器學習演算法全互動實驗室

本專案是一個全方位的機器學習互動式學習與研究平台。它完美地將詳細的演算法學術報告、11 個即時 HTML5 數據實驗室、隨堂知識挑戰測驗，以及具備 RAG 知識庫檢索與雲端模型對接的 AI 智慧對話助教融合在一個流暢且高響應性的單網頁應用中。

🚀 核心產品特色

1. 11 大單元全互動數據實驗室 (Interactive Sandbox)

不只是閱讀報告！我們為所有演算法單元量身打造了專屬的 HTML5 Canvas 模擬器：

線性迴歸：自訂散點，即時最小平方法 (OLS) 擬合最適直線。

邏輯斯迴歸：手動拉動斜率與 Bias 偏置，觀測 Sigmoid 分類曲線的幾何拉扯。

決策樹：自訂點擊分類點，系統在前端即時執行基尼不純度 (Gini Impurity) 運算，自動切分出軸平行的階梯決策邊界。

支持向量機 (SVM)：手動調整懲罰係數 $C$，系統會自動為落在超平面邊界帶上的點標記亮黃色光環（支持向量）。

單純貝氏：自訂分類散點，後端/前端即時渲染雙高斯機率分佈密度漸層（Contour Map）。

K-Nearest Neighbors：移動綠色預測點，調整 $K$ 值，即時拉出鄰近連線並進行多數決投票。

K-Means 聚類：點擊新增灰點，點選「單步疊代」觀測「分配數據」➔「更新質心」的收斂動畫。

隨機森林 & Boosting：調整樹木總數或提升輪數，觀測多個弱分類器如何融合成極其強韌、平滑的最終分類邊界。

主成分分析 (PCA)：一鍵開啟投影，看 2D 數據點如何正交投射至 PC1 最大特徵向量軸。

偏差與變異取捨：經典四靶心彈點模型，提供最生動的 Bias-Variance 天平直覺。

人工神經網路：前向傳播多層神經元權重鏈視覺化，深入感知深度學習的底層。

2. 隨堂知識挑戰測驗 (Interactive Quiz)

每個單元皆內建多道精心設計的選擇題（含單選與深入詳盡解析），幫助使用者在調參實驗後，即時進行學術與工程知識的自我檢算，答題後會顯示詳盡的數學與邏輯原理解析。

3. 雙驅動 AI 對話助教 (Hybrid AI Engine)

免金鑰本地檢索 (Local RAG)：使用者無須輸入 API Key 即可使用，前端特徵關鍵字算法會自動對應至 11 大單元的學術報告與優缺點評析，給予最精準的回答。

雲端大語言模型對接：提供極高擴充性的 Flask 代理服務，支援 Gemini 2.5、OpenAI GPT-4o、Anthropic Claude 3.5。

4. 前後端解耦與隱私安全

所有演算法報告、優缺點評析、隨堂測驗題庫皆抽離至 data.json 中，前端動態 Fetch 載入。

呼叫 LLM 的 API Key 統一儲存在本地私密環境變數 .env 中，由後端 app.py 中繼代理轉發，100% 杜絕前端金鑰外洩風險與 CORS 跨網域連線阻擋。

📂 專案資料夾架構

本專案採用最為優雅、平坦且高度擴充的微服務目錄架構：

d:\data\ml_assistant\ (您的專案根目錄)
 ├── app.py               # Flask 後端主程式 (處理大模型中繼 API 轉發與靜態檔案路由)
 ├── data.json            # 11 大單元的「研讀內容、優缺點、應用評析、隨堂測驗」結構資料庫
 ├── index.html           # 前端 SPA 網頁 (含 Canvas 實驗室、測驗引擎與極致滾動 UI)
 ├── requirements.txt     # Python 後端套件依賴清單 (Flask、Requests、Dotenv)
 ├── .env                 # 本地私密環境變數檔 (存放您的 Gemini/OpenAI API 金鑰)
 └── README.md            # 本專案說明文件


⚙️ 快速安裝與本地部署

請依照以下步驟，在您的電腦上快速啟動這個互動式機器學習學習平台：

步驟 1：建立專案目錄並放置檔案

請在您的本地端硬碟中建立資料夾（例如 d:\data\ml_assistant\），並將專案所屬的 app.py、data.json、index.html 以及 requirements.txt 檔案放入。

步驟 2：配置環境變數金鑰

在該目錄下手動建立一個名為 .env 的文字檔案，並填入您自有的雲端模型 API Key（留空代表僅使用免密鑰本地檢索）：

GEMINI_API_KEY=您的Gemini金鑰
OPENAI_API_KEY=您的OpenAI金鑰


步驟 3：安裝依賴套件

打開您的終端機（CMD、PowerShell 或 Terminal），切換至該專案根目錄，並安裝所需套件：

cd d:\data\ml_assistant\
pip install -r requirements.txt


步驟 4：啟動 Flask 服務

執行後端主程式：

python app.py


步驟 5：打開瀏覽器體驗

在您的瀏覽器中輸入網址，即可開始完美的互動式 ML 學習之旅：

[http://127.0.0.1:5000](http://127.0.0.1:5000)


🛠️ 開發與技術架構

前端：Tailwind CSS (響應式深色美學), Marked.js (Markdown 即時解析), KaTeX (極速 LaTeX 數學公式渲染), Vanilla HTML5 Canvas。

後端：Python Flask (靜態映射、API 代理伺服器), Requests (模型中繼代理連線), Python-Dotenv (變數加載)。
