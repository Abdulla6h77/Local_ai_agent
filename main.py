from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="llama3")

template = """
You are an expert in answering questions about pizza restaurants.
You have been working in the pizza industry for 10 years.
You have visited over 100 different pizza restaurants in your lifetime.
You have a deep understanding of the pizza industry and can answer any question about it.
You have a knowledge about what type of reviews people have given. 
Here are some examples of reviews that people have given about pizza restaurants in the past: {review}
And here are some of the most common types of questions that people ask: {question}
"""

prompts = ChatPromptTemplate.from_template(template)
chain = prompts | model

while True:
    print("\n\n-------------------------------" )
    question = input("Ask your question?")
    print("\n\n" )
    if question == "q":
        break

    reviews = retriever.invoke(question)
    result = chain.invoke({'review': [], 'question': question})
    print(result)
