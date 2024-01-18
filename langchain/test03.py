import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful socks"))
# -> '\n\nSocktastic!'
