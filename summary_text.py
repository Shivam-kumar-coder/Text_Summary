import streamlit as st 
from transformers import pipeline, set_seed

@st.cache_resource
def summar():
  return pipeline('summarization',model='sshleifer/distilbart-cnn-12-6')
gen=summar()
st.title("✍ Text Summarization App")
i=st.chat_input(" Enter Your Sentences 📌")
l=st.slider("Choose max lenght Word of summary",30,200,40,step=5)

if i:
  with st.spinner(" Generating Summary ✍ ......."):
    set_seed(42)
    result=gen(i,max_length=l,num_return_sequences=1)
    st.success("✔ Genterated Summary ")
    st.write(result[0]['summary_text'])
else:
  st.info("Please Enter Sentences")
    

