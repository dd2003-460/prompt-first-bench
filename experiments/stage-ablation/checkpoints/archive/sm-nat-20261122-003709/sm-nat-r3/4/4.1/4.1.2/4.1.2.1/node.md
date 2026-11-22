# N176: K_objects 的具体数值确定：根据 N67 和 N81 的结论，在 C=128GB 和 Pareto(α=1.1) 下，缓存可容纳的对象数量 K ≈ 50

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

K_objects 的具体数值确定：根据 N67 和 N81 的结论，在 C=128GB 和 Pareto(α=1.1) 下，缓存可容纳的对象数量 K ≈ 50,000-60,000（若按头部对象平均大小估算）或 K=100,000（若按最小对象 1KB 估算）。需明确采用哪种 K 值进行 P_cov 计算，不同 K 导致 P_cov 差异巨大。

## Corrected Claim

K_objects 的具体数值确定：根据 N67 和 N81 的结论，在 C=128GB 和 Pareto(α=1.1) 下，缓存可容纳的对象数量 K ≈ 50,000-60,000（若按头部对象平均大小估算）或 K=100,000（若按最小对象 1KB 估算）。需明确采用哪种 K 值进行 P_cov 计算，不同 K 导致 P_cov 差异巨大。

## Evidence

先验知识/题面给定，逻辑校验通过：128GB / 1KB = 131,072，与K=100,000量级一致；128GB / 2.5KB ≈ 52,428，与K≈50,000-60,000量级一致，数值推导自洽。
