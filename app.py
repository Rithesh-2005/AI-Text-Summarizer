import streamlit as st
from transformers import pipeline

#set page configuration
st.set_page_config(page_title="Text Summarizer", layout="centered", page_icon=":memo:")

#load sumarizer
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")
summarizer = load_summarizer()

#add tittle and description
st.title("🧠 Text Summarizer")
st.markdown("This app uses `facebook/bart-large-cnn` from Hugging Face to summarize large bodies of text. "
    "You can either **paste text** or **upload a `.txt` file** to get a summary.")

#input
opt = st.radio("Choose input method:", ("Paste text", "Upload .txt file"))
text_input = ""

if opt == "Paste text":
    text_input = st.text_area("Paste you text here:", height = 300)
else:
    file = st.file_uploader("Upload .txt file here:", type=["txt"])
    if file:
        text_input = file.read().decode("utf-8")

#summarize
if st.button("Summarize"):
    if not text_input.strip():
        st.warning("Pplease provide some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            res = summarizer(text_input, max_length=130, min_length=30, do_sample=False)
            st.subheader("📝 Summary:")
            st.success(res[0]['summary_text'])