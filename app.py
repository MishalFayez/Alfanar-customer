import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    

)
css='''
[data-testid="stSidebarNav"] {
    position:absolute;
    bottom: 0;
    color: red;
    color:white
}
.css-j7qwjs {
    color:white
}
'''

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.sidebar.image("new.png")
st.markdown("""
<style>
[data-testid=stSidebar] {
  background-color: #2d5d9f;
}
</style>
""", unsafe_allow_html=True)



st.sidebar.markdown("# <span style='color:white'>Customer Registration</span> ", unsafe_allow_html=True)




