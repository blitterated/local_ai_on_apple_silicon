from openai import OpenAI


def main() -> None:
    step1()


def step1() -> None:
    client = OpenAI()

    response = client.chat.completions.create(
        model="Llama-3.2-3B-Instruct-8bit",
        messages=[
            {"role": "user", "content": "Explain what an AI agent is in one sentence."},
        ],
    )

    print(response.choices[0].message.content)
