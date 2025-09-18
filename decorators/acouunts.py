from functools import wraps
from config import ACCOUNT_INFO
def ensure_accounts(func):
    @wraps(func)
    async def wrapper(self, *args, **kwargs):
        if not self._init_account:
            for user in ACCOUNT_INFO:
                await self.api.pool.add_account(
                    user.username, "", "", "", cookies=user.cookies
                )
            self._init_account = True
        return await func(self, *args, **kwargs)
    return wrapper

