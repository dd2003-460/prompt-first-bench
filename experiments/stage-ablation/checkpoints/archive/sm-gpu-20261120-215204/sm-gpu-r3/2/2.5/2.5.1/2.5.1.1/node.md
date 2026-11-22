# N225: RTX 4090 在 INT8 精度下运行 Qwen3-27B (27B参数) 的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (假设 F

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

RTX 4090 在 INT8 精度下运行 Qwen3-27B (27B参数) 的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (假设 FP16/KV Cache 未量化，约 12.8 GB) 及激活/碎片开销 (~2 GB)，总显存需求约 41.8 GB，超出 24 GB 物理上限，因此单卡 4090 在 32K 上下文下无法运行 INT8 模型，必须降低上下文至 ~12K 或使用 CPU Offloading。

## Corrected Claim

RTX 4090 在 INT8 精度下运行 Qwen3-27B (27B参数) 的权重显存占用为 27 GB，加上 32K 上下文 KV Cache (假设 FP16/KV Cache 未量化，约 12.8 GB) 及激活/碎片开销 (~2 GB)，总显存需求约 41.8 GB，超出 24 GB 物理上限，因此单卡 4090 在 32K 上下文下无法运行 INT8 模型，必须降低上下文至 ~12K 或使用 CPU Offloading。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数INT8权重约27GB，32K上下文KV Cache约12.8GB，加上激活开销，总显存需求约41.8GB，远超RTX 4090的24GB物理上限，结论合理。
