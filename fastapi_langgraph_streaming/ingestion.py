from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

urls = [
    "https://namu.wiki/w/%EC%95%BC%EA%B5%AC/%EA%B2%BD%EA%B8%B0%20%EB%B0%A9%EC%8B%9D",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=0, model_name="gpt-4o-mini"
)
doc_splits = text_splitter.split_documents(docs_list)

chroma_directory = "./chroma"
# vectorstore = Chroma.from_documents(
#     documents=doc_splits,
#     collection_name="baseball-chroma",
#     embedding=OpenAIEmbeddings(),
#     persist_directory="./chroma",
# )

retriever = Chroma(
    collection_name="baseball-chroma",
    embedding_function=OpenAIEmbeddings(),
    persist_directory=chroma_directory,
).as_retriever()
