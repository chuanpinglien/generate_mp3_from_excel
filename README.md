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

## 🧩 安裝方式
建議使用虛擬環境安裝所需的python套件，以下為安裝指令

git clone https://github.com/chuanpinglien/generate_mp3_from_excel.git
cd generate_mp3_from_excel
pip install -r requirements.txt

## 🔐 設定 Google 認證（.env 檔）
為了安全性，建議在專案目錄下建立 .env 檔案，內容如下：

GOOGLE_APPLICATION_CREDENTIALS=your-google-key.json

並將該金鑰 your-google-key.json 指定路徑。

考慮安全性，我並未將.env 或金鑰檔上傳到 GitHub。

## 📊 Excel 格式說明
讀取的 Excel 檔，需要 group_2與settings 分頁，以下為格式說明。

### group_2 分頁
group_2 分頁紀錄單字(word)、例句(example)與中文解釋(zh-TW)。

範例如下：
| word  | example                        | zh-TW  |
|-------|--------------------------------|--------|
| apple | I eat an apple every morning. | 蘋果   |
| run   | She runs fast.                | 跑     |

### settings 分頁
另一個 settings 分頁是用來記錄聲音與播放參數。

為適應考試有不同腔調、人聲，目前程式寫法會將同一單字以男聲、女聲，輪流播放多種腔調。

- `language`：語音腔調（en-US 為美式，en-GB 為英式）
- `speaking_rate`：語速（單位為倍速，例如 1.0）
- `pause`：每段語音之間的靜音秒數
- `gender`：M 為男聲、F 為女聲
- `repeat`：每組內容重複次數
- `output prefix`：輸出檔案名稱前綴

範例如下：

| Key            | Value 1         | Value 2 |
|----------------|-----------------|---------|
| speaking_rate  | 1.0             |         |
| pause          | 0.8             |         |
| language       | en-US           | en-GB   |
| gender         | M               | F       |
| repeat         | 2               |         |
| output prefix  | Longman3000_lv6_group002 |   |

## 🧪 執行方式
python generate_mp3_from_excel.py

完成後會輸出一個 MP3 檔案(檔名前綴於上述output prefix中設定)，例如：

Longman3000_lv6_group002.mp3

## ✅ 注意事項
本專案需配合 Google Cloud Text-to-Speech API 使用，請先開通服務並下載金鑰 xxx.json。

建議將金鑰路徑設為環境變數或 .env，避免硬編碼。勿將任何 .json 金鑰檔案上傳至 GitHub

## 📄 授權 License
本專案以 MIT License 授權。使用者可自由修改、引用，僅需保留原作者資訊。

作者：Chuan-Ping Lien
最後更新：2025/3/29

