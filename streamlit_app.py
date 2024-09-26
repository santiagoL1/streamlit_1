import streamlit as st 
st.title('My first streamlit app')
st.write('This is a simple streamlit app')
user_input = st.text_input("enter your name")
st.write('your name is ', user_input)
age = st.slider("choose your age",1,100)
st.write("you are ", age, " years old")
if st.button('say hello'):
  st.write("hello there")

