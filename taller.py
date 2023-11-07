import os
import pinecone
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone


def pinecone_stuff():
    pinecone.init(api_key=os.getenv('PINECONE_API_KEY'),environment=os.getenv('PINECONE_ENVIRONMENT'))
    embeddings = OpenAIEmbeddings()
    
    directory = ["texto\economia.txt","texto\ingenieria-civil.txt","texto\ingenieria-electrica.txt","texto\ingenieria-electronica.txt","texto\ingenieria-industrial.txt","texto\ingenieria-sistemas.txt"]
    for archive in directory:
        with open(archive, 'r', encoding='utf8', errors='ignore') as file:
            text = file.read()
        data=Pinecone.from_texts(texts=[text],embedding=embeddings,index_name= "documentos")
    
 
@tool("sayHello", return_direct=True)
def say_hello(name:str) -> str:
    """Answer when someone say hello"""
    return f"Hello {name}! My name is Sainapsis"


@tool("searchPinecone", return_direct=True)
def search_pinecone(query:str, k:int) -> list:
    """Search in pinecone"""
    index = pinecone.Index(index_name="documentos")
    data = Pinecone.from_texts(texts=[text], embedding=embeddings, index_name="documentos")
    results = data.similarity_search(query, k)
    return results

def main():
    llm = ChatOpenAI(temperature=0.0)
    tools = [
        say_hello,
        search_pinecone
    ]
    agent = initialize_agent(
        tools=tools,
        llm = llm,
        agent = AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
    
    print(agent.run("Hello! my name is David"))
    print(agent.run("searchPinecone('Ingeniería Civil', 1)"))
    

main()