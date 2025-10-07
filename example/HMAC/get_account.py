import os
import aiohttp
import asyncio
from urllib.parse import urlencode
from dotenv import load_dotenv
load_dotenv()
from htx_api_python.HTX_Manager.hmacsha256 import HTX_Api_Manager


async def main():
    """
        Main function to demonstrate API client usage.
        """
    access_key = os.getenv("HTX_ACCESS_KEY")
    secret_key = os.getenv("HTX_SECRET_KEY")

    if not access_key or not secret_key:
        print("Error: Please set HTX_ACCESS_KEY and HTX_SECRET_KEY in your .env file.")
        return
    
    async with HTX_Api_Manager(access_key, secret_key) as client:
        accounts = await client.get_accounts()
        print("Accounts:", accounts)

        account2 = await client.get_accounts()
        print("Accounts:", account2)


asyncio.run(main())
