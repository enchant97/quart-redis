# Example Of Usage
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
        assert await result.data == b"it works!"
```
