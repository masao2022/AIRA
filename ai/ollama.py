import requests


class Ollama:

    def __init__(
        self,
        url="http://localhost:11434",
        model="gemma3:4b"
    ):
        self.url = url
        self.model = model


    def chat(self, message):

        data = {
            "model": self.model,
            "prompt": message,
            "stream": False
        }


        response = requests.post(
            f"{self.url}/api/generate",
            json=data
        )


        if response.status_code == 200:

            result = response.json()

            return result.get(
                "response",
                ""
            )

        else:

            return "Ollama接続エラー"