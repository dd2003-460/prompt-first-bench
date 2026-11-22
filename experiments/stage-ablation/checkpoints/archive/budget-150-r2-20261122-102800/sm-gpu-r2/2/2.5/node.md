# N17: 多卡方案显存分布与通信开销：2×RTX 4090 (48GB total) 运行BF16时，权重分片每卡27GB，KV Cache分片每卡2.15GB，总显存每

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

多卡方案显存分布与通信开销：2×RTX 4090 (48GB total) 运行BF16时，权重分片每卡27GB，KV Cache分片每卡2.15GB，总显存每卡~30.5GB < 24GB? 否，30.5 > 24，故2×4090无法运行BF16 Qwen3-27B 32K上下文；2×RTX 3090 (48GB total) 同理；2×A6000 (96GB total) 运行BF16时每卡~30.9GB < 48GB，可行

## Corrected Claim

2×RTX 4090 (48GB total) 运行BF16时，权重分片每卡27GB，KV Cache分片每卡2.15GB，总显存每卡~29.15GB > 24GB，故2×4090无法运行BF16 Qwen3-27B 32K上下文；2×RTX 3090 (48GB total) 同理；2×A6000 (96GB total) 运行BF16时每卡~29.15GB < 48GB，可行

## Evidence

父节点级核验未通过：不完备（子节点之间针对不同硬件配置（4090-BF16, 4090-INT8, A6000-BF16）和量化策略，内容互斥且无矛盾，正交性良好。然而，父节点明确包含 '2×RTX 3090 (48GB total) 同理' 的结论，子节点中完全缺失对 3090 的讨论，导致覆盖不完整。）

## Search Query

multi-GPU tensor parallelism 27B LLM VRAM per GPU BF16 KV cache sharding
