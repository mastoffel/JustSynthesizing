from dotenv import load_dotenv
from anthropic import Anthropic
import base64

load_dotenv()

# read pdf file
with open("data/input/Weiss_et_al_2017_data_avail.pdf", "rb") as f:
    pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")

client = Anthropic()
message = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=[
        {
            "role": "user", 
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "base64",
                        "media_type": "application/pdf",
                        "data": pdf_data
                    }
                },
            {
                "type": "text",
                    "text": "Make a table of the estimated repeatabilities (ICC's) in the paper, with trait, estimate, ci if available and sample size."
                }
            ]
        }
    ]
)

# run main
if __name__ == "__main__":
    # content contains the actual text
    print(message.content[0].text)

