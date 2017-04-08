import aiohttp


class BaseClient:
    BASE_URL = None

    def __init__(self):
        self.loop = None
        self.client = None
        self.url = None
        self.params = None
        self.data = None

    async def get_request(self):
        async with aiohttp.ClientSession(loop=self.loop) as client:
            async with client.get(self.url, params=self.params) as resp:
                assert resp.status == 200
                return await resp.json()

    async def post_request(self):
        async with aiohttp.ClientSession(loop=self.loop) as client:
            async with client.post(self.url, params=self.params, data=self.data) as resp:
                assert resp.status == 200
                return await resp.json()


