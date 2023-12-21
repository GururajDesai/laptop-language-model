from langchain.llms import HuggingFacePipeline
from langchain import PromptTemplate, LLMChain

model_id = "MBZUAI/LaMini-Flan-T5-248M"
llm = HuggingFacePipeline.from_model_id(
    model_id=model_id,
    task="text2text-generation",
    model_kwargs={"temperature": 0, "max_length": 500}
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
