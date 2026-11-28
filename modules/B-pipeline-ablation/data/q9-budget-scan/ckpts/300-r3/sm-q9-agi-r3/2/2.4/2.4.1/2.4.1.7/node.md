# N222: Semantic Scholar API 速率限制的突发容忍度：免费层虽标称 1 req/s，但实际支持短时的 Burst Traffic（约 5-10 req

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N63, N64, N65

## Claim

Semantic Scholar API 速率限制的突发容忍度：免费层虽标称 1 req/s，但实际支持短时的 Burst Traffic（约 5-10 req/s 持续 1s 不触发 429），通过令牌桶算法（Token Bucket, rate=1, burst=5）平滑请求，可将短期并发检索的等待时间减少 80%，避免简单的 sleep(1) 造成的串行瓶颈。

## Corrected Claim

Semantic Scholar API 免费层存在速率限制（通常约为 1 req/s 或 60 req/min），实际使用中可能存在短暂的突发容忍度。采用令牌桶等平滑算法进行请求调度，相比简单的固定间隔 sleep，能更有效地利用允许的突发窗口，减少因严格串行等待造成的整体耗时，从而优化批量检索效率。

## Evidence

[质询]具体数值（burst 5-10 req/s, 80% 效率提升）及特定算法参数（token bucket rate=1, burst=5）属于经验性工程细节，缺乏官方文档或权威来源的直接支持，且不同时期/账户类型的限制策略可能不同，存在过度具体化导致的准确性风险。 | 来源 [1][2] 确认了 Semantic Scholar API 存在速率限制（如 60 req/min）及 429 错误，支持使用节流机制的必要性，但未提供具体的 burst 容忍度数值或令牌桶参数；来源 [3] 讨论替代方案，未涉及此细节。逻辑上令牌桶算法用于平滑流量是合理的，但具体参数为经验事实，缺直接来源支持。

## Search Query

Semantic Scholar API rate limit burst tolerance 429 status code behavior

## Retrieval Sources

- {'url': 'https://ask.csdn.net/questions/9046325&rut=7ab07eb340d6084f8f16e102fa44905b21d8a434addfb803c4d8cd076a8e6689', 'type': 'ddg', 'title': '如何处理Semantic Scholar API的请求频率限制？ - CSDN问答'}
- {'url': 'https://ask.csdn.net/questions/9046325/56029081&rut=ea4b53a42cbc1ecd019bfedb2570e52b1ee61d0368e3516c9fec5606c3690745', 'type': 'ddg', 'title': '如何处理Semantic Scholar API的请求频率限制？ - CSDN问答'}
- {'url': 'https://blog.csdn.net/weixin_42441790/article/details/169156009&rut=5fa4908b7ddc383b119c55bacc388cc193a266e3b77e75ed9daa9ac88e47afdf', 'type': 'ddg', 'title': '给研究助手接上论文检索：Semantic Scholar限流之后用谁顶上-CSDN博客'}
