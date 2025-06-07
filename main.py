from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]

vector_store = Chroma.from_documents(
    documents= documents,
    embedding=OpenAIEmbeddings()
)

retriever = RunnableLambda(vector_store.similarity_search).bind(k=1)

llm = ChatOpenAI()

message = """
Answer this question using the provided context only.
{question}
context:
{context}
"""

prompt = ChatPromptTemplate.from_messages(["humman",message])

chain = {"context": retriever,"question": RunnablePassthrough() }|prompt | llm

if __name__ == "__main__":
    #print(vector_store.similarity_search("dog"))
    #print(vector_store.similarity_search_with_score("cat"))
    #embedding = OpenAIEmbeddings().embed_query("dog")
    #print(vector_store.similarity_search_by_vector(embedding=embedding))
    #print(retriever.batch(["Cat","shark"]))

    response = chain.invoke("tel me about cats")
    print(response.content)