# N233: 异步执行架构：使用 Celery 或 asyncio 将验证任务放入后台队列，主推理链路仅同步执行‘快速预检’（如数值格式检查，耗时 <100ms），验证结果通

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82

## Claim

异步执行架构：使用 Celery 或 asyncio 将验证任务放入后台队列，主推理链路仅同步执行‘快速预检’（如数值格式检查，耗时 <100ms），验证结果通过 WebSocket 推送至前端；若验证失败，主流程暂停并等待人工介入，避免阻塞后续无关步骤。

## Corrected Claim

异步执行架构：使用 Celery 或 asyncio 将验证任务放入后台队列，主推理链路仅同步执行‘快速预检’（如数值格式检查，耗时 <100ms），验证结果通过 WebSocket 推送至前端；若验证失败，主流程暂停并等待人工介入，避免阻塞后续无关步骤。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

async agent workflow verification queue Celery websocket push LLM pipeline
