import time
from src import OllamaClient


# Helper class to manage chat session and response generation
class ChatSessionManager:
    def __init__(self):
        self.ollama_client = OllamaClient()

    def response_generator(self, prompt):
        start_time = time.time()

        for chunk in self.ollama_client.stream(prompt):
            yield chunk

        total_time_elapsed = time.time() - start_time
        yield f"\n\n---\n⏱️ Elapsed Time: {total_time_elapsed:.2f} seconds\n"
