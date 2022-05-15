from src.settings.models import DatabaseConfig
from os import environ as env

db_driver = env.get('db_driver', 'postgresql')
db_host = env.get('db_host', '127.0.0.1')
db_username = env.get('db_user', 'postgres')
db_password = env.get('db_password', 'password')
db_port = int(env.get('db_port', '5432'))
db_name = env.get('db_name', 'postgres')

db_config = DatabaseConfig(
    driver=db_driver,
    host=db_host,
    username=db_username,
    password=db_password,
    port=db_port,
    name=db_name)