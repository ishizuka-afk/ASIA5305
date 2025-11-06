import streamlit as st
import pandas as pd
import numpy as np

# アプリのタイトル
st.title('シンプルなデータ可視化アプリ')

# 説明文
st.write('このアプリではランダムデータを生成し、折れ線グラフとして表示します。')

# ランダムデータ生成
st.sidebar.header('設定')
n = st.sidebar.slider('データポイント数', min_value=10, max_value=100, value=50)

# データフレーム作成
data = pd.DataFrame(
    {
        'x': np.arange(n),
        'y': np.random.randn(n).cumsum()
    }
)

# グラフ表示
st.line_chart(data, x='x', y='y')
