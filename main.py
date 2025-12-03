import pandas as pd
from flask import render_template, Flask


df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv')

print(df.to_numpy())
for i in df.to_numpy():
    print(i)

tabela = df.to_numpy()[::-1]

app = Flask(__name__)
with app.app_context():
    def gerar_html_estatico():
        html_gerado = render_template('template.html', tabela=tabela)

        novo_arquivo = 'index.html'
        with open(novo_arquivo, 'w', encoding='utf-8') as f:
            f.write(html_gerado)
        
        print("HTML gerado com sucesso! Acesse o index.html")

    if __name__ == "__main__":
        try:
            gerar_html_estatico()
            
        except:
            print("Erro ao gerar o HTML")

        try:
            df.to_excel('relatorio_excel.xlsx', index=False)
            print("Excel gerado com sucesso! Acesse o relatorio_excel.xlsx")

        except:
            print("Não foi posssivel gerar o arquivo Excel")