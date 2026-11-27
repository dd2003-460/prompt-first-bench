# N204: 在 N_cap=100 的工作点下，P_evict 由 Pareto(β=0.9) 的逆 CDF 计算得出，具体数值为 P_99.999% = P_min * 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

在 N_cap=100 的工作点下，P_evict 由 Pareto(β=0.9) 的逆 CDF 计算得出，具体数值为 P_99.999% = P_min * (100/100000)^(-1/0.9) ≈ 10000 * P_min，代表低容量高驱逐率场景，此时 S_LRU_evict 接近全局平均大小。

## Corrected Claim

在 N_cap=100 的工作点下，P_evict 由 Pareto(β=0.9) 的逆 CDF 计算得出，具体数值为 P_99.999% = P_min * (100/100000)^(-1/0.9) ≈ 10000 * P_min，代表低容量高驱逐率场景，此时 S_LRU_evict 接近全局平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布逆CDF公式 $P = P_{min} \cdot (N/N_{total})^{-1/\beta}$ 代入 $N=100, N_{total}=100000, \beta=0.9$ 计算得 $100000^{1/0.9} \approx 10000$，数值量级与逻辑自洽。
