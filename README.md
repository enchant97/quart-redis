# Quart-Redis
![PyPI](https://img.shields.io/pypi/v/quart-redis)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/quart-redis)
![PyPI - Downloads](https://img.shields.io/pypi/dm/quart-redis)
![GitHub](https://img.shields.io/github/license/enchant97/quart-redis)
![GitHub issues](https://img.shields.io/github/issues/enchant97/quart-redis)
![Lines of code](https://img.shields.io/tokei/lines/github/enchant97/quart-redis)
![GitHub last commit](https://img.shields.io/github/last-commit/enchant97/quart-redis)

A easy way of setting up a redis connection in quart.

## Requirements
- quart
- aioredis

## Example of Use
```python
from quart import Quart
from quart_redis import RedisHandler, get_redis

app = Quart(__name__)
app.config["REDIS_URI"] = "redis://localhost"
redis_handler = RedisHandler(app)

@app.route("/")
async def index():
    redis = get_redis()

    val = await redis.get("my-key", encoding="utf-8")

    if val is None:
        await redis.set("my-key", "it works!")

    return val
```
