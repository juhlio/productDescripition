from dotenv import load_dotenv
import os
import openai

# carrega as variáveis do arquivo .env
load_dotenv()

class Search:

    def __init__(self, product):
        self.product = product


    def get_description(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Faz uma descrição deste produto: {self.product}",
            temperature=0,
            max_tokens=250,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        produto = {"name": self.product, "description": response.choices[0].text}
        return produto


    def __str__(self):
        return self.product