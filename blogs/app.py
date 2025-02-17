import asyncio
import logging
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI , Request
from psycopg_pool import AsyncConnectionPool
from utils.constants import SERVICE_NAME
from utils.db_setup import get_conn_str

# Setup logger
logger=logging.getLogger("uvicorn")
# Setupm lifespan events
@asynccontextmanager
async def life_span(app:FastAPI):
  logger.info("Application going to be started")
  app.async_pool=AsyncConnectionPool(conninfo=get_conn_str())
  yield
  logger.info("Application going to be closed")
  app.async_pool.close()


app=FastAPI(
  docs_url=f'/v1/{SERVICE_NAME}/docs',
  title='Personal Blogging Application',
  description='A webapp for simple blogging applications',
  version='1.0.0',
  lifespan=life_span
)

# Add necessary middlewares


# Add necessary routes


# Add global exception handler

# main 

# Default health check route

@app.get('/')
async def health_cheack():
  return {'msg':'Server is healthy'}

if __name__=="__main__":
  uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)