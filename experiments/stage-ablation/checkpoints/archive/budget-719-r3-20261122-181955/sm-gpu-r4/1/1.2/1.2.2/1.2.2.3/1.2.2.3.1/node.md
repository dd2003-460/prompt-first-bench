# N456: A100 40GB PCIe 在 INT4 权重配置下的显存占用为 13.5 GB，框架开销估算为 1.5 GB，剩余可用显存 = 40 - 13.5 - 1.

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N155

## Claim

A100 40GB PCIe 在 INT4 权重配置下的显存占用为 13.5 GB，框架开销估算为 1.5 GB，剩余可用显存 = 40 - 13.5 - 1.5 = 25 GB。

## Corrected Claim

A100 40GB PCIe 在 INT4 权重配置下的显存占用为 13.5 GB，框架开销估算为 1.5 GB，剩余可用显存 = 40 - 13.5 - 1.5 = 25 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 40 - 13.5 - 1.5 = 25 正确，且 INT4 权重占用 13.5GB 在 A100 40GB 卡上属于合理量级（通常大模型 INT4 权重+KV Cache 等开销后剩余显存用于推理，此处仅计算静态占用与框架开销，逻辑自洽）。
