import base64
import os
from typing import Dict, Any, List, Optional
from anthropic import Anthropic


class DataExtractor:
    """Extract data for meta-analysis from papers using LLMs."""

    def __init__(self, client: object, model: str = "claude-3-5-haiku-20241022",
                 max_tokens: int = 4096):
        """Initialize the DataExtractor with the given model and max tokens.
        
        Args:
            client (object): The Anthropic client object.
            model (str): The model to use for the extraction.
            max_tokens (int): The maximum number of tokens in the response.
        """
        self.client = client
        self.model = model
        self.max_tokens = max_tokens
        
    def extract_data_from_pdf(self, file_path: str) -> Dict[str, Any]:
        """Extract meta-analysis data from a PDF file.
        
        Args:
            file_path (str): The path to the PDF file.
            
        Returns:
            Dict[str, Any]: A dictionary containing the extracted data.
        """
        try:
            with open(file_path, "rb") as f:
                pdf_data = base64.standard_b64encode(f.read()).decode("utf-8")
                
            file_name = os.path.basename(file_path)
            
            message = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
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
                                "text": """
                                The meta-analysis is about the effect of cold water on health. 
                                Extract and organize the following information from this paper in JSON format:
                                1. Study metadata (title, year)
                                2. All effect sizes relevant for the meta-analysis. For each effect size, extract the following information,
                                if not available, leave blank:
                                    - Effect size
                                    - Effect size type (correlation, linear model estimate, etc.)
                                    - Sample size
                                    - Outcome measures
                                    - Notes
                                Format your response as a valid JSON object only, no explanation text.
                                """
                            }
                        ]
                    }
                ]
            )
            
            return {
                "file_name": file_name,
                "file_path": file_path,
                "response": message.content[0].text
            }
            
        except Exception as e:
            return {
                "file_name": file_name,
                "file_path": file_path,
                "error": str(e)
            }
        
        
        
        
        
        
        
        
        