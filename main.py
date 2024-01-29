from fastapi import FastAPI
from clickhouse_connection import ClickhouseConnection
from fastapi.responses import HTMLResponse
from models.models import RegistrationData
import json



from clickhouse_driver import Client

app = FastAPI()
    
clickhouse_conn = ClickhouseConnection()
clickhouse_conn.connect()
print(clickhouse_conn.execute_query("SHOW TABLES FROM default;"))
clickhouse_conn.execute_query("INSERT INTO example_table(id, name, age) VALUES (1, 'name', '10')")
print(clickhouse_conn.execute_query("SELECT * FROM example_table"))
print(clickhouse_conn.execute_query("DESCRIBE TABLE example_table"))

@app.get("/")
async def get_index():
    with open("views/index.html", "r") as file:
        file_content = file.read()
    return HTMLResponse(content=file_content)


@app.get("/create")
async def create_client(data: RegistrationData):
    #clickhouse_conn.execute_query("INSERT INTO example_table () VALUES ()")
    return