from unittest import IsolatedAsyncioTestCase

from redis.asyncio import from_url

from tests.app import create_app


class QuartAppTestCase(IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.r = from_url("redis://localhost")
        await self.r.flushall()
        await self.r.ping()
        self.app = create_app().test_app()
        await self.app.startup()

    async def asyncTearDown(self):
        await self.app.shutdown()
        await self.r.flushall(True)
        await self.r.aclose()

    async def test_get_msg(self):
        async with self.app.test_client() as client:
            await self.r.set("msg", "Hello World")
            resp = await client.get("/get-msg")
            data = await resp.get_data(as_text=True)
            self.assertEqual("Hello World", data)

    async def test_get_msg_with_context(self):
        async with self.app.test_client() as client:
            await self.r.set("msg", "Hello World")
            resp = await client.get("/get-msg/with-context")
            data = await resp.get_data(as_text=True)
            self.assertEqual("Hello World", data)

    async def test_set_msg(self):
        async with self.app.test_client() as client:
            await client.post("/set-msg")
            data = await self.r.get("msg")
            self.assertEqual(b"Hello World", data)
