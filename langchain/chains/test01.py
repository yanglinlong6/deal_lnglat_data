import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain.chains import APIChain
from langchain.chains.api.prompt import API_RESPONSE_PROMPT
from langchain.llms import OpenAI
from langchain.prompts.prompt import PromptTemplate

llm = OpenAI(temperature=0)

from langchain.chains.api import open_meteo_docs

chain_new = APIChain.from_llm_and_api_docs(
    llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=True
)
chain_new.run(
    "What is the weather like right now in Munich, Germany in degrees Farenheit?"
)
