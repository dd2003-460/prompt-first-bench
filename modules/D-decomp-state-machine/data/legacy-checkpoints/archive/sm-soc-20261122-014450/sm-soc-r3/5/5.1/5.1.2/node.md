# N90: 不确定性范围计算公式：对于置信度为 C 的断言，其95%置信区间宽度 W = (1 - C) * V_max，其中 V_max 为该参数可能的最大理论波动幅度（

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

不确定性范围计算公式：对于置信度为 C 的断言，其95%置信区间宽度 W = (1 - C) * V_max，其中 V_max 为该参数可能的最大理论波动幅度（如价格弹性 E ∈ [-5, 0.5] 时 V_max=5.5）。

## Corrected Claim

不确定性范围计算公式：对于置信度为 C 的断言，其95%置信区间宽度 W = (1 - C) * V_max，其中 V_max 为该参数可能的最大理论波动幅度（如价格弹性 E ∈ [-5, 0.5] 时 V_max=5.5）。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了公式中 V_max 的定义，缺失了对置信度 C 和置信区间宽度 W 的解释，未完整覆盖父节点公式的所有关键变量。）
