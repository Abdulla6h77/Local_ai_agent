# Local AI Agent - Pizza Restaurant Review Assistant

A local AI-powered chatbot that specializes in answering questions about pizza restaurants using LangChain, Ollama, and ChromaDB for vector storage. The agent leverages historical restaurant reviews to provide informed responses about pizza establishments.

## Features

- Specialized pizza restaurant knowledge assistant
- Vector-based similarity search for relevant reviews
- Local LLM integration using Ollama
- Persistent vector storage using ChromaDB
- CSV-based review data processing

## Prerequisites

- Python 3.12
- Ollama installed with `llama3` and `mxbai-embed-large` models
- ChromaDB for vector storage

## Installation

1. Clone the repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `main.py`: Core application logic and chat interface
- `vector.py`: Vector store setup and retrieval functionality
- `realistic_restaurant_reviews.csv`: Dataset containing restaurant reviews
- `requirements.txt`: Project dependencies
- `chroma_langchain_db/`: Directory for persistent vector storage

## Usage

1. Ensure you have the required CSV file with restaurant reviews in the project directory
2. Run the application:
```bash
python main.py
```
3. Start asking questions about pizza restaurants
4. Type 'q' to quit the application

## How It Works

1. The application loads restaurant reviews from a CSV file
2. Reviews are embedded using the Ollama embedding model
3. Embeddings are stored in a ChromaDB vector store
4. User questions are processed to find relevant reviews
5. The LLM generates responses based on the context and question

## Dependencies

- langchain: Framework for developing applications with LLMs
- langchain-ollama: Integration with Ollama models
- langchain-chroma: Vector store integration
- pandas: Data manipulation and CSV handling