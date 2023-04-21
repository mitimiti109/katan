import streamlit as st
import pandas as pd
import time
import os
import plotly.express as px

col1,col2,col3,col4,col5 = st.columns(5)
with col1:
    st.image("red.jpg")
    st.write("開拓地        - +")
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
   col1_kouall =2
else:
   col1_kouall =0

if kouall == "青":
   col2_kouall =2
else:
   col2_kouall =0

if kouall == "黄":
   col3_kouall =2
else:
   col3_kouall =0

if  kouall == "白":
   col4_kouall =2
else:
   col4_kouall =0

col6,col7,col8,col9,col10 = st.columns(5)

with col6:
    col1_point = col1_kai + col1_toshi*2 +col1_meto*4 + col1_poi + col1_shouall +col1_kouall
    #st.write("_____________________________")
    st.write(f'<span style="color:black;background:pink"><font size="5">合計{col1_point}P</front></span>',unsafe_allow_html=True)


with col7:
    col2_point = col2_kai + col2_toshi*2 +col2_meto*4 + col2_poi + col2_shouall +col2_kouall
    #st.write("_____________________________")
    st.write(f'<span style="color:black;background:lightskyblue"><font size="5">合計{col2_point}P</front></span>',unsafe_allow_html=True)       

with col8:
    col3_point = col3_kai + col3_toshi*2 +col3_meto*4 + col3_poi + col3_shouall +col3_kouall
    #st.write("_____________________________")
    st.write(f'<span style="color:black;background:yellow"><font size="5">合計{col3_point}P</front></span>',unsafe_allow_html=True)

with col9:
    col4_point = col4_kai + col4_toshi*2 +col4_meto*4 + col4_poi + col4_shouall +col4_kouall
    #st.write("_____________________________")
    st.write(f'<span style="color:black;background:ivory"><font size="5">合計{col4_point}P</front></span>',unsafe_allow_html=True)
st.write('<span style="color:black;background:ivory"><font size="1">______________________________________________________________________________________________________</front></span>',unsafe_allow_html=True)

toshi_count = col1_toshi + col2_toshi + col3_toshi + col4_toshi + col1_meto +col2_meto +col3_meto +col4_meto
st.write(f'<span style="color:black;background:ivory"><font size="5">合計都市数={toshi_count}</front></span>',unsafe_allow_html=True)

if 'i' not in st.session_state:
   st.session_state.i = 0

if st.button("Clear"):
   st.session_state.i = 0
   os.remove('test')

if st.button("start"):
   st.session_state.i =1 
#st.write(st.session_state.i)

#jikan_list = []
#jikan_list.append(time.strftime('%H:%M:%S'))
#st.table(jikan_list)
#score_red_list = []
#score_red_list.append(col1_point)
#st.table(score_red_list)
#dict = {"jikan":jikan_list,"red_score":score_red_list}
#df= pd.DataFrame(dict)
#st.table(df)
#df.to_csv("test",mode='a')

#if st.session_state.i == 0:
#   os.remove('test')
#   dict_w = {"jikan":0,"赤":0,"青":0,"黄":0,"白":0}



#   jikan_list = []
#   jikan_list.append(time.strftime('%H:%M:%S'))
#   score_red_list = []
#   score_red_list.append(col1_point)
#   dict = {"jikan":jikan_list,"red_score":score_red_list}
#   df= pd.DataFrame(dict)
#   df.to_csv('test')

if st.session_state.i == 1:
   jikan_list = []
   jikan_list.append(time.strftime('%H:%M:%S'))
   score_red_list = []
   score_red_list.append(col1_point)
   score_blue_list = []
   score_blue_list.append(col2_point)
   score_yellow_list = []
   score_yellow_list.append(col3_point)
   score_white_list = []
   score_white_list.append(col4_point)      

   dict = {"jikan":jikan_list,"赤":score_red_list,"青":score_blue_list,"黄":score_yellow_list,"白":score_white_list}
   df= pd.DataFrame(dict)
   df.to_csv('test',mode='a',index=False,header=False)

line_data = pd.read_csv('test')
line_data.columns=["jikan","赤","青","黄","白"]
line_data.set_index("jikan",inplace=True)
#st.table(line_data)
line_data_t = line_data
#st.table(line_data_t)

#st.line_chart(line_data_t)

fig = px.line(line_data_t, title='カタン順位履歴',color_discrete_map={"赤":"red","青":"blue","黄":"yellow","白":"black"})
st.plotly_chart(fig)


#if st.session_state.i == 1:
# for k in range(10):
#   col1_point = col1_kai + col1_toshi*2 +col1_meto*4 + col1_poi + col1_shouall +col1_kouall
#   jikan_list.append(time.strftime('%H:%M:%S'))
#   score_red_list.append(col1_point)
#   st.table(score_red_list)
#   st.table(jikan_list)
#   time.sleep(1)

#jikan_list = []
#jikan_list.append(time.strftime('%H:%M:%S'))
#
#score_red_list = []
#score_red_list.append(col1_point)
#
#dict = {"jikan":jikan_list,"red_score":score_red_list}
#df= pd.DataFrame(dict)
#df.to_csv('test')


#if 'i' not in st.session_state:
#   st.session_state.i = 0

#def score_def():
#    score_red_list = []
#    return score_red_list

#def jikan_def():
#    jikan_list = []
#    return jikan_list


#@st.cache_data(score_def(),jikan_def())

#score_red_list =score_def()
#jikan_list = jikan_def()



#def cash_crear():
#   ikan_list = []
#   score_red_list = []
#   st.cache_data.clear()


#if st.button("Clear"):
#   st.session_state.i = 0
#   cash_crear()

#if st.button("start"):
#   st.session_state.i =1 



#if st.session_state.i == 1:
# for k in range(10):
#   col1_point = col1_kai + col1_toshi*2 +col1_meto*4 + col1_poi + col1_shouall +col1_kouall
#   jikan_list.append(time.strftime('%H:%M:%S'))
#   score_red_list.append(col1_point)
#   st.table(score_red_list)
#   st.table(jikan_list)
#   time.sleep(1)
#
#
#
#df= pd.DataFrame({
#            'red': pd.Series(score_red_list,index=jikan_list),
#   })
#st.table(df)
