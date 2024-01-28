import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain.chains import (LLMChain, OpenAIModerationChain, SequentialChain,
                              SimpleSequentialChain)
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

moderation_chain = OpenAIModerationChain()
moderation_chain.run("This is okay")
moderation_chain.run("I will kill you")
