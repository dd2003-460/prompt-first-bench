# N457: Mock Server 注入延迟的实现机制：在 FastAPI/Flask 响应中间件中调用 time.sleep(t) 或 asyncio.sleep(t)，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N160

## Claim

Mock Server 注入延迟的实现机制：在 FastAPI/Flask 响应中间件中调用 time.sleep(t) 或 asyncio.sleep(t)，需确保 t 的精度误差 < 10ms（基于系统时钟分辨率），避免阻塞主线程导致请求超时

## Corrected Claim

Mock Server 注入延迟的实现机制：在 FastAPI/Flask 响应中间件中调用 time.sleep(t) 或 asyncio.sleep(t)，需确保 t 的精度误差 < 10ms（基于系统时钟分辨率），避免阻塞主线程导致请求超时

## Evidence

先验知识/题面给定，逻辑校验通过
