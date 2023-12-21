# pip install -q transformers
from transformers import pipeline

checkpoint = "LaMini-Flan-T5-248M"

print("Loading the model!!")
model = pipeline('text2text-generation', model = checkpoint)

while True:
    user_input = input("Enter your input here!!")
    generated_text = model(user_input, max_length=512, do_sample=True)[0]['generated_text']
    print("Response", generated_text)
