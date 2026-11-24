# N594: 有效计费容量成本修正系数 k_cost = 1.0 / f_eff，若 f_eff=0.825，则 k_cost = 1.212，即实际每 TB 成本需乘以 1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N211

## Claim

有效计费容量成本修正系数 k_cost = 1.0 / f_eff，若 f_eff=0.825，则 k_cost = 1.212，即实际每 TB 成本需乘以 1.212 以补偿吞吐损失

## Corrected Claim

有效计费容量成本修正系数 k_cost = 1.0 / f_eff，若 f_eff=0.825，则 k_cost = 1.212，即实际每 TB 成本需乘以 1.212 以补偿吞吐损失

## Evidence

先验知识/题面给定，逻辑校验通过：k_cost = 1/f_eff 是标准的成本修正定义，1/0.825 ≈ 1.2121，数值计算准确，逻辑自洽。
