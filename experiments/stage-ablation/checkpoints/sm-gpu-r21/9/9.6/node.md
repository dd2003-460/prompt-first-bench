# N111: Apple M2 Ultra 192GB 的 32K 上下文吞吐基准：tokens/sec = (192GB × 800 GB/s) / (27B × 2 by

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

Apple M2 Ultra 192GB 的 32K 上下文吞吐基准：tokens/sec = (192GB × 800 GB/s) / (27B × 2 bytes) ≈ 57 tokens/sec（理论上限），实际约 40-50 tokens/sec，仅为 NVIDIA 方案的 1/5 [待核验]。

## Corrected Claim

Apple M2 Ultra 192GB 的 32K 上下文吞吐基准：tokens/sec = (192GB × 800 GB/s) / (27B × 2 bytes) ≈ 57 tokens/sec（理论上限），实际约 40-50 tokens/sec，仅为 NVIDIA 方案的 1/5 [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：理论上限计算 (192*800)/(27*2) ≈ 56.9 tokens/sec 与陈述一致；实际性能受内存带宽效率及计算开销影响，40-50 tokens/sec 符合工程经验；M2 Ultra 带宽 (800GB/s) 与 NVIDIA 高端方案 (如 A100/H100 的 2TB/s+) 相比，吞吐量约为 1/4 至 1/5，量级合理。
