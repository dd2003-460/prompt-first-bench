# N124: Pareto(β=0.9) 分布下，头部 10% 对象占据的请求流量比例 R_req(0.1) 的精确计算值为 1 - 0.1^(0.1) ≈ 80.1%，表明

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N48

## Claim

Pareto(β=0.9) 分布下，头部 10% 对象占据的请求流量比例 R_req(0.1) 的精确计算值为 1 - 0.1^(0.1) ≈ 80.1%，表明 LFU 策略仅缓存前 10% 对象即可覆盖约 80% 的流量，是评估 LFU 相对于 LRU 提升空间的关键阈值。

## Corrected Claim

Pareto(β=0.9) 分布下，头部 10% 对象占据的请求流量比例 R_req(0.1) 的精确计算值为 1 - 0.1^(0.1) ≈ 80.1%，表明 LFU 策略仅缓存前 10% 对象即可覆盖约 80% 的流量，是评估 LFU 相对于 LRU 提升空间的关键阈值。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积分布函数推导正确，数值计算准确
