![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/gerenciado%20com-uv-purple)
![License](https://img.shields.io/badge/license-MIT-green)

> Projeto de busca de endereços por CEPs utilizando Python

O projeto utiliza python com a biblioteca `requests` para buscar os endereços correspondentes aos CEPs via API, podendo ou não salvar os resultados em um arquivo JSON.

Através da biblioteca `argparse`, é possível buscar os endereços apenas digitando os CEPs através do terminal:

```bash
uv run busca-cep 66640365
```
ou
```bash
uv run busca-cep 68600000 66640365 -o data/enderecos.json
```