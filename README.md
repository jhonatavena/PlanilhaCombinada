# PlanilhaCombinada

Este é um projeto Python que permite unificar informações de duas planilhas do Excel, removendo duplicatas com base em um campo-chave. O resultado é uma nova planilha consolidada.

## Uso

1. Certifique-se de ter o Pandas instalado em seu ambiente Python.
   
   pip install pandas
   

2. Execute o código Python fornecido, que lê as planilhas, remove duplicatas com base em um campo específico e cria uma nova planilha unificada.

```python
import pandas as pd

# Carregue a planilha original
df = pd.read_excel("planilha_compilado.xlsx")

# Remova duplicatas com base no campo 'Número do Processo'
df_sem_duplicatas = df.drop_duplicates(subset=['Número do Processo'])

# Salve a nova planilha unificada
df_sem_duplicatas.to_excel('compilado_atualizado.xlsx', index=False)
```

3. O resultado será uma nova planilha, `compilado_atualizado.xlsx`, contendo os dados consolidados.

## Contribuições

Contribuições são bem-vindas! Se você deseja contribuir com melhorias neste projeto, sinta-se à vontade para abrir uma solicitação de pull.


---

**Observação:** Certifique-se de ajustar os caminhos de arquivo e o código conforme necessário para corresponder à sua estrutura de diretório e aos nomes dos arquivos.

