
import os

def get_conn_str():
  return f"""
  dbname={os.environ.get('POSTGRES_DB',None)}
  user={os.environ.get('POSTGRES_USER',None)}
  password={os.environ.get('POSTGRES_PASSWORD',None)}
  host={os.enviorn.get('POSTGRES_HOST',None)}
  port={os.environ.get('POSTGRES_PORT',5432)}
  """