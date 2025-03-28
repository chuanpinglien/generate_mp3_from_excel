
import os
import pandas as pd
from google.cloud import texttospeech

# 設定 Google 認證檔案路徑（請依實際位置修改）
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "main-xxx.json"

# 輸入檔案
#input_filename = "my_volcabulary.xlsx"
input_filename = "myscore6_vocab_groups.xlsx"


# 讀取 Excel
xls = pd.ExcelFile(input_filename)
meta_raw = pd.read_excel(xls, sheet_name='settings', header=None)
#words_df = pd.read_excel(xls, sheet_name='group_1')
words_df = pd.read_excel(xls, sheet_name='group_2')
output_prefix = 'Longman3000_lv6_group002'

# 解析 metadata
meta_dict = {}
for i in range(len(meta_raw)):
    key = str(meta_raw.iloc[i, 0]).strip()
    values = meta_raw.iloc[i, 1:].dropna().tolist()
    meta_dict[key] = values

# 提取參數
speaking_rate = float(meta_dict.get('speaking_rate', [1.0])[0])
pause = meta_dict.get('pause', ['0.8'])[0]
lang_list = meta_dict.get('language', ['en-US'])
repeat = int(meta_dict.get('repeat', [1])[0])
gender_list = meta_dict.get('gender', ['M'])
#output_prefix = meta_dict.get('output prefix', ['my_volcabulary'])[0]

# 初始化 TTS
client = texttospeech.TextToSpeechClient()
all_audio = b""

# 合成語音
for idx, row in words_df.iterrows():
    word = str(row['word'])
    sentence = str(row['example'])
    zh_explaination = str(row['zh-TW'])

    for gender in gender_list:
        if gender =="M":
            voice_gender = texttospeech.SsmlVoiceGender.MALE
        else:
            voice_gender = texttospeech.SsmlVoiceGender.FEMALE
        
        for lang_code in lang_list:
            for _ in range(repeat):
                # 1️⃣ 英文單字
                ssml_parts_en_word = []
                ssml_parts_en_word.append('<speak>')
                ssml_parts_en_word.append(f'<break time="{pause}s"/>')
                ssml_parts_en_word.append(f'<prosody pitch="+2st">{word}</prosody>')
                ssml_parts_en_word.append(f'<break time="{pause}s"/>')
                ssml_parts_en_word.append('</speak>')
                ssml_en_word = ''.join(ssml_parts_en_word)

                audio_en_word = client.synthesize_speech(
                    input=texttospeech.SynthesisInput(ssml=ssml_en_word),
                    voice=texttospeech.VoiceSelectionParams(language_code=lang_code,
                                                            ssml_gender=voice_gender),
                    audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3,
                                                          speaking_rate=speaking_rate)
                    ).audio_content

                # 2️⃣ 英文例句
                ssml_parts_en_sentence = []
                ssml_parts_en_sentence.append('<speak>')
                ssml_parts_en_sentence.append(f'<break time="{pause}s"/>')
                ssml_parts_en_sentence.append(f'<prosody pitch="+2st">{sentence}</prosody>')
                ssml_parts_en_sentence.append(f'<break time="{pause}s"/>')
                ssml_parts_en_sentence.append('</speak>')
                ssml_en_sentence = ''.join(ssml_parts_en_sentence)

                audio_en_sentence = client.synthesize_speech(
                    input=texttospeech.SynthesisInput(ssml=ssml_en_sentence),
                    voice=texttospeech.VoiceSelectionParams(language_code=lang_code,
                                                            ssml_gender=voice_gender),
                    audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3,
                                                          speaking_rate=speaking_rate)
                    ).audio_content


                # 3️⃣ 中文翻譯
                ssml_parts_zh_explaination = []
                ssml_parts_zh_explaination.append('<speak>')
                ssml_parts_zh_explaination.append(f'<break time="{pause}s"/>')
                ssml_parts_zh_explaination.append(f'<prosody pitch="+2st">{zh_explaination}</prosody>')
                ssml_parts_zh_explaination.append(f'<break time="{pause}s"/>')
                ssml_parts_zh_explaination.append('</speak>')
                ssml_zh_explaination = ''.join(ssml_parts_zh_explaination)
                
                audio_zh_explaination = client.synthesize_speech(
                    input=texttospeech.SynthesisInput(ssml=ssml_zh_explaination),
                    voice=texttospeech.VoiceSelectionParams(language_code='zh-TW',
                                                            ssml_gender=voice_gender),
                    audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3,
                                                          speaking_rate=speaking_rate)
                    ).audio_content
            

                # 4️⃣ 組合成單一 MP3 音訊片段
                all_audio += audio_en_word + audio_en_sentence + audio_zh_explaination

# 儲存音檔
with open(f"{output_prefix}.mp3", "wb") as f:
    f.write(all_audio)

print(f"✅ 語音檔已輸出為 {output_prefix}.mp3")
