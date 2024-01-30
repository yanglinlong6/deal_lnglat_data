import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful socks"))
# -> '\n\nSocktastic!'
