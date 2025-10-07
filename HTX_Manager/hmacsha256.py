# signature MANAGER HmacSHA256
import time
import hmac
import hashlib
import base64
from urllib.parse import urlencode
from typing import Dict, Any, Optional
import aiohttp
import asyncio


class HTX_Api_Manager:
    # BASE
    def __init__(self, access_key, secret_key, url="https://api.huobi.pro"):
        if not access_key or not secret_key:
            raise ValueError("API access_key and secret_key cannot be empty.")
        
        self.access_key = access_key
        self.secret_key = secret_key
        self.BASE_URL = url

        # Session is created within the async context manager for proper handling
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        """Async context manager entry to create the session."""
        self.session = aiohttp.ClientSession(headers={
            "Content-Type": "application/json",
            "User-Agent": "MyHtxAsyncClient/1.0"
        })
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit to close the session."""
        if self.session:
            await self.session.close()

    def _create_signature(self, method: str, path: str, params: Dict[str, Any]) -> str:
        """Creates the required API signature."""
        host = self.BASE_URL.replace("https://", "")
        # The signature payload requires parameters to be sorted alphabetically.
        sorted_params = urlencode(sorted(params.items()))
        payload = f"{method.upper()}\n{host}\n{path}\n{sorted_params}"
        
        digest = hmac.new(self.secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).digest()
        return base64.b64encode(digest).decode()
    
    async def _signed_request(self, method: str, path: str, extra_params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        if not self.session:
            raise RuntimeError("Session not started. Use 'async with' context manager.")

        if extra_params is None:
            extra_params = {}
            
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        
        params = {
            'AccessKeyId': self.access_key,
            'SignatureMethod': 'HmacSHA256',
            'SignatureVersion': '2',
            'Timestamp': timestamp,
            **extra_params
        }
        
        params['Signature'] = self._create_signature(method, path, params)
        
        url = f"{self.BASE_URL}{path}?{urlencode(params)}"
        print("Request URL:", url)

        try:
            async with self.session.request(method, url) as response:
                response.raise_for_status()  # Raises ClientResponseError for bad responses (4xx or 5xx)
                data = await response.json()
                # print("data:", data)

                # Huobi API specific error checking
                if data.get('status') == 'error':
                    print(f"API Error: {data.get('err-msg')}")
                    return None
                return data
        except aiohttp.ClientError as e:
            print(f"An error occurred during the request: {e}")
            return None

    async def get_accounts(self) -> Optional[Dict[str, Any]]:
        """Fetches all accounts associated with the API key."""
        return await self._signed_request('GET', '/v1/account/accounts')