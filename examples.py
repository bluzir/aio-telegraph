import asyncio

from api import TelegraphAPIClient

async def get_posts_count():
    response = await tg.get_page_list()
    if response['ok']:
        result = response['result']
        total_count = result['total_count']
        return total_count
    else:
        return 0


async def main(loop):
    posts = await get_posts_count()
    print(posts)

loop = asyncio.get_event_loop()
tg = TelegraphAPIClient()
tg.loop = loop
loop.run_until_complete(main(loop))

