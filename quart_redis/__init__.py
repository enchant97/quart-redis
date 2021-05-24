import logging

from aioredis import Redis, create_redis_pool
from quart import Quart

__all__ = ["RedisHandler", "get_redis"]
__version__ = "0.1.0"


class RedisHandler:
    _connection: Redis = None
    conn_key = "REDIS_URI"

    def __init__(self, app: Quart = None):
        """
        calls init_app()

            :param app: the quart app
        """
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Quart):
        """
        get config from quart app
        then setup connection handlers

            :param app: the quart app
        """
        conn_uri = app.config[self.conn_key]

        @app.before_serving
        async def init_redis():
            RedisHandler._connection = await create_redis_pool(conn_uri)
            logging.info("Redis started")

        @app.after_serving
        async def close_redis():
            RedisHandler._connection.close()
            await RedisHandler._connection.wait_closed()
            logging.info("Redis shutdown")

    @classmethod
    def get_connection(cls) -> Redis:
        """
        get the shared redis connection
        """
        return cls._connection


def get_redis() -> Redis:
    """
    get the shared redis connection
    """
    return RedisHandler.get_connection()
