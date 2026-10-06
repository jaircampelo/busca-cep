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