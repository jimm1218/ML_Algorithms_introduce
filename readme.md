🤖 機器學習十大演算法互動式精裝圖譜 (Machine Learning Algorithms Interactive Handbook)

這是一個以單一 HTML 檔案核心構建的互動式機器學習教學與探索平台。旨在透過視覺化沙盒、全維度矩陣對比與決策引導精靈，幫助初學者與開發者快速掌握機器學習的十大核心演算法。

🌐 在線預覽 (Live Demo)

Netlify: https://papaya-lolly-0a2853.netlify.app/

Vercel: https://web-ml-algorithms-introduce.vercel.app/

🌟 核心功能 (Features)

1. 演算法探索器 (Algorithm Explorer)

深度知識庫：涵蓋 10 種最經典的機器學習演算法，包含原理說明、數學公式（使用 KaTeX 渲染）、優缺點對比與應用場景。

實戰程式碼：提供 Scikit-learn / XGBoost 極簡範例程式，並支援一鍵複製。

動態沙盒模擬 (Interactive Sandbox)：透過滑桿與按鈕，即時視覺化體驗決策邊界、擬合直線與迭代過程。

2. 全維度對比矩陣 (Comparison Matrix)

將十大演算法放在同一個表格中橫向對比。

比較維度：核心任務、可解釋性、訓練與預測速度、特徵尺度敏感度、抗噪能力與主要調參重點。

篩選功能：提供快速篩選按鈕（迴歸、分類、非監督式）。

3. 決策引導精靈 (Decision Wizard)

透過簡單的問答（是否有標籤？可解釋性要求？數據規模？等），一步步引導使用者找到最適合當前任務的演算法。

🧠 收錄的十大演算法 (Top 10 Algorithms)

監督式學習 (Supervised Learning)

線性迴歸 (Linear Regression)

邏輯迴歸 (Logistic Regression)

決策樹 (Decision Tree)

隨機森林 (Random Forest)

支持向量機 (SVM)

K-近鄰演算法 (KNN)

單純貝氏 (Naive Bayes)

梯度提升機 (Gradient Boosting / XGBoost)

非監督式學習 (Unsupervised Learning)

K-Means 分群 (K-Means Clustering)

主成分分析 (PCA)

📂 專案資料夾架構

ml-algorithms-handbook/
├── app.py              # Flask 後端服務 (API 代理與路由處理)
├── data.json           # 核心知識庫與測驗數據庫
├── index.html          # 前端互動主介面 (SPA 核心)
├── requirements.txt    # Python 依賴清單
├── .env                # 環境變數 (存放 API 金鑰)
└── README.md           # 專案說明文件


🛠️ 技術堆疊 (Tech Stack)

前端框架：純 HTML5, CSS3, Vanilla JavaScript (單一檔案架構)

CSS 框架：Tailwind CSS (透過 CDN 引入)

數學公式渲染：KaTeX

圖示庫：Lucide Icons

後端架構：Python Flask (作為安全 API 代理層)
