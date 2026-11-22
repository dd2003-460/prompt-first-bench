# N10: LRU 稳态字节命中率下界模型：HitRate_bytes_LRU ≈ 1 - (1/C_bytes) * ∫_{s_min}^{∞} s * f_S(s) *

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

LRU 稳态字节命中率下界模型：HitRate_bytes_LRU ≈ 1 - (1/C_bytes) * ∫_{s_min}^{∞} s * f_S(s) * (1 - F_H(h(s))) ds，其中 h(s) 由负相关 ρ=-0.3 确定，该积分需数值求解，下界由忽略相关性的独立假设（ρ=0）计算得出。

## Corrected Claim

LRU 稳态字节命中率下界模型：HitRate_bytes_LRU ≈ 1 - (1/C_bytes) * ∫_{s_min}^{∞} s * f_S(s) * (1 - F_H(h(s))) ds，其中 h(s) 由负相关 ρ=-0.3 确定，该积分需数值求解，下界由忽略相关性的独立假设（ρ=0）计算得出。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 780)

## Search Query

LRU cache hit rate lower bound pareto size popularity correlation
