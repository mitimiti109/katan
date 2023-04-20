import streamlit as st
import pandas as pd

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.image("red.jpg")
    st.write("開拓地")
    col1_kai = st.number_input("col1_kait",0,10,1,label_visibility="collapsed")
    st.write("都市")
    col1_toshi = st.number_input("ol1_toshit",0,10,1,label_visibility="collapsed")
    st.write("メトロポリス")
    col1_meto = st.number_input("col1_metot",0,10,0,label_visibility="collapsed",)
    st.write("戦略・英雄P")
    col1_poi = st.number_input("ol1_poit",0,10,0,label_visibility="collapsed")
    #col1_point = col1_kai + col1_toshi*2 +col1_meto*4 + col1_poi
    #st.write("_____________________________")
    #st.write('合計ポイント',col1_point)      
with col2:
    st.image("blue.jpg")
    st.write("開拓地")
    col2_kai = st.number_input("col2_kai",0,10,1,label_visibility="collapsed")
    st.write("都市")
    col2_toshi = st.number_input("col2_toshi",0,10,1,label_visibility="collapsed")
    st.write("メトロポリス")
    col2_meto = st.number_input("ccol2_meto",0,10,0,label_visibility="collapsed")
    st.write("戦略・英雄P")
    col2_poi = st.number_input("col2_poiP",0,10,0,label_visibility="collapsed")
    #col2_point = col2_kai + col2_toshi*2 +col2_meto*4 + col2_poi
    #st.write("_____________________________")
    #st.write('合計ポイント',col2_point)
    
with col3:
    st.image("yellow.jpg")
    st.write("開拓地")
    col3_kai = st.number_input("col3_kai",0,10,1,label_visibility="collapsed")
    st.write("都市")
    col3_toshi = st.number_input("ocl3_toshi",0,10,1,label_visibility="collapsed")
    st.write("メトロポリス")
    col3_meto = st.number_input("ccol3_meto",0,10,0,label_visibility="collapsed")
    st.write("戦略・英雄P")
    col3_poi = st.number_input("col3_poiP",0,10,0,label_visibility="collapsed")
    #col3_point = col3_kai + col3_toshi*2 +col3_meto*4 + col3_poi
    #st.write("_____________________________")
    #st.write('合計ポイント',col3_point)

with col4:
    st.image("white.jpg")
    st.write("開拓地")
    col4_kai = st.number_input("col4_kai",0,10,1,label_visibility="collapsed")
    st.write("都市")
    col4_toshi = st.number_input("ocl4_toshi",0,10,1,label_visibility="collapsed")
    st.write("メトロポリス")
    col4_meto = st.number_input("ccol4_meto",0,10,0,label_visibility="collapsed")
    st.write("戦略・英雄P")
    col4_poi = st.number_input("col4_poiP",0,10,0,label_visibility="collapsed")
    #col4_point = col4_kai + col4_toshi*2 +col4_meto*4 + col4_poi
    #st.write("_____________________________")
    #st.write('合計ポイント',col4_point)

with col5:
   shouall = st.radio("商人", ("赤","青","黄","白","なし"),horizontal=True,index=4)
   kouall = st.radio("最長交易路",("赤","青","黄","白","なし"),horizontal=True,index=4)


if shouall == "赤":
   col1_shouall =1
else:
   col1_shouall =0

if shouall == "青":
   col2_shouall =1
else:
   col2_shouall =0

if shouall == "黄":
   col3_shouall =1
else:
   col3_shouall =0

if shouall == "白":
   col4_shouall =1
else:
   col4_shouall =0

if kouall == "赤":
   col1_kouall =1
else:
   col1_kouall =0

if kouall == "青":
   col2_kouall =1
else:
   col2_kouall =0

if kouall == "黄":
   col3_kouall =1
else:
   col3_kouall =0

if  kouall == "白":
   col4_kouall =1
else:
   col4_kouall =0

col6,col7,col8,col9,col10 = st.columns(5)

with col6:
    col1_point = col1_kai + col1_toshi*2 +col1_meto*4 + col1_poi + col1_shouall +col1_kouall
    #st.write("_____________________________")
    st.write('合計ポイント',col1_point) 
    st.write('<span style="color:red;background:pink">該当するデータがありません・・・・</span>',
              unsafe_allow_html=True) 

with col7:
    col2_point = col2_kai + col2_toshi*2 +col2_meto*4 + col2_poi + col2_shouall +col2_kouall
    #st.write("_____________________________")
    st.write('合計ポイント',col2_point)        

with col8:
    col3_point = col3_kai + col3_toshi*2 +col3_meto*4 + col3_poi + col3_shouall +col3_kouall
    #st.write("_____________________________")
    st.write('合計ポイント',col3_point)

with col9:
    col4_point = col4_kai + col4_toshi*2 +col4_meto*4 + col4_poi + col4_shouall +col4_kouall
    #st.write("_____________________________")
    st.write('合計ポイント',col4_point)
st.write("___________________________________________________________________________________")

toshi_count = col1_toshi + col2_toshi + col3_toshi + col4_toshi + col1_meto +col2_meto +col3_meto +col4_meto
st.write("合計都市数＝",toshi_count)