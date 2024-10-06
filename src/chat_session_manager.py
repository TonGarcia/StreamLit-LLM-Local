import time
from src import OllamaClient


# Helper class to manage chat session and response generation
class ChatSessionManager:
    def __init__(self):
        self.ollama_client = OllamaClient()

    def response_generator(self, prompt):
        start_time = time.time()

        # Request the response from Ollama
        response = self.ollama_client.request(prompt)
        full_response = response["content"]
        elapsed_time = response["total_duration"]

        # Simulate typing effect by yielding chunks of the response
        chunk_size = 5
        for i in range(0, len(full_response), chunk_size):
            yield full_response[i:i + chunk_size]
            time.sleep(0.05)

        # Calculate total time taken
        total_time_elapsed = time.time() - start_time
        yield f"\n\n---\n⏱️ Elapsed Time: {total_time_elapsed:.2f} seconds\n"
