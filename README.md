# Quart-Redis
[![Documentation Status](https://readthedocs.org/projects/quart-redis/badge/?version=latest)](https://quart-redis.readthedocs.io/en/latest/)
![PyPI](https://img.shields.io/pypi/v/quart-redis)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/quart-redis)
![PyPI - Downloads](https://img.shields.io/pypi/dm/quart-redis)
![GitHub](https://img.shields.io/github/license/enchant97/quart-redis)
![GitHub issues](https://img.shields.io/github/issues/enchant97/quart-redis)
![Lines of code](https://img.shields.io/tokei/lines/github/enchant97/quart-redis)
![GitHub last commit](https://img.shields.io/github/last-commit/enchant97/quart-redis)

An easy way of setting up a redis connection in quart.

## Requirements
- quart
- aioredis

## Example of Use
```
pip install quart-redis
```

```python
from quart import Quart
from quart_redis import RedisHandler, get_redis

app = Quart(__name__)
app.config["REDIS_URI"] = "redis://localhost"
redis_handler = RedisHandler(app)

@app.route("/")
async def index():
    redis = get_redis()

    val = await redis.get("my-key")

    if val is None:
        await redis.set("my-key", "it works!")
        val = await redis.get("my-key")

    return val
```
