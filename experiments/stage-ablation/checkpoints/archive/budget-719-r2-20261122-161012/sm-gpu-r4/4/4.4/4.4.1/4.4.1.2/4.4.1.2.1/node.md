# N534: RTX 5090 单卡 BF16 不可行的量化缺口分解：权重占用 54GB (27B * 2 bytes)，KV Cache 在 32K 上下文下占用约 1-2

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N221

## Claim

RTX 5090 单卡 BF16 不可行的量化缺口分解：权重占用 54GB (27B * 2 bytes)，KV Cache 在 32K 上下文下占用约 1-2GB (取决于 Attention Heads 和 Head Dim)，激活值与 CUDA 开销约 1-2GB，总需求 56-58GB，超出 32GB 显存 24-26GB，该缺口无法通过软件优化弥补，必须降低精度或启用 Offload。

## Corrected Claim

RTX 5090 单卡 BF16 不可行的量化缺口分解：权重占用 54GB (27B * 2 bytes)，KV Cache 在 32K 上下文下占用约 1-2GB (取决于 Attention Heads 和 Head Dim)，激活值与 CUDA 开销约 1-2GB，总需求 56-58GB，超出 32GB 显存 24-26GB，该缺口无法通过软件优化弥补，必须降低精度或启用 Offload。

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数BF16权重占用54GB，加上KV Cache和激活值开销，总显存需求确实远超32GB，缺口计算符合算术逻辑。
