# Ollama Client Connector
import os
from typing import Iterator, Optional

import ollama
from dotenv import load_dotenv

load_dotenv()

class OllamaClient:
    def __init__(self, model: Optional[str] = None):
        self.llm_model = model or os.getenv("LLM_MODEL", "llama3.2")

    def request(self, prompt):
        try:
            # Generate the response
            response = ollama.chat(
                model=self.llm_model,
                messages=[
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            )

            return {"content": response['message']['content'], "total_duration": response['total_duration']}
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def stream(self, prompt: str) -> Iterator[str]:
        """Stream response chunks from Ollama as they are generated."""
        try:
            stream = ollama.chat(
                model=self.llm_model,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
            )
            for chunk in stream:
                content = chunk.get("message", {}).get("content", "")
                if content:
                    yield content
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
