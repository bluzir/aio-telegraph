import json

import settings as config

from base import BaseClient


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
        self.url = self.BASE_URL.format('createAccount')
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
        self.url = self.BASE_URL.format('editAccountInfo')
        self.params = {
            'short_name': config.SHORT_NAME,
            'author_name': config.AUTHOR_NAME,
            'author_url': config.AUTHOR_URL,
            'access_token': config.ACCESS_TOKEN,
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

    async def revoke_access_token(self):
        self.url = self.BASE_URL.format('revokeAccessToken')
        self.params = {
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def create_page(self, title, content, return_content=False):
        self.url = self.BASE_URL.format('createPage')
        self.params = {
            'title': title,
            'content': content,
            'return_content': return_content,
            'access_token': self.ACCESS_TOKEN,
        }
        result = await self.get_request()
        return result

    async def edit_page(self, path, title, content, return_content=False):
        self.url = self.BASE_URL.format('editPage')
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