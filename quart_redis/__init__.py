import logging

from aioredis import Redis, from_url
from quart import Quart

__all__ = ["RedisHandler", "get_redis"]
__version__ = "1.0.0"


class RedisHandler:
    _connection: Redis = None
    conn_key = "REDIS_URI"

    def __init__(self, app: Quart = None, **kwargs):
        """
        calls init_app() automatically,
        with any given kwargs if app is given.

            :param app: the quart app, defaults to None
            :param **kwargs: pass arguments to init_app()
        """
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: Quart, *, encoding="utf8", decode_responses=True, **kwargs):
        """
        get config from quart app
        then setup connection handlers.

            :param app: the quart app
            :param encoding: optional encoding to use, defaults to "utf8"
            :param decode_responses: optional decode_responses, defaults to True
            :param **kwargs: pass any further arguments to redis
        """
        conn_uri = app.config[self.conn_key]

        @app.before_serving
        async def init_redis():
            RedisHandler._connection = from_url(
                conn_uri,
                encoding=encoding,
                decode_responses=decode_responses,
                **kwargs
            )
            logging.info("Redis started")

        @app.after_serving
        async def close_redis():
            await RedisHandler._connection.close()
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
