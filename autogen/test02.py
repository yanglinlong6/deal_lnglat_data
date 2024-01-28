from autogen import UserProxyAgent, ConversableAgent, config_list_from_json
import os

os.environ["OPENAI_API_KEY"] = "sk-CJ6T1HaR1ODHNHXc00Bd3fD7357c424fAa1868570c593102"


def main():
    # Load LLM inference endpoints from an env variable or a file
    # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    # and OAI_CONFIG_LIST_sample.
    # For example, if you have created a OAI_CONFIG_LIST file in the current working directory, that file will be used.
    config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

    # Create the agent that uses the LLM.
    assistant = ConversableAgent(
        "agent",
        llm_config={"config_list": config_list},
        code_execution_config={"work_dir": ".", "use_docker": False},
    )

    # Create the agent that represents the user in the conversation.
    user_proxy = UserProxyAgent(
        "user",
        code_execution_config={"work_dir": ".", "use_docker": False},
    )

    # Let the assistant start the conversation.  It will end when the user types exit.
    assistant.initiate_chat(user_proxy, message="How can I help you today?")


if __name__ == "__main__":
    main()
