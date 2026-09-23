import subprocess
from openai import OpenAI


def main() -> None:
    key_path = "API/oMLX/api_key"
    api_key = get_api_key(key_path)
    step1(api_key)


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


def step1(api_key) -> None:
    client = OpenAI(
        base_url="http://127.0.0.1:8000/v1",
        api_key=api_key
    )

    response = client.chat.completions.create(
        model="Llama-3.2-3B-Instruct-8bit",

        # Message roles:
        #   user:      a prompt/query from a human user.
        #   assistant: a response from the LLM.
        #   system:    something that should be loaded and understood by the LLM at start of session.
        messages=[
            {"role": "user", "content": "Explain what an AI agent is in one sentence."},
        ],
    )

    print(response.choices[0].message.content)
