import os
import PySimpleGUI as sg
from search import Search
from sheet import sheet

cabecalho = ['Produto', 'Descrição']
dados = []

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Escreva caracteristicas ou dê o nome do produto a ser descrito')],
          [sg.Text('Produto'), sg.InputText(),sg.Button('Ok')],
          [sg.Text('Produtos com a descrição pronta')],
          [sg.Table(values=dados, headings=cabecalho, max_col_width=200,
                    col_widths=[40, 150], expand_x=True, justification='left', key='-TABELA-')],
          [sg.Button('Abrir Planilha com as Descrições')]
          ]

window = sg.Window('Descrição de Produtos', layout)

planilha = sheet()
print(planilha)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    if event == 'Ok':
        print('You entered ', values[0])
        produto = Search(values[0])
        descricao = produto.get_description(planilha)
        print(produto)
        dados.append([produto, descricao])
        window['-TABELA-'].update(values=dados)
        print(dados)
    if event == 'Abrir Planilha com as Descrições':
        caminho_absoluto = os.path.abspath('./src')
        caminho_arquivo = os.path.join(caminho_absoluto, planilha.name)
        os.startfile(caminho_arquivo)

window.close()
