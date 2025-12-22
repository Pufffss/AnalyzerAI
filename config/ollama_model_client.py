from autogen_ext.models.ollama import OllamaChatCompletionClient


def get_model_client():
    ollama_model_client=OllamaChatCompletionClient(
        model='llama3.2:latest'
        # model = 'deepseek-coder-v2:16b'
    )
    return ollama_model_client