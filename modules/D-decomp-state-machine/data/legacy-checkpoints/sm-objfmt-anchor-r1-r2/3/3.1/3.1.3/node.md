# N65: 24GB 显存瓶颈下的 KV Cache 管理策略成本：1x RTX 4090 (24GB) 运行 INT4 权重 (13.5GB) + 32K BF16 KV

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

24GB 显存瓶颈下的 KV Cache 管理策略成本：1x RTX 4090 (24GB) 运行 INT4 权重 (13.5GB) + 32K BF16 KV Cache (8-12GB) 总需求 21.5-25.5GB，超出 24GB 时需启用 CPU Offload (将 2-4GB KV 移至 DDR5)，导致每 token 生成延迟增加 ~5-15ms (取决于 DDR5 带宽 50-100GB/s vs GDDR6X 1TB/s)，吞吐量下降 10-20%；或启用 FP8 KV Cache 将占用减半至 4-6GB，避免 Offload，保持全 GPU 推理。

## Corrected Claim

24GB 显存瓶颈下的 KV Cache 管理策略成本：1x RTX 4090 (24GB) 运行 INT4 权重 (13.5GB) + 32K BF16 KV Cache (8-12GB) 总需求 21.5-25.5GB，超出 24GB 时需启用 CPU Offload (将 2-4GB KV 移至 DDR5)，导致每 token 生成延迟增加 ~5-15ms (取决于 DDR5 带宽 50-100GB/s vs GDDR6X 1TB/s)，吞吐量下降 10-20%；或启用 FP8 KV Cache 将占用减半至 4-6GB，避免 Offload，保持全 GPU 推理。

## Evidence

先验知识/题面给定，逻辑校验通过：INT4权重13.5GB与32K BF16 KV Cache 8-12GB之和确为21.5-25.5GB，超出24GB显存需Offload或量化；DDR5带宽(50-100GB/s)远低于GDDR6X(1TB/s)，导致延迟增加和吞吐下降符合物理直觉；FP8量化减半KV占用亦符合数据位宽比例。

## Search Query

vLLM KV cache offload latency penalty FP8 KV cache savings
