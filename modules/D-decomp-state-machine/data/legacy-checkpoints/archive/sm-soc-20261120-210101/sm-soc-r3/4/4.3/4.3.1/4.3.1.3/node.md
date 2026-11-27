# N286: 新品占比 w_new 的动态计算口径：w_new 不应为静态常数，而应基于近7天该品类成交量加权计算：w_new = Σ(Quantity_i * I[Cond

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

新品占比 w_new 的动态计算口径：w_new 不应为静态常数，而应基于近7天该品类成交量加权计算：w_new = Σ(Quantity_i * I[Condition_i > Threshold]) / Σ(Quantity_i)，其中 Threshold 为成色判定阈值（如 S>0.8）。

## Corrected Claim

新品占比 w_new 的动态计算口径：w_new 不应为静态常数，而应基于近7天该品类成交量加权计算：w_new = Σ(Quantity_i * I[Condition_i > Threshold]) / Σ(Quantity_i)，其中 Threshold 为成色判定阈值（如 S>0.8）。

## Evidence

先验知识/题面给定，逻辑校验通过
