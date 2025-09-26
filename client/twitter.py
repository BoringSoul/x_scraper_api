from decorators.acouunts import ensure_accounts
from logger import BaseLogger
from twscrape import API, gather
from twscrape.models import User, Tweet
from config import ACCOUNTS_DB_PATH
from decorators.singleton import singleton


@singleton
class TweetScraper:

    def __init__(self) -> None:
        self.logger = BaseLogger(name=__name__)
        self.api = API(ACCOUNTS_DB_PATH)
        self._init_account = False

    @ensure_accounts
    async def tweet_details(self, tweet_id: int) -> Tweet | None:
        try:
            return await self.api.tweet_details(tweet_id)
        except Exception as e:
            self.logger.error(f"获取推文内容失败: {e}")
            return None

    @ensure_accounts
    async def user_by_login(self, username: str) -> User | None:
        try:
            return await self.api.user_by_login(username)
        except Exception as e:
            self.logger.error(f"获取用户名 '{username}' 的用户信息时出错: {e}")
        return None

    @ensure_accounts
    async def user_tweets(self, user_id: int, limit: int = 100) -> list[Tweet]:
        try:
            return await gather(self.api.user_tweets(user_id, limit))
        except Exception as e:
            self.logger.error(f"获取用户 ID {user_id} 推文时出错: {e}")
        return []
    
    @ensure_accounts
    async def user_following(self, user_id: int, limit: int = 100) -> list[User]:
        try:
            return await gather(self.api.following(user_id, limit))
        except Exception as e:
            self.logger.error(f"获取用户 ID {user_id} 关注列表时出错: {e}")
        return []

    @ensure_accounts
    async def user_followers(self, user_id: int, limit: int = 100) -> list[User]:
        try:
            return await gather(self.api.followers(user_id, limit))
        except Exception as e:
            self.logger.error(f"获取用户 ID {user_id} 粉丝列表时出错: {e}")
        return []

    @ensure_accounts
    async def search(self, q: str, kv: dict = {"product": "Top"}, limit: int = 100):
        try:
            return await gather(self.api.search(q, kv=kv, limit=limit))
        except Exception as e:
            self.logger.error(f"搜索时出错: {e}")
        return []
