#!/bin/python3
import aiohttp
import asyncio
import time

start_time = time.time()

no_link_counter = []

# Requests page html
async def get_page_html(session, url):
    async with session.get(url) as response:
        page_html = await response.text()
        return page_html

async def main():

    # Creates connection
    async with aiohttp.ClientSession() as session:
        print('\nSending requests and collecting responses...')
        # Runs requests in coroutines        
        tasks = []
        for page_number in range(1, 10000):
            url = f'https://s3.eu-central-1.amazonaws.com/qa-web-test-task/{page_number}.html'
            tasks.append(asyncio.ensure_future(get_page_html(session, url)))
        # Creates list that contains all pages text
        html_list = await asyncio.gather(*tasks)
        print('\nPreparing of result...')
        # Parses every page text for next page link, adds to no_link_counter
        for item in range(1, len(html_list) + 1):
            if f"a href='{item + 1}.html'" not in html_list[item - 1]:
                no_link_counter.append(item)

# Handles exception for EventLoopPolicy on Windows, except for Linux
try:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
except:
    asyncio.run(main())

end_time = time.time() - start_time
print(f"\nWeb test #0 completed:\nExecution time: {end_time:.3f} seconds")
print(f"List of page numbers with missed links: {no_link_counter}")
