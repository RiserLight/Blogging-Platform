
import os

def get_conn_str():
  return f"""
  dbname={os.environ.get('POSTGRES_DB',"postgres")}
  user={os.environ.get('POSTGRES_USER',"postgres")}
  password={os.environ.get('POSTGRES_PASSWORD',"Mysql")}
  host={os.environ.get('POSTGRES_HOST',"localhost")}
  port={os.environ.get('POSTGRES_PORT',5432)}
  """