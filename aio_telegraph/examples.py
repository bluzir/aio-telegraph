import asyncio

from aio_telegraph.api import TelegraphAPIClient


async def register_user():
    short_name = input('Enter your short name: ')
    author_name = input('Enter author name: ')
    author_url = input('Enter your author url: ')
    response = await tg.create_account(short_name, author_name, author_url)
    if response['ok']:
        result = response['result']
        return result
    else:
        return False


async def check_token():
    response = await tg.get_account_info()
    if response['ok']:
        return True
    else:
        return False


async def get_posts_count():
    response = await tg.get_page_list()
    if response['ok']:
        result = response['result']
        total_count = result['total_count']
        return total_count
    else:
        return 0


async def main():
    user = await register_user()
    if user:
        token = user['access_token']
        auth_url = user['auth_url']
        tg.ACCESS_TOKEN = token
        count = await get_posts_count()
        print('Your access token: {}'.format(token))
        print('You can authenticate in browser by this url: {}'.format(auth_url))
        print('Your posts count is {}'.format(count))
    else:
        print("Something gone wrong")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tg = TelegraphAPIClient()
    tg.loop = loop
    loop.run_until_complete(main())

