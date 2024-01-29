from clickhouse_driver import Client


class ClickhouseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClickhouseConnection, cls).__new__(cls)
            cls._instance.client = None
        return cls._instance

    def connect(self, host='localhost', port=None, user=None, password=None, database=None):
        if host != 'localhost' and port and user and password and database:
            self.client = Client(host=host, port=port, user=user, password=password, database=database)
        else:
            self.client = Client(host=host)

    def execute_query(self, query):
        if not self.client:
            raise RuntimeError("ClickHouse client is not connected. Use connect method first.")
        return self.client.execute(query)
