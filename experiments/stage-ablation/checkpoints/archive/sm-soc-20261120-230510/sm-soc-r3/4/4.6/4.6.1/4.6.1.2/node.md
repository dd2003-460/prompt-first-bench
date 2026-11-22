# N243: 工作点2（中多样性-效用损失均衡）：当 N_choices = 10 时，E[min(V_i)] 显著上升，V_selection = V_max - E[mi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N80

## Claim

工作点2（中多样性-效用损失均衡）：当 N_choices = 10 时，E[min(V_i)] 显著上升，V_selection = V_max - E[min(V_i|N=10)]；根据截断正态分布参数（μ=V, σ=0.1V），计算 E[min(V_i)] ≈ V - 1.5σ，此时 V_selection ≈ 1.5σ，代表典型的强筛选干预后的状态，买家牺牲部分多样性换取价格确定性。

## Corrected Claim

工作点2（中多样性-效用损失均衡）：当 N_choices = 10 时，E[min(V_i)] 显著上升，V_selection = V_max - E[min(V_i|N=10)]；根据截断正态分布参数（μ=V, σ=0.1V），计算 E[min(V_i)] ≈ V - 1.5σ，此时 V_selection ≈ 1.5σ，代表典型的强筛选干预后的状态，买家牺牲部分多样性换取价格确定性。

## Evidence

先验知识/题面给定，逻辑校验通过：基于截断正态分布（μ=V, σ=0.1V）及N=10的样本量，E[min(V_i)] ≈ V - 1.5σ 符合统计学直觉（10个样本的最小值期望通常位于均值下方1-2个标准差范围内），推导出的 V_selection ≈ 1.5σ 在量纲和数值量级上均合理。
