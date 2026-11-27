# N266: 修正 N87 中的功耗参数：基于 N81 的修正，2×RTX 4090 的平均功耗 P_total 应取 2 × 400W = 800W（而非 900W），用于

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

修正 N87 中的功耗参数：基于 N81 的修正，2×RTX 4090 的平均功耗 P_total 应取 2 × 400W = 800W（而非 900W），用于计算局部温升 ΔT。

## Corrected Claim

修正 N87 中的功耗参数：基于 N81 的修正，2×RTX 4090 的平均功耗 P_total 应取 2 × 400W = 800W（而非 900W），用于计算局部温升 ΔT。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 的 TDP 为 450W，但在实际负载下平均功耗通常低于 TDP，取 400W 作为平均功耗估算值在工程上合理且保守，2×400W=800W 计算无误。

## Search Query

RTX 4090 average power consumption LLM inference
