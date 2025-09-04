#  AI Text Summarizer - Streamlit App

This is a simple and powerful **AI-powered Text Summarizer** built using **Python**, **Streamlit**, and the `facebook/bart-large-cnn` model from Hugging Face Transformers.  
It allows you to paste long text or upload `.txt` files and get concise summaries using state-of-the-art NLP models.

---

##  Features

- Summarize long articles or documents
- Upload `.txt` files or paste text
- Built with `facebook/bart-large-cnn` summarization model
- Lightweight and fast Streamlit UI

---

##  How to Run the App Locally

###  1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-text-summarizer-streamlit.git
cd ai-text-summarizer-streamlit
```

###  2. Create a Virtual Environment

```bash
python -m venv venv
```
- Windows
```bash
venv\Scripts\activate
```
- macOS/Linux
```bash
source venv/bin/activate
```

###  3. Install Dependencies

```bash
pip install -r requirements.txt
```

###  4. Run the Streamlit App
```bash
streamlit run app.py
```

###  Deploy on Streamlit Cloud

#### Steps:
- Push your code to a GitHub repository
- Visit: https://streamlit.io/cloud
- Sign in with GitHub
- Click "New app"
- Select your repo and the app.py file
- Click Deploy
