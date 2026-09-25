from openai import OpenAI
import purpygent

client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key=purpygent.get_api_key()
)

while True:
    user_input = input("You> ")
    if user_input.strip().lower() in ("exit", "quit"):
        break

    response = client.chat.completions.create(
        model="Llama-3.2-3B-Instruct-8bit",
        messages=[{"role": "user", "content": user_input}],
    )

    bot_output = response.choices[0].message.content
    print("Bot> ", bot_output)
