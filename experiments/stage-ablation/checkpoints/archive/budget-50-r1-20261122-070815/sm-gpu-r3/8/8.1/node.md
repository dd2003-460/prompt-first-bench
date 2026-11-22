# N138: Apple Mac Studio M2 Ultra 192GB 版本价格约 $4000-$5000，内存带宽 800 GB/s，运行 Qwen3-27B INT

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

Apple Mac Studio M2 Ultra 192GB 版本价格约 $4000-$5000，内存带宽 800 GB/s，运行 Qwen3-27B INT4 (13.5GB) 时，理论 decode 速度上限为 800 / 13.5 ≈ 59 tokens/s，略低于 RTX 4090 的 65 tokens/s，但支持 32K 上下文且无显存碎片问题

## Corrected Claim

Apple Mac Studio M2 Ultra 192GB 版本价格约 $4000-$5000，内存带宽 800 GB/s，运行 Qwen3-27B INT4 (13.5GB) 时，理论 decode 速度上限为 800 / 13.5 ≈ 59 tokens/s，略低于 RTX 4090 的 65 tokens/s，但支持 32K 上下文且无显存碎片问题

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 内存带宽确为 800GB/s，Qwen3-27B INT4 模型大小约 13.5GB-15GB，800/13.5≈59 tokens/s 符合内存带宽瓶颈下的理论上限估算逻辑；RTX 4090 显存带宽 1008GB/s，若模型大小相近，65 tokens/s 亦在合理量级范围内（实际受其他开销影响可能更低，但作为对比基准逻辑自洽）。
