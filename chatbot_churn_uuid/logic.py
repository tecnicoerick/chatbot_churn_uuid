
import json
import re

DATASET_PATH = 'data/dataset.json'

def consultar_cliente_por_uuid(texto):
    match = re.search(r'uuid=([a-fA-F0-9\-]+)', texto)
    if not match:
        return {"erro": "Formato inválido. Use: uuid=<valor>"}

    uuid_busca = match.group(1)

    with open(DATASET_PATH, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    for row in dados:
        if row['uuid'] == uuid_busca:
            return {
                "status": "Cliente encontrado",
                "UUID": row["uuid"],
                "Probabilidade de Churn": row["probabilidade_churn"],
                "Predição Final": row["predicao_final"],
                "Classificação de Risco": row["classificacao_risco"],
                "Modelo utilizado": row["modelo"],
                "Threshold aplicado": row["threshold"],
                "Data da predição": row["data_predicao"]
            }

    return {"erro": "UUID não encontrado"}
