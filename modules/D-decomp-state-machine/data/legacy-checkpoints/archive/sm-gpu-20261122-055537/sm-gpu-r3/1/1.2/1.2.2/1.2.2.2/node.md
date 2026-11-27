# N143: NVIDIA H100 80GB SXM 运行 Qwen3-27B (BF16) 在 32K 上下文下的理论最大吞吐量：受限于 HBM3 带宽 (3350 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

NVIDIA H100 80GB SXM 运行 Qwen3-27B (BF16) 在 32K 上下文下的理论最大吞吐量：受限于 HBM3 带宽 (3350 GB/s) 和 BF16 权重大小 (54GB)，理论上限为 3350/54 ≈ 62.04 tokens/s；实际受 KV Cache 和计算开销影响，预计 40-55 tokens/s。

## Corrected Claim

NVIDIA H100 80GB SXM 运行 Qwen3-27B (BF16) 在 32K 上下文下的理论最大吞吐量：受限于 HBM3 带宽 (3350 GB/s) 和 BF16 权重大小 (54GB)，理论上限为 3350/54 ≈ 62.04 tokens/s；实际受 KV Cache 和计算开销影响，预计 40-55 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM HBM3带宽3.35TB/s与Qwen3-27B BF16权重约54GB（27B*2bytes）符合事实，算术推导3350/54≈62.04正确，且实际吞吐量受KV Cache和计算开销影响低于理论上限符合工程直觉。
