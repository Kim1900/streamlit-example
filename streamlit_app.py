import streamlit as st
from streamlit_ace import st_ace

st.title("""
Athletes Performance Analysis
Code Editor App
""")

col1, col2 = st.columns(2)

with col1:
    st.markdown("## Input")
    code = st_ace(language = 'python', theme = 'monokai')

with col2:
    st.markdown("## Output")
    #st.markdown('``` python\n' + code) # 1 option to print code
    st_ace(value = code,
    language = 'python',
    theme = 'xcode',
    readonly = True)
