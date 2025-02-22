from quart import Quart

from quart_redis import RedisHandler, get_redis


def create_app():
    app = Quart(__name__)
    app.config["REDIS_URI"] = "redis://localhost"
    redis_handler = RedisHandler(app)

    @app.get("/get-msg")
    async def get_msg():
        r = redis_handler.get_connection()
        return await r.get("msg")

    @app.get("/get-msg/with-context")
    async def get_msg_with_context():
        r = get_redis()
        return await r.get("msg")

    @app.post("/set-msg")
    async def set_msg():
        r = redis_handler.get_connection()
        await r.set("msg", "Hello World")
        return ""

    return app
