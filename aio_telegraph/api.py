import json

import aio_telegraph.config as config

from aio_telegraph.base import BaseClient


class TelegraphAPIClient(BaseClient):
    BASE_URL = 'https://api.telegra.ph/{}'
    ACCESS_TOKEN = config.ACCESS_TOKEN

    def __init__(self, access_token=None):
        super(TelegraphAPIClient, self).__init__()
        self.client = None
        self.access_token = access_token
        self.params = None
        self.data = None

        if not self.access_token:
            self.access_token = config.ACCESS_TOKEN

    async def create_account(self, short_name=None, author_name=None, author_url=None):
        method = 'createAccount'
        self.url = self.BASE_URL.format(method)
        if not short_name:
            short_name = config.SHORT_NAME

        if not author_name:
            author_name = config.AUTHOR_NAME

        if not author_url:
            author_url = config.AUTHOR_URL

        self.params = {
            'short_name': short_name,
            'author_name': author_name,
            'author_url': author_url,
        }
        result = await self.get_request()
        return result

    async def edit_account_info(self):
        method = 'editAccountInfo'
        self.url = self.BASE_URL.format(method)

        self.params = {
            'short_name': config.SHORT_NAME,
            'author_name': config.AUTHOR_NAME,
            'author_url': config.AUTHOR_URL,
            'access_token': config.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def get_account_info(self):
        method = 'getAccountInfo'
        self.url = self.BASE_URL.format(method)
        fields = ['short_name', 'author_name', 'author_url', 'auth_url', 'page_count']
        self.params = {
            'fields': json.dumps(fields),
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def revoke_access_token(self):
        method = 'revokeAccessToken'
        self.url = self.BASE_URL.format(method)
        self.params = {
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def create_page(self, title, content, return_content=False):
        method = 'createPage'
        self.url = self.BASE_URL.format(method)

        self.params = {
            'title': title,
            'content': content,
            'return_content': return_content,
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def edit_page(self, path, title, content, return_content=False):
        method = 'editPage'
        self.url = self.BASE_URL.format(method)
        self.params = {
            'access_token': self.ACCESS_TOKEN,
            'path': path,
            'title': title,
            'content': content,
            'return_content': return_content,
        }
        result = await self.get_request()
        return result

    async def get_page(self, path, return_content=False):
        self.url = self.BASE_URL.format('getPage')
        self.params = {
            'path': path,
            'return_content': return_content,
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

    async def get_views(self, path, year=None, month=None, day=None, hour=None):
        self.url = self.BASE_URL.format('getViews')
        self.params = {
            'path': path,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
        }
        result = await self.get_request()
        return result
