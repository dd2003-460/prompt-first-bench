# N191: 在 27B 模型上执行 Self-Consistency (k=5) 的额外计算开销为 4 次完整推理（1次基准+4次重采样），总耗时 T_SC = 5 * T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N68

## Claim

在 27B 模型上执行 Self-Consistency (k=5) 的额外计算开销为 4 次完整推理（1次基准+4次重采样），总耗时 T_SC = 5 * T_single_infer；若 T_single_infer=5s，则 T_SC=25s，较单次推理增加 400% 延迟。

## Corrected Claim

在 27B 模型上执行 Self-Consistency (k=5) 的额外计算开销为 4 次完整推理（1次基准+4次重采样），总耗时 T_SC = 5 * T_single_infer；若 T_single_infer=5s，则 T_SC=25s，较单次推理增加 400% 延迟。

## Evidence

先验知识/题面给定，逻辑校验通过：Self-Consistency k=5 需生成5个样本，计算量为单次的5倍，耗时线性叠加，百分比增加计算正确（(5-1)/1=400%）。
