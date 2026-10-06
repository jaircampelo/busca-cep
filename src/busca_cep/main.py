import requests
import json
import argparse
import os

def busca_enderecos(ceps:list, path:str | None = None):
    """
    Busca endereços a partir de uma lista de CEPs e retorna um arquivo json no caminho especificado.
    """
    enderecos = []
    for cep in ceps:
        url = f"https://cep.awesomeapi.com.br/json/{cep}"
        resp = requests.get(url=url)
        if resp.status_code == 200:
            data = resp.json()
            enderecos.append(data)
        else:
            print(f"Erro na requisição do CEP: {cep}. Erro: {resp.status_code}")

    if path:
        pasta = os.path.dirname(path)
        if pasta:
            os.makedirs(pasta, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(enderecos, f, ensure_ascii=False, indent=4)
        print(f"Arquivo salvo em: {path}")
    else:
        print(json.dumps(enderecos, ensure_ascii=False, indent=4))

    return enderecos

def main():
    # Criando um parser de argumentos para a linha de comando
    parser = argparse.ArgumentParser(description="Busca endereços a partir de CEPs no formato 00000000 e retorna um json com os endereços encontrados.")
    parser.add_argument("ceps", nargs="+", help="CEPs a serem consultados. Exemplo: 66640365 68600000 66645455")
    parser.add_argument("-o", "--output", default=None, help="Caminho do arquivo de saída. Se não for especificado, aparece no terminal.)")
    args = parser.parse_args()
    busca_enderecos(ceps=args.ceps, path=args.output)

if __name__ == "__main__":
    main()