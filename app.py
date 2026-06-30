import os
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from src.load_and_extract_text import extract_text_from_pdf

from dotenv import load_dotenv

load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")
embedding_model=os.getenv("EMBEDDING_MODEL")
llm_model=os.getenv("LLM_MODEL")

llm=ChatGroq(groq_api_key=groq_api_key,model_name=llm_model)
# print(llm.invoke("who is Hardik Pandya?"))

if __name__=="__main__":
    extracted_text=extract_text_from_pdf("research-paper.pdf")
    print(extracted_text)
    
