# N155: A100 40GB PCIe 在 INT4 权重 + INT8 KV Cache 配置下的理论 Decode 吞吐量为 1555 / (16.38 + 13.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

A100 40GB PCIe 在 INT4 权重 + INT8 KV Cache 配置下的理论 Decode 吞吐量为 1555 / (16.38 + 13.5) ≈ 52.0 tokens/s，高于 A100 80GB 的 BF16 方案（23.5 tokens/s），但需确认 INT8 KV Cache 对精度的影响是否可接受（通常 <1% 损失）。

## Corrected Claim

A100 40GB PCIe 在 INT4 权重 + INT8 KV Cache 配置下的理论 Decode 吞吐量为 1555 / (16.38 + 13.5) ≈ 52.0 tokens/s，高于 A100 80GB 的 BF16 方案（23.5 tokens/s），但需确认 INT8 KV Cache 对精度的影响是否可接受（通常 <1% 损失）。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 1555/29.88 ≈ 52.0 正确，且 INT4/INT8 量化方案在理论吞吐上优于 BF16 符合硬件带宽与计算量减少的基本原理。
