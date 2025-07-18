from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def summarize(text):
    input_text = "summarize: " + text.strip().replace("\n", " ")
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(input_ids, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

input_text = """
Artificial Intelligence is a branch of computer science that aims to create machines that can perform tasks that typically require human intelligence. 
These tasks include reasoning, learning, problem-solving, perception, and language understanding. AI is categorized into narrow AI, which is designed 
to perform a narrow task, and general AI, which performs any intellectual task a human can. AI techniques include machine learning, deep learning, and
natural language processing. Over the years, AI has been integrated into various sectors such as healthcare, finance, automotive, and customer service. 
It helps improve productivity, reduce human error, and automate repetitive tasks. However, the ethical implications and potential job displacement caused 
by AI continue to be major concerns among policymakers and researchers."""

summary = summarize(input_text)
print("Original Text:\n", input_text)
print("\nSummary:\n", summary)
