from dotenv import load_dotenv
import os
import openai

# carrega as variáveis do arquivo .env
load_dotenv()

produto = input('Escreva caracteristicas ou dê o nome do produto a ser descrito')


openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= f"Faz uma descrição deste produto: {produto}",
  temperature=0,
  max_tokens=250,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

print(response.choices[0].text)