import requests
import pandas as pd
from datetime import datetime

def buscar_dados():
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # 1. URLs da API (Garantindo o formato JSON)
# Adicionamos '&page_size=100' para pegar todos de uma vez
    url_p = "https://sapl.aquiraz.ce.leg.br/api/parlamentares/parlamentar/?format=json&page_size=100"
    url_m = "https://sapl.aquiraz.ce.leg.br/api/materia/materialegislativa/?format=json&page_size=100"

    try:
        # Coletando Parlamentares
        res_p = requests.get(url_p, headers=headers).json()
        # Se 'results' não existir, ele cria uma lista vazia e não trava o programa
        dados_p = res_p.get('results', [])
        df_p = pd.DataFrame(dados_p)
        
        # Coletando Matérias
        res_m = requests.get(url_m, headers=headers).json()
        dados_m = res_m.get('results', [])
        df_m = pd.DataFrame(dados_m)

        # Salva os arquivos (mesmo que vazios, para o Power BI não dar erro)
        df_p.to_csv("parlamentares.csv", index=False, encoding='utf-8-sig')
        df_m.to_csv("projetos.csv", index=False, encoding='utf-8-sig')
        
        print(f"Sucesso! Atualizado em: {datetime.now()}")

    except Exception as e:
        print(f"Erro detalhado: {e}")
        # Cria arquivos vazios para evitar erro no GitHub Actions
        pd.DataFrame().to_csv("parlamentares.csv")
        pd.DataFrame().to_csv("projetos.csv")

if __name__ == "__main__":
    buscar_dados()
