import json
from openai import OpenAI
import purpygent
import pprint


client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key=purpygent.get_api_key()
)


def read_file(path):
    with open (path, "r", encoding="utf-8") as f:
        return f.read()


TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a text file and return its contents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path of the file to read.",
                    },
                },
                "required": ["path"],
            },
        },
    },
]


messages=[
    {"role": "user", "content": "What is inside step_3_notes.txt? Summarize it in one line."},
]


while True:
    response = client.chat.completions.create(
        model="Qwen3.5-9B-MLX-8bit",
        messages=messages,
        tools=TOOL_SCHEMAS,
    )
    # Here, instead of just appending content, we're appending the whole message.
    response_msg = response.choices[0].message
    pprint.pprint(response_msg)
    messages.append(response_msg)


    # No tool calls means the model finished and gave us an answer.
    if not response_msg.tool_calls:
        print(response_msg.content)
        break


    for tool_call in response_msg.tool_calls:
        args = json.loads(tool_call.function.arguments)
        print(f"Model wants to run: read_file({args})")

        result = read_file(**args)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result,
        })
