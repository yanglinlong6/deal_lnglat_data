import os

os.environ["OPENAI_API_KEY"] = "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"
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

prefix = """Answer the following questions as best you can. You have access to the following tools:"""
suffix = """When answering, you MUST speak in the following language: {language}.
 
Question: {input}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(
    tools,
    prefix=prefix,
    suffix=suffix,
    input_variables=["input", "language", "agent_scratchpad"],
)

llm_chain = LLMChain(llm=OpenAI(temperature=0), prompt=prompt)
agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools)
agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent, tools=tools, verbose=True
)
result = agent_executor.run(
    input="How many people live in canada as of 2023?", language="italian"
)

print(result)
