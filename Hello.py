import langchain_helper as lch 
import streamlit as st
import matplotlib.pyplot as plt
import os


st.title("Casper's enemy roasting machine ")
st.text("Upload an image of who is flirting u : ")

file_uploaded = st.file_uploader('Choose the file', type = ['jpg', 'png', 'jpeg'])
if file_uploaded is not None:
        image = st.image(file_uploaded, caption=st.text('Casperz enemiez !!! :'))

name = st.text_area(label="What is the name of this person ?")
gender = st.text_area(label="tell me somthing about this man/woman ?")
st.button("Reset", type="primary")
if st.button('analyze') :
    result = lch.generate_stupid_names(name,gender)
    st.write(result)
