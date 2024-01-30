import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain.chains import LLMChain, LLMRequestsChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

template = """Between >>> and <<< are the raw search result text from google.
Extract the answer to the question '{query}' or say "not found" if the information is not contained.
Use the format
Extracted:<answer or "not found">
>>> {requests_result} <<<
Extracted:"""

PROMPT = PromptTemplate(
    input_variables=["query", "requests_result"],
    template=template,
)

chain = LLMRequestsChain(llm_chain=LLMChain(llm=OpenAI(temperature=0), prompt=PROMPT))
question = "What are the Three (3) biggest countries, and their respective sizes?"
inputs = {
    "query": question,
    "url": "https://www.google.com/search?q=" + question.replace(" ", "+"),
}

print(chain(inputs))
