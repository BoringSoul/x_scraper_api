from starlette.routing import Route, Mount
from constants.request.method import GET, POST
from .twitter import *

routes = [
    Mount(path="/api", routes=[
        Route(path="/tweet/{tweet_id:int}", methods=[GET], endpoint=tweet_details),
        Route(path="/user/{username}", methods=[GET], endpoint=get_user_info),
        Route(path="/user/tweets/{user_id:int}", methods=[GET], endpoint=get_user_tweets),
        Route(path="/search", methods=[POST], endpoint=search),
    ])
]