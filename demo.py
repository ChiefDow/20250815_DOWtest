import numpy as np
import pandas as pd
import streamlit as st

#標籤大小的設定
st.title("DEMO PAGE")
st.write("# This is a demo page for Streamlit.")
st.write("## This is a demo page for Streamlit.")
st.write("### This is a demo page for Streamlit.")
st.write("#### This is a demo page for Streamlit.")
st.write("##### This is a demo page for Streamlit.")
st.write("###### This is a demo page for Streamlit.")

#陣列
arr1 = np.array([1, 2, 3, 4, 5,6])
st.write(arr1)

#表格
df1 = pd.DataFrame([[11,22,33,44], [55,66,77,88]])
st.write(df1)
st.table(df1)

#核取方塊、選項按鈕、滑桿
st.write("核取方塊")
r1 = st.checkbox("外帶")
if r1:
    st.info("外帶選項")
else:
    st.info("內用選項")

checks = st.columns(2)
txt = ''
with checks[0]:
    r11 = st.checkbox("雞腿飯")
    if r11:
        txt += '雞腿飯 '
with checks[1]:
    r12 = st.checkbox("香腸飯")
    if r12:
        txt += '香腸飯 '
st.info(txt)        

st.write("選項按鈕")
b1 = st.radio("選擇一個選項",("咖啡","果汁","奶茶"))
st.info(b1)

b2 = st.radio("選擇一個選項",("餅乾","蛋糕","果凍"),key="b2")
st.info(b2)

st.write("滑桿")
num = st.slider("選擇一個數字", 1.0, 5.0,0.5) #1是起始，10是終止，0.5是起始值
st.info(num)
st.write("滑桿2")
num2 = st.slider("選擇一個數字", 1, 10, 5) #1是起始，10是終止，5是間格
st.info(num2)

#下拉選單
st.write("下拉選單")
city = st.selectbox("選擇一個城市",("台北","台中","高雄"))
if city == "台北":
    st.info("台北市")
elif city == "台中":
    st.info("台中市")   
else:
    st.info("高雄市")

st.sidebar.write("側邊選單")
city = st.sidebar.selectbox("選擇一個城市側邊顯示",("台北","台中","高雄"))
if city == "台北":
    st.sidebar.info("台北市")
elif city == "台中":
    st.sidebar.info("台中市")   
else:
    st.sidebar.info("高雄市")

st.write("## 按鈕")
a = st.number_input("num...")
b = st.number_input("num2...",key="b")
if st.button("相加"):
    st.info(f"num + num2 = {a + b}")
    st.write("## ",a + b)

