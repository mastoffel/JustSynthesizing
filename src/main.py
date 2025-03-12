import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": "Translate Heinrich Heine's poem 'Die Lorelei' to English."}
    ]
)

# run main
if __name__ == "__main__":
    print(message.content)

