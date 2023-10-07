import pandas as pd

df = pd.read_excel("C:\\Users\\jhona\\planilha_compilado.xlsx")

df_sem_duplicatas = df.drop_duplicates(subset=['Número do Processo'])

df_sem_duplicatas.to_excel('compilado_atualizado.xlsx', index=False)

print(df_sem_duplicatas)
