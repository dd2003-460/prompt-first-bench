# N287: Apple M2 Ultra 在 32K 上下文下的 KV Cache 显存占用计算：与 N83 相同公式，KV_Cache ≈ 25.8 GB (BF16)。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N111

## Claim

Apple M2 Ultra 在 32K 上下文下的 KV Cache 显存占用计算：与 N83 相同公式，KV_Cache ≈ 25.8 GB (BF16)。M2 Ultra 192GB 统一内存扣除系统占用 (约 20-30GB) 后，剩余 ~160GB 足以容纳 54GB 权重 + 25.8GB KV Cache，无溢出风险，但带宽瓶颈导致速度远低于 H100。

## Corrected Claim

Apple M2 Ultra 在 32K 上下文下的 KV Cache 显存占用计算：与 N83 相同公式，KV_Cache ≈ 25.8 GB (BF16)。M2 Ultra 192GB 统一内存扣除系统占用 (约 20-30GB) 后，剩余 ~160GB 足以容纳 54GB 权重 + 25.8GB KV Cache，无溢出风险，但带宽瓶颈导致速度远低于 H100。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 192GB 统一内存扣除系统开销后剩余容量足以容纳 54GB 权重与 25.8GB KV Cache，且带宽瓶颈导致推理速度低于 H100 符合硬件特性常识。
