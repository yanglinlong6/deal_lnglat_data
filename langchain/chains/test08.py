import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain.chains import LLMSummarizationCheckerChain
from langchain.llms import OpenAI

llm = OpenAI(temperature=0)
checker_chain = LLMSummarizationCheckerChain.from_llm(llm, verbose=True, max_checks=3)
text = "The Greenland Sea is an outlying portion of the Arctic Ocean located between Iceland, Norway, the Svalbard archipelago and Greenland. It has an area of 465,000 square miles and is one of five oceans in the world, alongside the Pacific Ocean, Atlantic Ocean, Indian Ocean, and the Southern Ocean. It is the smallest of the five oceans and is covered almost entirely by water, some of which is frozen in the form of glaciers and icebergs. The sea is named after the island of Greenland, and is the Arctic Ocean's main outlet to the Atlantic. It is often frozen over so navigation is limited, and is considered the northern branch of the Norwegian Sea."
print(checker_chain.run(text))
