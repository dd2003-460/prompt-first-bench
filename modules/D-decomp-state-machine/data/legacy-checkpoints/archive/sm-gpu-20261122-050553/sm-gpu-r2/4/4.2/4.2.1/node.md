# N81: RTX 4090 在 LLM 推理负载下的平均功耗 P_avg_4090 并非满载 450W，而是根据计算密度在 300-450W 之间波动，保守估计取 400

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

RTX 4090 在 LLM 推理负载下的平均功耗 P_avg_4090 并非满载 450W，而是根据计算密度在 300-450W 之间波动，保守估计取 400W 用于 TCO 计算。

## Corrected Claim

RTX 4090 在 LLM 推理负载下的平均功耗 P_avg_4090 并非满载 450W，而是根据计算密度在 300-450W 之间波动，保守估计取 400W 用于 TCO 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 TDP为450W，LLM推理负载通常未达满载，300-450W波动范围及400W保守估计符合工程直觉与物理规律。

## Search Query

RTX 4090 average power consumption LLM inference load watts
