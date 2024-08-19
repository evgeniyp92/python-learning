import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', use_column_width=True)

with col2:
    st.title('Evgeniy Pimenov')
    st.info('asdlfija;eoirfuksljdf aiguae adlghelr aoiefaskdjhfklasdhf liuaefkjharflgkjhasd')