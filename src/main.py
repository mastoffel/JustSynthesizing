from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()

client = Anthropic()

message = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Translate the poem Mondnacht to English."}
    ]
)

# run main
if __name__ == "__main__":
    # content contains the actual text
    print(message.content[0].text)

