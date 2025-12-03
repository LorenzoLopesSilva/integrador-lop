import pandas as pd
from flask import render_template, request, redirect, url_for, session, Flask
import requests

df = pd.read_csv('LOPAL-ProjetoIntegrador-Esp8266_Receiver.csv')

print(df.to_numpy())
for i in df.to_numpy():
    print(i)

tabela = df.to_numpy()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tabela = tabela)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# url = 