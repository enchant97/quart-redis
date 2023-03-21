import logging
from typing import Optional

from quart import Quart
from redis.asyncio import Redis, from_url

__all__ = ["RedisHandler", "get_redis"]
__version__ = "1.0.0"

logger = logging.getLogger(__name__)


class RedisNotInitialized(Exception):
    pass


class RedisHandler:
    _connection: Optional[Redis] = None
    conn_key = "REDIS_URI"

    def __init__(self, app: Optional[Quart] = None, **kwargs):
        """
        calls init_app() automatically,
        with any given kwargs if app is given.

            :param app: the quart app, defaults to None
            :param **kwargs: pass arguments to init_app()
        """
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app: Quart, **kwargs):
        """
        get config from quart app
        then setup connection handlers.

            :param app: the quart app
            :param **kwargs: pass any further arguments to redis
        """
        conn_uri = app.config[self.conn_key]

        @app.before_serving
        async def init_redis():
            RedisHandler._connection = from_url(
                conn_uri,
                **kwargs
            )
            logger.info("Redis started")

        @app.after_serving
        async def close_redis():
            if RedisHandler._connection is not None:
                await RedisHandler._connection.close()
                logger.info("Redis shutdown")

    @classmethod
    def get_connection(cls) -> Redis:
        """
        get the shared redis connection

            :raises RedisNotInitialized: if redis has not been initialized
        """
        if cls._connection is None:
            raise RedisNotInitialized("Redis has not been initialized")
        return cls._connection


def get_redis() -> Redis:
    """
    get the shared redis connection

        :raises RedisNotInitialized: if redis has not been initialized
    """
    return RedisHandler.get_connection()
