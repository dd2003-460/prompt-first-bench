# N24: 并发控制采用令牌桶算法，限流阈值为每秒10个新请求（基于V100集群的最大Prefill吞吐），突发流量被缓冲到队列，队列长度超过100时返回429状态码，避免

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

并发控制采用令牌桶算法，限流阈值为每秒10个新请求（基于V100集群的最大Prefill吞吐），突发流量被缓冲到队列，队列长度超过100时返回429状态码，避免OOM和延迟雪崩。

## Corrected Claim

并发控制采用令牌桶算法，限流阈值为每秒10个新请求（基于V100集群的最大Prefill吞吐），突发流量被缓冲到队列，队列长度超过100时返回429状态码，避免OOM和延迟雪崩。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM rate limiting token bucket algorithm
