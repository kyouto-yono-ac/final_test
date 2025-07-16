import streamlit as st
import pandas as pd
import google.generativeai as genai


# データの読み込み
data = pd.read_csv('data/data.csv')

# データの表示
st.title('データ表示アプリ')
st.write(data)

api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-2.0-flash-lite')


# ユーザー入力(画面下部に固定表示される入力フィールド)
prompt = st.chat_input("メッセージを入力してください...")
if prompt: # ユーザーが何か入力してEnterを押した場合
    # 1. ユーザーメッセージを表示(チャット画面の右側に表示)
    with st.chat_message("user"):
        st.markdown(prompt)
    # 2. AI応答を生成・表示(チャット画面の左側、アイコン付きで表示)
    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)