import streamlit as st
st.set_page_config(page_title="portfolio",page_icon="(❁´◡`❁)",layout="wide")
st.title("Gudise.Jyothi sri vinaya",anchor=False)
st.subheader("Frontend web developer")
with st.container(border=True):
    st.info("I am .....")
col1,col2,col3=st.columns(3)
with col1:
    with st.expander(label="know me more",expanded =False):
        st.write("hey.....")
        st.image("sri.jpg",width=120)
        
