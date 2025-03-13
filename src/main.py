from dotenv import load_dotenv
from anthropic import Anthropic
import base64
from data_extractor import DataExtractor
load_dotenv()


client = Anthropic()
data_extractor = DataExtractor(client, model="claude-3-5-haiku-20241022", max_tokens=4096)
response = data_extractor.extract_data_from_pdf("data/input/buijze_2016.pdf")

# run main
if __name__ == "__main__":
    # content contains the actual text
    print(response["response"])

