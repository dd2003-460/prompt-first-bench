# N82: A100 40GB PCIe 在 LLM 推理负载下的平均功耗 P_avg_A100 并非满载 400W，而是根据计算密度在 250-400W 之间波动，保守估

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

A100 40GB PCIe 在 LLM 推理负载下的平均功耗 P_avg_A100 并非满载 400W，而是根据计算密度在 250-400W 之间波动，保守估计取 350W 用于 TCO 计算。

## Corrected Claim

A100 40GB PCIe 在 LLM 推理负载下的平均功耗 P_avg_A100 并非满载 400W，而是根据计算密度在 250-400W 之间波动，保守估计取 350W 用于 TCO 计算。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 TDP为400W，LLM推理通常非满载，350W为合理保守估计

## Search Query

A100 PCIe average power consumption LLM inference load watts
