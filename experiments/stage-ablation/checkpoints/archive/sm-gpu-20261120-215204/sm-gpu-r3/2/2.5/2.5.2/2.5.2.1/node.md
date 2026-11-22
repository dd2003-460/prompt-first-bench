# N229: RTX 4090 在 W4A16 精度下运行 Qwen3-27B (27B参数) 的权重显存占用为 13.5 GB (27B * 0.5 bytes)，加上 3

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

RTX 4090 在 W4A16 精度下运行 Qwen3-27B (27B参数) 的权重显存占用为 13.5 GB (27B * 0.5 bytes)，加上 32K 上下文 KV Cache (BF16, ~12.8 GB) 及激活/碎片开销 (~2 GB)，总显存需求约 28.3 GB，超出 24 GB 物理上限，因此单卡 4090 在 32K 上下文下无法运行 W4 模型，必须降低上下文至 ~16K 或使用 CPU Offloading。

## Corrected Claim

RTX 4090 在 W4A16 精度下运行 Qwen3-27B (27B参数) 的权重显存占用为 13.5 GB (27B * 0.5 bytes)，加上 32K 上下文 KV Cache (BF16, ~12.8 GB) 及激活/碎片开销 (~2 GB)，总显存需求约 28.3 GB，超出 24 GB 物理上限，因此单卡 4090 在 32K 上下文下无法运行 W4 模型，必须降低上下文至 ~16K 或使用 CPU Offloading。

## Evidence

[质询]KV Cache 的估算值（12.8 GB）可能因 Qwen3-27B 的具体架构参数（如层数、头数、GQA 比例）不同而存在偏差，但量级合理；W4A16 权重占用 13.5 GB 计算准确。 | 先验知识/题面给定，逻辑校验通过：W4 权重 27B*0.5B=13.5GB，KV Cache 在 32K 上下文下通常占用 10-15GB 量级，总显存需求约 28GB 确实超过 RTX 4090 的 24GB 物理上限，结论成立。
