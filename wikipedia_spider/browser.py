import asyncio
import nest_asyncio
import sys
import threading
from camoufox.async_api import AsyncCamoufox

nest_asyncio.apply()


async def main():
    async with AsyncCamoufox() as browser:
        page = await browser.new_page()
        await page.goto(
            "https://en.wikipedia.org/wiki/Category:Works_about_animals"
        )


def run_main():
    if not sys.platform.startswith("win") and sys.version_info >= (3, 10):
        loop = asyncio.new_event_loop()
    else:
        loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    loop.close()


if __name__ == "__main__":
    if sys.platform.startswith("win") and sys.version_info >= (3, 10):
        threading.Thread(target=run_main).start()
    else:
        asyncio.create_task(main())
