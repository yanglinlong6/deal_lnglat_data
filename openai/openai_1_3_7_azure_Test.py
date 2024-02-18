from openai import AzureOpenAI

# gets the API Key from environment variable AZURE_OPENAI_API_KEY
client = AzureOpenAI(
    # https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#rest-api-versioning
    api_version="2023-07-01-preview",
    # https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal#create-a-resource
    azure_endpoint="https://glsk-openai-ce.openai.azure.com",
    api_key="8ba61036fe7847c7be4ebaaf58b85275"
)

completion = client.chat.completions.create(
    model="gpt-35-turbo-1106",  # e.g. gpt-35-instant
    messages=[
        {
            "role": "user",
            "content": "帮我生成2条续保营销文案，每条不超过12个字，输出json格式",
        },
    ],
)
print(completion.usage)
print(completion.choices[0].message.content)
print(completion.model_dump_json(indent=2))