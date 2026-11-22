# N157: 工作点1（高覆盖/低精度）：设定请求频次占比阈值 R(k) = 90%。解得 k_eff ≈ 10^5 * (0.10)^(1/0.9) ≈ 10^5 * 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N70

## Claim

工作点1（高覆盖/低精度）：设定请求频次占比阈值 R(k) = 90%。解得 k_eff ≈ 10^5 * (0.10)^(1/0.9) ≈ 10^5 * 0.126 ≈ 12600 个对象。此工作点覆盖了绝大多数请求，但包含了大量低频对象，导致缓存替换开销增加，命中率增益边际递减。

## Corrected Claim

工作点1（高覆盖/低精度）：设定请求频次占比阈值 R(k) = 90%。解得 k_eff ≈ 10^5 * (0.10)^(1/0.9) ≈ 10^5 * 0.126 ≈ 12600 个对象。此工作点覆盖了绝大多数请求，但包含了大量低频对象，导致缓存替换开销增加，命中率增益边际递减。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 10^5 * (0.1)^(1/0.9) ≈ 12589 与陈述中的 12600 一致，且符合 Zipf 分布下覆盖 90% 流量所需对象数量的量级直觉。

## Search Query

Pareto distribution request frequency coverage k_eff calculation beta 0.9
