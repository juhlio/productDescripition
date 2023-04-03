from dotenv import load_dotenv
import os
import openai
from openpyxl import Workbook, load_workbook

filename = './src/Produtos.xlsx'
wb = load_workbook(filename = filename)
ws = wb.active

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
        proxima_linha = ws.max_row + 1
        ws.cell(row=proxima_linha, column=1).value = self.product
        ws.cell(row=proxima_linha, column=2).value = response.choices[0].text
        wb.save(filename=filename)
        return produto


    # def __str__(self):
    #     return self