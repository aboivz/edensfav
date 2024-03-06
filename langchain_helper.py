from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import streamlit as st

OPENAI_API_KEY= st.secrets["key"]

def generate_stupid_names(name,gender):
    llm = OpenAI(temperature=0.6)

    prompt_template_name = PromptTemplate(
        input_variables=['name','gender'],
        template="Write a short roast to make fun of a person named {name} which is {gender}, make it ridiculous, stupid and funny of them that no one will like them. And tell them to stop"
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="names")

    response = name_chain({'name': name, 'gender': gender})

    return response

if __name__ == "__main__":
    print(generate_stupid_names("shitty, stupid, racist","cat"))
   