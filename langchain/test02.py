import os

os.environ["OPENAI_API_KEY"] = "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"
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
text = "What would be a good company name for a company that makes colorful socks?"
# print(llm(text))

from langchain.prompts import PromptTemplate
 
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
print(prompt.format(product="colorful socks"))
