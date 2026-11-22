# N108: 效应量与置信度映射函数：定义置信度 C = 1 - P(complete_ignoring|d)，假设 d=0.3 时完全忽略概率为 0.25，d=0.5 时为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

效应量与置信度映射函数：定义置信度 C = 1 - P(complete_ignoring|d)，假设 d=0.3 时完全忽略概率为 0.25，d=0.5 时为 0.15，则 C(0.3) = 0.75, C(0.5) = 0.85，父节点中的0.8对应于 Cohen's d ≈ 0.4 的中间状态，而非效应量上限。

## Corrected Claim

效应量与置信度映射函数：定义置信度 C = 1 - P(complete_ignoring|d)，假设 d=0.3 时完全忽略概率为 0.25，d=0.5 时为 0.15，则 C(0.3) = 0.75, C(0.5) = 0.85，父节点中的0.8对应于 Cohen's d ≈ 0.4 的中间状态，而非效应量上限。

## Evidence

先验知识/题面给定，逻辑校验通过：C=1-P，代入数值计算正确（1-0.25=0.75, 1-0.15=0.85），且0.8介于0.75和0.85之间，对应d≈0.4符合线性插值逻辑，无内部矛盾。
