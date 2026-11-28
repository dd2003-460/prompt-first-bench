# N23: 外部依赖不确定性：云端 API 响应延迟 P99 通常比 P50 高 2-5 倍，且存在速率限制（如 100 req/min），影响批量检索任务的并行度，需在调

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N5

## Claim

外部依赖不确定性：云端 API 响应延迟 P99 通常比 P50 高 2-5 倍，且存在速率限制（如 100 req/min），影响批量检索任务的并行度，需在调度器中建模为随机变量 U[1,5] × P50_latency

## Corrected Claim

外部依赖不确定性：云端 API 响应延迟 P99 通常比 P50 高 2-5 倍，且存在速率限制（如 100 req/min），影响批量检索任务的并行度，需在调度器中建模为随机变量 U[1,5] × P50_latency

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud LLM API latency distribution P50 P99 rate limiting impact on batch processing
