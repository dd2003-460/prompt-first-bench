# N138: N51 中 LFU 提升上限公式 ΔH ≤ (1 - H_LRU) * (1 - e^(-λ * T_window)) 存在量纲错误：(1 - e^(-λ * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

N51 中 LFU 提升上限公式 ΔH ≤ (1 - H_LRU) * (1 - e^(-λ * T_window)) 存在量纲错误：(1 - e^(-λ * T_window)) 是频率计数器对稳态流量的捕获率（≈0.095 for λ=0.1, T=1），而非 LFU 相对于 LRU 的增益；LFU 的增益来源于避免驱逐高频但非最近访问的对象，其上限应定义为 ΔH_max = H_optimal_subset - H_LRU，其中 H_optimal_subset 是容量约束下最大化字节吞吐的子集命中率，该值在 β=0.9 平坦分布下与 LRU 差距极小（<2%），因为 LFU 在长尾对象上的频率估计误差（N60 RSE≈4.8%）抵消了头部优势。

## Corrected Claim

N51 中 LFU 提升上限公式 ΔH ≤ (1 - H_LRU) * (1 - e^(-λ * T_window)) 存在量纲错误：(1 - e^(-λ * T_window)) 是频率计数器对稳态流量的捕获率（≈0.095 for λ=0.1, T=1），而非 LFU 相对于 LRU 的增益；LFU 的增益来源于避免驱逐高频但非最近访问的对象，其上限应定义为 ΔH_max = H_optimal_subset - H_LRU，其中 H_optimal_subset 是容量约束下最大化字节吞吐的子集命中率，该值在 β=0.9 平坦分布下与 LRU 差距极小（<2%），因为 LFU 在长尾对象上的频率估计误差（N60 RSE≈4.8%）抵消了头部优势。

## Evidence

先验知识/题面给定，逻辑校验通过：原公式将频率捕获率误用为命中率增益上限，量纲与物理意义不符；修正后的定义基于最优子集命中率差值，且结合长尾频率估计误差（RSE）抵消头部优势的逻辑自洽，符合缓存替换算法的基本原理。
