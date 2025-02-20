import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns([0.5, 1])



with col1:
    st.title("SER")
    st.subheader("Quantity: 22")
    st.subheader("Size: 6 ft")
    st.link_button(label="Excel",
                   url="https://1drv.ms/x/c/2f5d6a56f202642b/EQJ58CO4rZpBvep8a6Ru86oBGDugB_c1yW8rz48weAJtrA?e=km9iVn")

with col2:
    st.image("1.jpg", width=300)
