# Vector Store Intro

This project is a basic introduction to using vector stores with LangChain and OpenAI's embeddings API. It demonstrates how to embed textual data, store it in a vector database (ChromaDB), and perform similarity search for information retrieval.

##  What This Project Does

- Loads and splits text documents
- Embeds documents using OpenAI embeddings
- Stores them in a Chroma vector store
- Retrieves similar content based on a query
- Uses LangChain's Retriever interface

##  Files Overview

### `main.py`
Contains the core script that:
- Loads a `.txt` file
- Splits the content into chunks
- Embeds the content using OpenAI's embedding model
- Stores and searches chunks in ChromaDB

### `requirements.txt`
Specifies all the dependencies, including:
- `langchain`
- `openai`
- `chromadb`
- `python-dotenv` (for managing your API keys)

### `.env` (not included)
You need to create a `.env` file with the following content:

```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
(Optional for tracing)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=SIMPLECHATBOT
```

##  Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Your API Key

Create a `.env` file in the project root:
```
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

### 3. Run the Project

```bash
python main.py
```






##  Author

Developed by [Senanur Korkmaz](https://github.com/senakorkmaz)
