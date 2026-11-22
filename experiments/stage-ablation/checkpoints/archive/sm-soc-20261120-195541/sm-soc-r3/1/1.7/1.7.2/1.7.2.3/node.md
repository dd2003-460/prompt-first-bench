# N121: 更新频率 f_update_freq 的约束条件：若 f_update_freq > 2 次/天（即 T_update_days < 0.5 天），则 γ_da

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N41

## Claim

更新频率 f_update_freq 的约束条件：若 f_update_freq > 2 次/天（即 T_update_days < 0.5 天），则 γ_data_update > $0.004，总成本 γ > $0.009，接近 $0.01 阈值；若 f_update_freq = 4 次/天，则 γ = $0.005 + $0.008 = $0.013，超过初始假设，需评估 ROI 是否覆盖额外成本。

## Corrected Claim

更新频率 f_update_freq 的约束条件：若 f_update_freq > 2 次/天（即 T_update_days < 0.5 天），则 γ_data_update > $0.004，总成本 γ > $0.009，接近 $0.01 阈值；若 f_update_freq = 4 次/天，则 γ = $0.005 + $0.008 = $0.013，超过初始假设，需评估 ROI 是否覆盖额外成本。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算（0.005+0.008=0.013）正确，且符合成本随频率增加而上升的经济直觉，无内部矛盾。

## Search Query

data update frequency cost threshold e-commerce
