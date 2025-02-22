# Quart-Redis
[![Documentation Status](https://readthedocs.org/projects/quart-redis/badge/?version=latest)](https://quart-redis.readthedocs.io/en/latest/)
![PyPI](https://img.shields.io/pypi/v/quart-redis)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/quart-redis)
![PyPI - Downloads](https://img.shields.io/pypi/dm/quart-redis)
![GitHub](https://img.shields.io/github/license/enchant97/quart-redis)
![GitHub issues](https://img.shields.io/github/issues/enchant97/quart-redis)
![GitHub last commit](https://img.shields.io/github/last-commit/enchant97/quart-redis)

An easy way of setting up a redis connection in quart.

> View the docs [here](https://quart-redis.readthedocs.io/en/latest/).

## Requirements
- quart ~= 0.20
- redis >= 5.2.1, < 6

## Example

```python
# file: app.py
from quart import Quart
from quart_redis import RedisHandler, get_redis

app = Quart(__name__)
app.config["REDIS_URI"] = "redis://localhost"
# override default connection attempts, set < 0 to disable
# app.config["REDIS_CONN_ATTEMPTS"] = 3
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

## Testing
Due to quart_redis using `before_serving` and `after_serving`, using the Quart `test_client` requires the use of `test_app`. Pytest example shown below:

```python
# file: test.py
import pytest
from app import app

@pytest.fixture(name="my_app", scope="function")
async def _my_app():
    async with app.test_app() as test_app:
        yield test_app

async def test_redis(my_app):
    async with my_app.test_client() as client:
        result = await client.get("/")
        assert result == b"it works!"
```

## Faking Redis

For development and testing, you may not have a running Redis instance. In this case, the [`fakeredis`](https://pypi.org/project/fakeredis/) package may be installed and then used instead of actual redis by setting `USE_FAKE_REDIS` environment variable to true at runtime.
