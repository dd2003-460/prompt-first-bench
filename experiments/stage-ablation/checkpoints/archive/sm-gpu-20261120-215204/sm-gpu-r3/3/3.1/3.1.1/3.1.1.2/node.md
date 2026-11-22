# N237: RTX 4090 (24GB) 在 W4A16 权重 + BF16 KV Cache + 32K 上下文下的总显存需求重算：权重 13.5GB (27B * 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

RTX 4090 (24GB) 在 W4A16 权重 + BF16 KV Cache + 32K 上下文下的总显存需求重算：权重 13.5GB (27B * 0.5 bytes) + KV Cache 8.0GB (N135) + 激活/碎片开销 2.0GB = 23.5GB。该值 < 24GB 物理上限，结论修正为：在严格限制 Batch Size=1 且无额外中间层缓存的情况下，单卡 4090 理论上可容纳 32K 上下文的 W4A16+BF16 KV 配置，但余量极小 (0.5GB)，极易因 CUDA 上下文或框架开销溢出，需实测验证。

## Corrected Claim

RTX 4090 (24GB) 在 W4A16 权重 + BF16 KV Cache + 32K 上下文下的总显存需求重算：权重 13.5GB (27B * 0.5 bytes) + KV Cache 8.0GB (N135) + 激活/碎片开销 2.0GB = 23.5GB。该值 < 24GB 物理上限，结论修正为：在严格限制 Batch Size=1 且无额外中间层缓存的情况下，单卡 4090 理论上可容纳 32K 上下文的 W4A16+BF16 KV 配置，但余量极小 (0.5GB)，极易因 CUDA 上下文或框架开销溢出，需实测验证。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数W4量化权重约13.5GB，加上8GB KV Cache及2GB开销，总计23.5GB，小于24GB显存，计算逻辑自洽且符合工程常识。

## Search Query

RTX 4090 24GB VRAM limit LLM inference overhead CUDA context size
