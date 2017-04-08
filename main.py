import asyncio

from telegraph import TelegraphClient

async def main(loop):
    tg = TelegraphClient()
    tg.loop = loop
    response = await tg.get_page_list()
    if response['ok']:
        result = response['result']
        total_count = result['total_count']
        print('You have {} post(s) at telegra.ph'.format(total_count))
    else:
        print('Something gone wrong')

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))

