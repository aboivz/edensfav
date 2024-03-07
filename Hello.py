import langchain_helper as lch 
import streamlit as st
import matplotlib.pyplot as plt
import os


st.title("Casper's enemy roasting bot ")
st.text("Notice: This is an aggressive bot that will roast it's target,  \nall of the bot's answers is AI trained with none of Casper's interferences.  \nSo I'm not responsible for any of the target's emotional damages.  \nBut if it's someone who is flirting with Eden.  \nObiviously, I don't care lol. ")

st.text("Upload an image of who is flirting u Eden : ")

file_uploaded = st.file_uploader('Choose the file', type = ['jpg', 'png', 'jpeg'])
if file_uploaded is not None:
        image = st.image(file_uploaded, caption=st.text('Casperz enemiez detected !!! :'))

name = st.text_area(label="What is the name of this person ?")
gender = st.text_area(label="Tell me somthing about this man/woman ?")

st.text("Bot's verdict :")
st.button("Reset", type="primary")
if st.button('Analyze') :
    result = lch.generate_stupid_names(name,gender)
    st.write(result)
