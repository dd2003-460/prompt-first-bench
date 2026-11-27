# N305: A100 80GB PCIe 在 LLM 推理负载下的实测平均功耗约为 210-240 W，占 TDP (300W) 的 70%-80%；修正 N98 中假设的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102, N103, N104

## Claim

A100 80GB PCIe 在 LLM 推理负载下的实测平均功耗约为 210-240 W，占 TDP (300W) 的 70%-80%；修正 N98 中假设的 400W 错误，采用 N102 定义的 300W TDP 作为基准。

## Corrected Claim

A100 80GB PCIe 在 LLM 推理负载下的实测平均功耗通常低于其 300W TDP 上限，具体数值需依据实际负载和散热条件测定；修正 N98 中假设的 400W 错误，采用 N102 定义的 300W TDP 作为基准。

## Evidence

[质询]该陈述包含具体的经验性功耗数值（210-240W）和百分比范围，属于经验事实而非第一性原理可推导内容；且缺乏外部来源支持，无法排除不同负载场景下功耗波动导致该范围不准确的可能性。 | 经验事实，逻辑自洽（210-240W在300W TDP范围内且符合LLM推理高负载特征）但缺来源支持

## Search Query

A100 80GB PCIe power consumption LLM inference average watts
