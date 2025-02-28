# Bibliotecas
import pandas as pd 
import sys
import os
# Adiciona ao sys.path o diretório acima de `src`
sys.path.append(r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\02.01.simulador_politica\classes")
from database_executor import DatabaseQueryExecutor



# Dados CRL
database = "inteligencia_credito_dados"
query_file_path = r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\02.01.simulador_politica\data\Consultas\crl.sql"
# Lê o conteúdo do arquivo SQL
with open(query_file_path, 'r') as file:
    query = file.read()
# Criação de uma instância da classe
db_executor = DatabaseQueryExecutor(database, query)
resultado = db_executor.execute_query()
resultado.to_parquet(r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\02.01.simulador_politica\data\database\crl.parquet")  

# Dados CRL
database = "inteligencia_credito_dados"
query_file_path = r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\02.01.simulador_politica\data\Consultas\scr.sql"
# Lê o conteúdo do arquivo SQL
with open(query_file_path, 'r') as file:
    query = file.read()
# Criação de uma instância da classe
db_executor = DatabaseQueryExecutor(database, query)
resultado = db_executor.execute_query()
resultado.to_parquet(r"C:\Users\fabio.varriano\OneDrive - Sicoob\01_2025\fabrica_de_limites\02.01.simulador_politica\data\database\scr.parquet")  