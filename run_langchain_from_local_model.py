from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain
from transformers import pipeline

checkpoint = "LaMini-Flan-T5-248M"
model_pipeline = pipeline('text2text-generation', 
    model = checkpoint, 
    max_length=512
)

llm = HuggingFacePipeline(
    pipeline=model_pipeline,
)

template = """
You are a friendly chatbot assistant that responds conversationally to users' questions.
Keep the answers short, unless specifically asked by the user to elaborate on something.

Question: {question}

Answer:"""

prompt = PromptTemplate(template=template, input_variables=["question"])
question = "What is the capital of India"
llm_chain = LLMChain(prompt=prompt, llm=llm)
res = llm_chain.run(question=question)
print(res)

while True:
    user_input = input("Ask your question here!!!")
    res = llm_chain.run(question=user_input)
    print(res)
