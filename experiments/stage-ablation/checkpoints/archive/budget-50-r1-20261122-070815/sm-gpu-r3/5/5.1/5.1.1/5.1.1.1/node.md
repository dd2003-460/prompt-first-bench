# N337: Qwen3-27B 在 RTX 4090 (24GB) 上运行 BF16 精度时，因显存需求（54GB权重+2GB KV Cache > 24GB）导致无法加载

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

Qwen3-27B 在 RTX 4090 (24GB) 上运行 BF16 精度时，因显存需求（54GB权重+2GB KV Cache > 24GB）导致无法加载完整模型，必须采用 CPU Offloading 或量化，因此纯 BF16 单卡推理吞吐量数值不存在（为 0 或不可行状态），此结论修正了 N120 中隐含的'BF16在4090上可测吞吐'的前提。

## Corrected Claim

Qwen3-27B 在 RTX 4090 (24GB) 上运行 BF16 精度时，因显存需求（54GB权重+2GB KV Cache > 24GB）导致无法加载完整模型，必须采用 CPU Offloading 或量化，因此纯 BF16 单卡推理吞吐量数值不存在（为 0 或不可行状态），此结论修正了 N120 中隐含的'BF16在4090上可测吞吐'的前提。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16精度下权重占用约54GB，远超RTX 4090的24GB显存，物理上无法加载完整模型，故纯BF16单卡推理不可行。
