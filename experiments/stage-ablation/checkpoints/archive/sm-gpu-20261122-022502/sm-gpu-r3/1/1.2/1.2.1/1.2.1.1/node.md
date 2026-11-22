# N114: L40S 48GB 在 INT8 量化下的理论解码吞吐量上限为 86.7 tokens/s (48GB / (27GB权重 + 2GB KV Cache/32K

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

L40S 48GB 在 INT8 量化下的理论解码吞吐量上限为 86.7 tokens/s (48GB / (27GB权重 + 2GB KV Cache/32K + 2GB 缓冲) * 864GB/s 带宽)，实际受限于计算瓶颈和驱动优化，预计实测值为 35-45 tokens/s。

## Corrected Claim

L40S 48GB 在 INT8 量化下，若模型权重约 27GB 且 KV Cache 占用约 2GB，理论带宽受限的解码吞吐量上限约为 86.7 tokens/s；实际性能受计算瓶颈和驱动优化影响，典型实测值可能在 35-45 tokens/s 区间（具体取决于模型架构和软件栈）。

## Evidence

[质询]该陈述包含具体的硬件规格（L40S 48GB 版本、864GB/s 带宽）和特定的模型/场景参数（27GB 权重、32K KV Cache），属于经验事实。虽然 L40S 标准版通常为 48GB 显存且带宽约为 864GB/s，但 '27GB 权重' 和 '35-45 tokens/s' 的实测预估高度依赖于未指明的具体模型（如 Llama-3-70B 还是其他模型）及软件栈优化程度，缺乏通用性，且 'L40S 48GB' 这一具体 SKU 的普及度及确切带宽在不同批次/驱动下可能存在细微差异，无法仅凭逻辑推导确认为普适真理。 | 经验事实，逻辑自洽但缺来源支持。计算逻辑（显存占用估算、带宽除以数据量）在量级上合理，但具体数值（27GB权重、35-45 tokens/s）为特定场景下的经验估算，非第一性原理可严格推导的普适常数，且无外部来源验证。
