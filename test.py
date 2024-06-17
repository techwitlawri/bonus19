import streamlit as st
st.slider("amount", min_value=10,max_value=30)
dir(st)

st.radio("amount", options=[10, 30])

st.button("amount", help= "amount")

