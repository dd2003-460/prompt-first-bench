# N662: RTX 5090 575W TDP 中约 30-35% 用于 GPU 核心，65-70% 用于显存供电和 PCB 损耗，实际推理负载下（非峰值游戏场景）平均功耗

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N203, N204, N205

## Claim

RTX 5090 575W TDP 中约 30-35% 用于 GPU 核心，65-70% 用于显存供电和 PCB 损耗，实际推理负载下（非峰值游戏场景）平均功耗通常在 450-500W 之间，年电力成本应按平均功耗而非 TDP 峰值计算。

## Corrected Claim

RTX 5090 的 TDP 为 575W。在典型推理负载下，其平均功耗通常低于 TDP 峰值，具体数值取决于工作负载和驱动优化，建议根据实际监控数据计算年电力成本，而非直接套用固定比例或区间。

## Evidence

[质询]该陈述包含具体的硬件功耗分配比例（30-35% vs 65-70%）和特定负载下的平均功耗数值（450-500W），属于经验事实。缺乏来源支持时，无法验证这些具体数值的准确性，且不同负载场景下功耗波动较大，固定区间可能过于绝对。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 5090 average power consumption LLM inference load watts
