import requests
import pandas as pd
from datetime import datetime

def buscar_dados():
    # Pega parlamentares
    url_p = "https://sapl.aquiraz.ce.leg.br/api/parlamentares/parlamentar/?format=json"
    res_p = requests.get(url_p).json()
    df_p = pd.DataFrame(res_p['results'])[['nome_parlamentar', 'sigla_partido']]

    # Pega últimas matérias (Projetos/Requerimentos)
    url_m = "https://sapl.aquiraz.ce.leg.br/api/materia/materialegislativa/?format=json"
    res_m = requests.get(url_m).json()
    df_m = pd.DataFrame(res_m['results'])[['tipo_materia_exibicao', 'ementa', 'data_apresentacao']]

    # Salva em um arquivo CSV
    df_p.to_csv("parlamentares.csv", index=False)
    df_m.to_csv("projetos.csv", index=False)
    print(f"Dados atualizados em: {datetime.now()}")

if __name__ == "__main__":
    buscar_dados()
