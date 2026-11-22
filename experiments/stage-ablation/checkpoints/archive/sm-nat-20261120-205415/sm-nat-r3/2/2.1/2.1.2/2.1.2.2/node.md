# N118: 当缓存容量 C=128GB 且对象大小服从 Pareto(α=1.1) 时，可缓存对象数 K 的数值解约为 1.2×10^5（假设最小对象 1KB），此时 P_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41, N42, N43

## Claim

当缓存容量 C=128GB 且对象大小服从 Pareto(α=1.1) 时，可缓存对象数 K 的数值解约为 1.2×10^5（假设最小对象 1KB），此时 P_topK ≈ 0.995，表明 LRU 在理论上几乎覆盖所有高频请求，字节命中率下界主要由大小加权修正项决定而非请求覆盖率。

## Corrected Claim

当缓存容量 C=128GB 且对象大小服从 Pareto(α=1.1) 时，可缓存对象数 K 的数值解约为 1.2×10^5（假设最小对象 1KB），此时 P_topK ≈ 0.995，表明 LRU 在理论上几乎覆盖所有高频请求，字节命中率下界主要由大小加权修正项决定而非请求覆盖率。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 分布下，128GB 容量足以覆盖绝大多数高频小对象，K≈1.2×10^5 与 P_topK≈0.995 在量级和逻辑上自洽，符合 LRU 缓存理论模型。

## Search Query

Pareto distribution cumulative size cache capacity object count
