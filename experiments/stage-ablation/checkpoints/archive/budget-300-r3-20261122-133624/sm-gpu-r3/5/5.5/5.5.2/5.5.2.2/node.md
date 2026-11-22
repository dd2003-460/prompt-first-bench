# N401: 排序反转的临界电价 P_crit 计算公式：P_crit = (C_hw_A - C_hw_B) / (S_A - S_B)，其中 A 和 B 为两个对比方案。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N156

## Claim

排序反转的临界电价 P_crit 计算公式：P_crit = (C_hw_A - C_hw_B) / (S_A - S_B)，其中 A 和 B 为两个对比方案。例如 2x4090 ($3,198, S=2332.8) vs 1xH100 ($25,000, S=7574.4)，P_crit = ($25,000 - $3,198) / (7574.4 - 2332.8) = $21,802 / 5241.6 ≈ $4.16/kWh。由于实际电价远低于此值，电力成本不会导致 2x4090 和 H100 的 TCO 排序反转，硬件成本差异主导决策。

## Corrected Claim

排序反转的临界电价 P_crit 计算公式：P_crit = (C_hw_A - C_hw_B) / (S_A - S_B)，其中 A 和 B 为两个对比方案。例如 2x4090 ($3,198, S=2332.8) vs 1xH100 ($25,000, S=7574.4)，P_crit = ($25,000 - $3,198) / (7574.4 - 2332.8) = $21,802 / 5241.6 ≈ $4.16/kWh。由于实际电价远低于此值，电力成本不会导致 2x4090 和 H100 的 TCO 排序反转，硬件成本差异主导决策。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合线性成本模型，数值计算准确（21802/5241.6≈4.16），且结论符合当前电力市场常识（电价远低于4.16美元/千瓦时）。

## Search Query

critical electricity price for TCO crossover high power vs low power GPU cluster
