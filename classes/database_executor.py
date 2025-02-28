from sqlalchemy import create_engine
import pandas as pd

from dotenv import load_dotenv
import os

# Carrega o .env
load_dotenv(os.path.join(os.getcwd(), '.env'))


class DatabaseQueryExecutor:
    def __init__(self, database, query):
        """
        Inicializa a classe com os parâmetros necessários para a conexão e consulta.
        
        :param user: Usuário para conexão com o banco de dados.
        :param password: Senha para o usuário.
        :param host: Endereço do host do banco de dados.
        :param port: Porta do banco de dados.
        :param database: Nome do banco de dados.
        :param query: Consulta SQL a ser executada.
        """
        self.user = self.user
        self.password = self.password
        self.host = self.host
        self.port = self.port
        self.database = database
        self.query = query
        
    def _create_connection(self):
        """
        Cria e retorna a string de conexão com o banco de dados.
        """
        connection_string = f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
        engine = create_engine(connection_string)
        return engine

    def execute_query(self):
        """
        Executa a consulta SQL e retorna o resultado em um DataFrame do pandas.
        
        :return: DataFrame contendo o resultado da consulta.
        """
        engine = self._create_connection()
        try:
            # Executa a consulta SQL e carrega os resultados em um DataFrame
            result_df = pd.read_sql_query(self.query, engine)
        finally:
            # Fecha a conexão após o uso
            engine.dispose()
        
        return result_df
