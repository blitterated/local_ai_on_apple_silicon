import subprocess
from openai import OpenAI


def main() -> None:
    key_path = "API/oMLX/api_key"
    api_key = get_api_key(key_path)

    #step_1__single_api_call(api_key)
    #step_2__track_conversation(api_key)
    step_2b__broken_conversation(api_key)
    #step_3__call_tools


def get_api_key(key_path) -> String:
    try:
        result = subprocess.run(
            ["gopass", "show", "-o", key_path],
            capture_output=True,
            text=True,
            check=True
        )

        api_key = result.stdout.strip()
        return api_key

    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"gopass failed for '{key_path}': {e.stderr.strip()}")


def step_1__single_api_call(api_key) -> None:
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="Llama-3.2-3B-Instruct-8bit",

        messages=[
            {"role": "user", "content": "Explain what an AI agent is in one sentence."},
        ],
    )

    print(response.choices[0].message.content)


def step_2__track_conversation(api_key) -> None:
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key=api_key
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


def step_2b__broken_conversation(api_key) -> None:
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key=api_key
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
