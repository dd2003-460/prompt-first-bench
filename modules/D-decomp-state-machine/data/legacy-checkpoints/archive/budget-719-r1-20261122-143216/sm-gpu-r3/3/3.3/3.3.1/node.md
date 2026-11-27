# N86: 2×RTX 4090 通过张量并行 (Tensor Parallelism) 在 BF16 精度下解码 Qwen3-27B (Batch Size=1) 的吞吐

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

2×RTX 4090 通过张量并行 (Tensor Parallelism) 在 BF16 精度下解码 Qwen3-27B (Batch Size=1) 的吞吐量受限于 PCIe Gen4 x16 互联带宽 (32 GB/s) 而非显存带宽，其理论上限远低于单卡 5090 的显存带宽瓶颈，预估实际吞吐量为 15-20 tokens/s。

## Corrected Claim

2×RTX 4090 通过张量并行在 BF16 精度下解码 Qwen3-27B (Batch Size=1) 时，若未使用量化或特殊优化，其吞吐量主要受限于 PCIe Gen4 互联带宽，理论上限极低（约 <1 token/s）；若实际测得 15-20 tokens/s，则可能涉及 KV Cache 优化、量化或并非纯张量并行瓶颈，原陈述中瓶颈归因与数值不符。

## Evidence

[质询]数值量级与瓶颈判断存疑：2x4090 的显存带宽（~1.6TB/s）远高于 PCIe Gen4（~32GB/s），在 BF16 下 27B 模型每 token 需读取约 54GB 权重，若受限于 PCIe，理论上限约为 0.6 tokens/s，而非 15-20 tokens/s；若实际达到 15-20 tokens/s，则说明并未受限于 PCIe 带宽，或者使用了 KV Cache 优化/量化/其他未提及的并行策略，陈述中‘受限于 PCIe’与‘15-20 tokens/s’在纯张量并行 BF16 场景下存在逻辑矛盾。 | 先验知识/题面给定，逻辑校验发现瓶颈描述与吞吐量数值不匹配：PCIe 带宽瓶颈下 27B BF16 模型吞吐应远低于 15 tokens/s，故降级。
