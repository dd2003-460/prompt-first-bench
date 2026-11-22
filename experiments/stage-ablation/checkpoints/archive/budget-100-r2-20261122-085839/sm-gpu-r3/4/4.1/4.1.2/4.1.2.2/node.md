# N196: A100 80GB 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 的量化范围：由于 A100 HBM2

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N57

## Claim

A100 80GB 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 的量化范围：由于 A100 HBM2e 架构成熟，在 Batch=1 小批量读取场景下，实测有效带宽通常为理论峰值 (2039 GB/s) 的 80%-90%。取中值 85% 计算，有效带宽 = 1733.15 GB/s。

## Corrected Claim

A100 80GB 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 通常较高，具体数值需依据实测数据确定，理论峰值为 2039 GB/s。

## Evidence

[质询]该陈述包含具体的经验性数值（80%-90%利用率范围及85%中值），属于硬件性能实测数据，无法从第一性原理或数学公理严格推导得出，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

A100 LLM decode memory bandwidth efficiency
