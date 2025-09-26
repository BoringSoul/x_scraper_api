# X Scraper API

X Scraper API 是一个基于Python的Twitter数据抓取API服务，使用twscrape库实现数据抓取功能。

## API 接口文档

### 1. 获取推文详情

**Endpoint:** `GET /api/tweet/{tweet_id}`

根据推文ID获取推文详细信息。

**参数:**
- `tweet_id` (int, path): 推文的唯一标识符

**响应:**
- 成功: 返回推文详细信息的JSON对象
- 失败: 返回错误信息 `{"message": "获取推文内容失败"}`

### 2. 获取用户信息

**Endpoint:** `GET /api/user/{username}`

根据用户名获取用户信息。

**参数:**
- `username` (str, path): Twitter用户名

**响应:**
- 成功: 返回用户信息的JSON对象
- 失败: 返回错误信息 `{"message": "获取用户信息失败"}`

### 3. 获取用户推文

**Endpoint:** `GET /api/user/tweets/{user_id}`

根据用户ID获取该用户发布的推文列表。

**参数:**
- `user_id` (int, path): 用户的唯一标识符
- `sz` (int, query, 可选): 返回推文数量，默认为100

**响应:**
- 成功: 返回推文列表的JSON数组
- 失败: 返回错误信息 `{"message": "没有找到对应推文"}`

### 4. 获取用户关注列表

**Endpoint:** `GET /api/user/following/{user_id}`

根据用户ID获取该用户的关注列表。

**参数:**
- `user_id` (int, path): 用户的唯一标识符
- `sz` (int, query, 可选): 返回用户数量，默认为100

**响应:**
- 成功: 返回用户列表的JSON数组

### 5. 获取用户粉丝列表

**Endpoint:** `GET /api/user/followers/{user_id}`

根据用户ID获取该用户的粉丝列表。

**参数:**
- `user_id` (int, path): 用户的唯一标识符
- `sz` (int, query, 可选): 返回用户数量，默认为100

**响应:**
- 成功: 返回用户列表的JSON数组

### 6. 搜索推文

**Endpoint:** `POST /api/search`

根据关键词搜索推文。

**请求体 (JSON):**
```json
{
  "q": "string",           // 搜索关键词
  "kv": "dict",            // 搜索参数，默认为 {"product": "top"}
  "limit": "int"           // 返回结果数量限制，默认为100
}
```

**响应:**
- 成功: 返回匹配推文列表的JSON数组
- 失败: 返回错误信息 `{"message": "没有找到对应推文"}`

## 项目结构

```
x_scraper_api/
├── client/              # 客户端实现
│   └── twitter.py       # Twitter抓取器实现
├── constants/           # 常量定义
│   └── request/
│       └── method.py    # HTTP方法常量
├── decorators/          # 装饰器实现
├── models/              # 数据模型
│   ├── req/             # 请求数据模型
│   │   └── search.py    # 搜索请求模型
│   ├── resp/            # 响应数据模型
│   └── twscraper/       # twscrape模型
├── routes/              # API路由定义
│   ├── __init__.py      # 路由配置
│   └── twitter.py       # 推文相关路由
├── app.py               # 应用主文件
├── config.py            # 配置文件
├── logger.py            # 日志配置
└── main.py              # 程序入口
```