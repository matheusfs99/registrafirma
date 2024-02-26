import requests


def consult_cnpj(cnpj):
    response = requests.get(f"https://receitaws.com.br/v1/cnpj/{cnpj}")
    return response.json(), response.status_code
