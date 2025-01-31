# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="LL-5aiQHBXbfEXEkYKdeNUyoIuTM5rlv4Mvxx3nQuCLNzMJOrHJg0FGxIoQL6LEP4Bn", base_url="https://api.llama-api.com")

response = client.chat.completions.create(
    model="llama3.1-70b",
    messages=[
        {"role": "system", "content": "You are a toxic assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)