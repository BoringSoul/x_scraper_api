import json
from starlette.requests import Request
from client.twitter import TweetScraper
from models.req.search import SearchReq
from decorators.request_handler import handle_request
from starlette.responses import Response, JSONResponse

@handle_request
async def tweet_details(requet: Request) -> Response:
    tweet_id = requet.path_params.get("tweet_id")
    if not tweet_id:
        return JSONResponse({"message": "请提供推文ID"})
    result = await TweetScraper().tweet_details(int(tweet_id))
    if not result:
        return JSONResponse({"message": "获取推文内容失败"})
    return Response(content=result.json(), headers={"Content-Type": "application/json"})

@handle_request
async def get_user_info(requet: Request) -> Response:
    username = requet.path_params.get("username")
    if not username:
        return JSONResponse({"message": "请提供用户名"})
    result = await TweetScraper().user_by_login(username)
    if not result:
        return JSONResponse({"message": "获取用户信息失败"})
    return Response(content=result.json(), headers={"Content-Type": "application/json"})

@handle_request
async def get_user_tweets(requet: Request) -> Response:
    user_id = requet.path_params.get("user_id")
    if not user_id:
        return JSONResponse({"message": "请提供用户id"})
    page_size = requet.query_params.get("sz")
    page_size = int(page_size) if page_size else 100
    result = await TweetScraper().user_tweets(int(user_id), page_size)
    if not result:
        return JSONResponse({"message": "没有找到对应推文"})
    return JSONResponse([json.loads(i.json()) for i in result])

@handle_request
async def search(request: Request) -> JSONResponse:
    data = await request.json()
    if not data:
        return JSONResponse({"message": "请提供搜索参数"})
    req = SearchReq(**data)
    result = await TweetScraper().search(req.q, req.kv, req.limit)
    if not result:
        return JSONResponse({"message": "没有找到对应推文"})
    return JSONResponse([json.loads(i.json()) for i in result])

