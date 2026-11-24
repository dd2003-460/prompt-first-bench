# N330: L1 缓存命中率 H_l1 由对象流行度分布（Zipf 参数 α）和缓存容量 C_l1 决定，H_l1 = 1 - P(request for uncached

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

L1 缓存命中率 H_l1 由对象流行度分布（Zipf 参数 α）和缓存容量 C_l1 决定，H_l1 = 1 - P(request for uncached object)，P99 延迟中回源路径的权重为 (1-H_l1)。

## Corrected Claim

L1 缓存命中率 H_l1 由对象流行度分布（Zipf 参数 α）和缓存容量 C_l1 决定，H_l1 = 1 - P(request for uncached object)，P99 延迟中回源路径的权重为 (1-H_l1)。

## Evidence

先验知识/题面给定，逻辑校验通过：缓存命中率定义即为命中请求占比，未命中占比(1-H)即为回源权重，符合基本概率逻辑。
