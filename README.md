# 🎧 generate_mp3_from_excel

使用 Google Cloud TTS 語音合成 API，從 Excel 字彙表自動產生包含英文單字、例句與中文翻譯的 MP3 音訊檔。  
本專案適用於英語學習、教材製作、個人化字彙練習等應用。

🔗 GitHub Repo: [chuanpinglien/generate_mp3_from_excel](https://github.com/chuanpinglien/generate_mp3_from_excel)

---

## 🚀 功能特色

- 從 Excel 檔讀取單字、例句與中文翻譯
- 使用 Google Cloud Text-to-Speech 產生自然語音
- 支援語速、聲音性別、語言多版本切換
- 可設定多次重複與中間停頓
- 將所有語音輸出為單一 MP3 檔案

---

## 🧩 安裝方式

git clone https://github.com/chuanpinglien/generate_mp3_from_excel.git
cd generate_mp3_from_excel

# 建議使用虛擬環境
pip install -r requirements.txt


## 🔐 設定 Google 認證（.env 檔）
為了安全性，請在專案目錄下建立 .env 檔案，內容如下：

GOOGLE_APPLICATION_CREDENTIALS=your-google-key.json
並將該金鑰 .json 放入同一資料夾中。請勿將 .env 或金鑰檔上傳到 GitHub！

## 📊 Excel 格式說明
# 請使用以下格式編輯你的 Excel 檔，需要group_2與settings 分頁

# group_2 由以下格式紀錄單字、例句與解釋
word    example                         zh-TW
apple   I eat an apple every morning.   蘋果
run	    She runs fast.	                跑

# 以及另需設定一個 settings 分頁，以記錄聲音與播放參數，內容範例如下(en-US，為美國腔英文、en-GB為英國腔英文)：
Key             Value 1	Value 2
speaking_rate	1.0	
pause	        0.8	
language        en-US   en-GB
gender	        M       F	
repeat	        2	
output prefix	Longman3000_lv6_group002	

## 🧪 執行方式
python generate_mp3_from_excel.py
完成後會輸出一個 MP3 檔案，例如：
Longman3000_lv6_group002.mp3

## ✅ 注意事項
本專案需配合 Google Cloud Text-to-Speech API 使用，請先開通服務並下載金鑰 xxx.json。

建議將金鑰路徑設為環境變數或 .env，避免硬編碼。勿將任何 .json 金鑰檔案上傳至 GitHub

## 📄 授權 License
本專案以 MIT License 授權。使用者可自由修改、引用，僅需保留原作者資訊。

作者：Chuan-Ping Lien
最後更新：2025/3/29

