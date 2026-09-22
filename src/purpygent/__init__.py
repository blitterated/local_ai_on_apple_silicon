from openai import OpenAI


def main() -> None:
    step1()


def step1() -> None:
    client = OpenAI()

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
