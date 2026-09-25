from openai import OpenAI
import purpygent

client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key=purpygent.get_api_key()
)

# Message roles:
#   user:      a prompt/query from a human user.
#   assistant: a response from the LLM.
#   system:    something that should be loaded and understood by the LLM at start of session.
messages = []

while True:
    user_input = input("You> ")
    if user_input.strip().lower() in ("exit", "quit"):
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="Llama-3.2-3B-Instruct-8bit",
        messages=messages,
    )

    bot_output = response.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_output})
    print("Bot> ", bot_output)
