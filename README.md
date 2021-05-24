# Quart-Redis
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
