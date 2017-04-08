import asyncio
import json

import settings as config

from base import BaseClient


class TelegraphClient(BaseClient):
    BASE_URL = 'https://api.telegra.ph/{}'
    ACCESS_TOKEN = config.ACCESS_TOKEN

    def __init__(self):
        super(TelegraphClient, self).__init__()
        self.client = None
        self.access_token = None
        self.params = None
        self.data = None

    async def create_account(self):
        self.url = self.BASE_URL.format('createAccount')
        self.params = {
            'short_name': config.SHORT_NAME,
            'author_name': config.AUTHOR_NAME,
            'author_url': config.AUTHOR_URL,
        }
        result = await self.get_request()
        return result

    async def get_account_info(self):
        self.url = self.BASE_URL.format('getAccountInfo')
        fields = ['short_name', 'author_name', 'author_url', 'auth_url', 'page_count']
        self.params = {
            'fields': json.dumps(fields),
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def get_page_list(self, offset=0, limit=50):
        self.url = self.BASE_URL.format('getPageList')
        self.params = {
            'offset': offset,
            'limit': limit,
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def get_token(self):
        result = self.create_account()
        token = result['access_token']
        return token












