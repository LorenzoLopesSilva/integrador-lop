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
        
        print("HTML gerado com sucesso. Acesse o index.html")

    if __name__ == "__main__":
        gerar_html_estatico()