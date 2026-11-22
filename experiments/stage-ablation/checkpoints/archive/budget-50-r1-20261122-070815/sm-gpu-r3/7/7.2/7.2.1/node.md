# N375: RTX 4080 Super 16GB 在 Qwen3-27B INT4 权重 (13.5GB) + 32K BF16 KV Cache (2.0GB) 配置下

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N132

## Claim

RTX 4080 Super 16GB 在 Qwen3-27B INT4 权重 (13.5GB) + 32K BF16 KV Cache (2.0GB) 配置下，总显存需求为 15.5GB，剩余仅 0.5GB 用于激活值和系统开销，根据 vLLM/llama.cpp 实测数据，该剩余空间低于最小安全阈值（通常需 ≥1-2GB），导致 OOM 概率 >90% [待核验: 需查找具体框架的激活值峰值日志]

## Corrected Claim

RTX 4080 Super 16GB 在 Qwen3-27B INT4 权重 (13.5GB) + 32K BF16 KV Cache (2.0GB) 配置下，总显存需求为 15.5GB，剩余仅 0.5GB 用于激活值和系统开销。由于剩余空间极小，在实际推理中极易因激活值峰值或系统开销波动导致 OOM。

## Evidence

[质询]该陈述包含具体的经验性阈值（'通常需 ≥1-2GB'）和概率估计（'OOM 概率 >90%'），这些属于特定硬件和软件版本下的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4080 Super 16GB Qwen3 27B INT4 OOM out of memory activation peak size
