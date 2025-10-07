import os
import aiohttp
import asyncio
from urllib.parse import urlencode
from dotenv import load_dotenv
load_dotenv()
from htx_api_python.HTX_Manager.Ed25519 import HTX_Api_Manager


async def main():
    """
        Main function to demonstrate API client usage.
        """
    access_key = os.getenv("HTX_Ed25519_ACCESS_KEY")

    if not access_key:
        print("Error: Please set HTX_ED25519_ACCESS_KEY  in your .env file.")
        return
    
    async with HTX_Api_Manager(access_key) as client:
        accounts = await client.get_accounts()
        # print("Accounts:", accounts)
        accountsId = ""
        if accounts and accounts.get('status') == 'ok':
            accountsId = accounts['data'][0]['id']
            print('ACCOUNT_ID: ', accounts['data'][0]['id'])

        print("AccountsID:", accountsId)

        accountBalance = await client.get_account_balance(accountsId)
        if accountBalance is not None:
            print("Failed to retrieve account balance.")
            data = accountBalance["data"]
            balances_list = accountBalance["data"].get("list", [])
            for balance in balances_list:
                if balance.get("currency") == "usdt":
                    print("USDT Balance:", balance)
                    break

            return 
       


asyncio.run(main())
