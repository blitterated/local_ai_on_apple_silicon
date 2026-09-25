from openai import OpenAI
import purpygent

client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key=purpygent.get_api_key()
)

response = client.chat.completions.create(
    model="Llama-3.2-3B-Instruct-8bit",

    messages=[
        {"role": "user", "content": "Explain what an AI agent is in one sentence."},
    ],
)

print(response.choices[0].message.content)
