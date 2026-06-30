import os,json
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from flask import Flask,render_template,request,jsonify
from src.load_and_extract_text import extract_text_from_pdf,extract_pdf_sections
from src.detect_and_split_sections import refine_sections,split_sections_with_content

from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

groq_api_key=os.getenv("GROQ_API_KEY")
embedding_model=os.getenv("EMBEDDING_MODEL")
llm_model=os.getenv("LLM_MODEL")

llm=ChatGroq(groq_api_key=groq_api_key,model_name=llm_model)
embedder=HuggingFaceEmbeddings(model_name=embedding_model)

# print(llm.invoke("who is Hardik Pandya?"))


@app.route('/')
def index():
    return render_template('index.html')





if __name__=="__main__":
    app.run(debug=True)