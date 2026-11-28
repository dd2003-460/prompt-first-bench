# N97: 性能分界点定义：设候选硬件 X (如 4090) 和 Y (如 3090) 的标称吞吐分别为 T_X 和 T_Y。性能分界点 Threshold = (T_X 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

性能分界点定义：设候选硬件 X (如 4090) 和 Y (如 3090) 的标称吞吐分别为 T_X 和 T_Y。性能分界点 Threshold = (T_X + T_Y) / 2。若推荐方案 X 的吞吐置信区间 [T_X - 0.1T_X, T_X + 0.1T_X] 跨越了 Threshold，则决策置信度低。例如，若 T_X=100 tok/s, T_Y=95 tok/s，Threshold=97.5，X 的下界 90 < 97.5，区间跨越，决策不稳定。

## Corrected Claim

性能分界点定义：设候选硬件 X (如 4090) 和 Y (如 3090) 的标称吞吐分别为 T_X 和 T_Y。性能分界点 Threshold = (T_X + T_Y) / 2。若推荐方案 X 的吞吐置信区间 [T_X - 0.1T_X, T_X + 0.1T_X] 跨越了 Threshold，则决策置信度低。例如，若 T_X=100 tok/s, T_Y=95 tok/s，Threshold=97.5，X 的下界 90 < 97.5，区间跨越，决策不稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（(100+95)/2=97.5, 100*0.9=90），区间跨越判断符合定义，无内部矛盾。
