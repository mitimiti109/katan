import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title("プログレスバー")
latest = st.empty()
bar = st.progress(0)

for i in range(100):
  latest.text(f'jikann{i+1}')
  bar.progress(i+1)
  time.sleep(0.1)


st.title ("title")
st.write ("DataFrame")

df = pd.DataFrame(
    np.random.rand(20,3),
    #columns=["a","b","c"]
)

"""
#  A
## B
### C
``` python
import streamlit as st
import pandas as pd
import numpy as nm

"""

st.write(df)

st.line_chart(df)

st.area_chart(df)


rr = pd.DataFrame(
    np.random.rand(100,2)/(50,50)+(35.69,139.79),
    columns=["lat","lon"]
)

st.map(rr)
if st.checkbox('show image'):
 img = Image.open('20140825_120747451_iOS.jpg')
 st.image(img,caption="test",use_column_width=True)


op = st.selectbox(
 'あなたが好きな数字',
  list(range(1,11))
  )
"あなたが好きな数字は",op,"です"

lef,ry =st.beta_columns(2)
bt = lef.button("右カラムに文字表示")
if bt:(
  ry.write("ここは右からむ")
)

ex = st.beta_expander("問い合わせ")
ex.write("問い合わせ")

tx = st.text_input("あなたの趣味をおしえてください")
"あなたの首位は",tx,"です"

con = st.slider("あなたのコンディションは",0,100,50)
"コンディション",con


