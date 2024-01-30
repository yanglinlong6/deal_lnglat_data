import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"
# openai.api_base = "https://oneapi.365jpshop.com/v1"
os.environ["OPENAI_API_BASE"] = "https://oneapi.365jpshop.com/v1"
os.environ[
    "SERPAPI_API_KEY"
] = "da8433eda3fc4629422e903b0b7eb9f642b1a5297a429b281ac7e1dc12c26042"

from langchain.agents import ZeroShotAgent, Tool, AgentExecutor
from langchain import OpenAI, SerpAPIWrapper, LLMChain

search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="useful for when you need to answer questions about current events",
    )
]

prefix = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:"""
suffix = """Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Args"
 
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools, prefix=prefix, suffix=suffix, input_variables=["input", "agent_scratchpad"]
)

print(prompt.template)

llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
tool_names = [tool.name for tool in tools]
agent = ZeroShotAgent(llm_chain=llm_chain, allowed_tools=tool_names)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True
)
print(agent_executor.run("How many people live in canada as of 2023?"))
